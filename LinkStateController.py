from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpidToStr
import pox.openflow.discovery
from pox.lib.addresses import IPAddr, EthAddr
from pox.lib.packet.arp import arp
from pox.lib.packet.ethernet import ethernet,ETHER_BROADCAST
from pox.lib.packet.packet_base import packet_base
from pox.lib.packet.packet_utils import *
import pox.lib.packet as pkt
from pox.lib.recoco import Timer
import time
import datetime
import operator
log = core.getLogger()

all_ports = of.OFPP_FLOOD

HostList = {}

LinkList = []

DpidListU = []

DpidListV = []

CostDict = {}

Path = []

def FindNearDpidList(dpid,dpidlist):
  global LinkList
  ResultDpidList = []
  for i in range(len(LinkList)):
    if dpid == LinkList[i][0]:
      if LinkList[i][1] in dpidlist:
        ResultDpidList.append(LinkList[i][1])
    elif dpid == LinkList[i][1]:
      if LinkList[i][0] in dpidlist:
        ResultDpidList.append(LinkList[i][0])
  return ResultDpidList
def FindNearLinkList(dpid,dpidlist):
  global LinkList
  ResultLinkList = []
  for i in range(len(LinkList)):
    if (dpid == LinkList[i][0]) or (dpid == LinkList[i][1]):
      if (LinkList[i][0] in dpidlist) or (LinkList[i][1] in dpidlist):
        ResultLinkList.append(LinkList[i])
  return ResultLinkList

def FindMinCost(dpidlist,valuedict):
  tmp = valuedict[dpidlist[0]]
  tmpIndex = 0
  for i in range(len(dpidlist)):
    if tmp < valuedict[dpidlist[i]] or valuedict[dpidlist[i]] == -1:
      pass
    else:
      tmp = valuedict[dpidlist[i]]
      tmpIndex = dpidlist[i]
  return tmpIndex

def Dijkstra(dpid_src,dpid_dst):
  global LinkList,CostDict
  global DpidListU,DpidListV
  global Path
  DpidListU = []
  oldDpid = dpid_src
  oldValueDict = {}
  ValueDict = {}
  ChangeFlag = []
  FirstEnterFlag = True
  l = len(DpidListV)
  for i in range(l):
    ChangeFlag.append(False)
  for i in range(len(DpidListV)):
    Path.append([oldDpid])
  print "Init Path"
  print Path
  print "Dijkstra"
  print "LinkList:"
  print LinkList
  print "CostDict:"
  print CostDict
  for i in range(len(DpidListV)):
    ValueDict[DpidListV[i]] = -1
  ValueDict[oldDpid] = 0
  oldValueDict = ValueDict
  while 1:
    for i in range(l):
      ChangeFlag[i] = False
    print "Enter while"
    DpidListU.append(oldDpid)
    print "DpidListU:"
    print DpidListU
    print "DpidListV pre:"
    print DpidListV
    print "Index: %d" %DpidListV.index(oldDpid)
    tmpDpidListV = DpidListV
    del tmpDpidListV[DpidListV.index(oldDpid)]
    if not DpidListV:
      break
    DpidListV = tmpDpidListV
    print "DpidListV after:"
    print DpidListV
    tmpDpidList = FindNearDpidList(oldDpid,DpidListV)
    print "tmpDpidList:"
    print tmpDpidList
    tmpLinkList = FindNearLinkList(oldDpid,DpidListV)
    print "tmpLinkList:"
    print tmpLinkList
    tmpFunc = lambda x,y:(x,y) if x < y else (y,x)
    for i in range(len(tmpDpidList)):
      tmpValue = oldValueDict[oldDpid] + CostDict[tmpFunc(oldDpid,tmpDpidList[i])]
      if oldValueDict[tmpDpidList[i]] == -1:
        ValueDict[tmpDpidList[i]] = tmpValue
        ChangeFlag[tmpDpidList[i] - 1] = True
      elif (oldValueDict[tmpDpidList[i]] > tmpValue):
        ValueDict[tmpDpidList[i]] = tmpValue
        ChangeFlag[tmpDpidList[i] - 1] = True
    oldValueDict = ValueDict
    tmpMinIndex = FindMinCost(tmpDpidList,oldValueDict)
    print "ChangeFlag:"
    print ChangeFlag
    for i in range(len(tmpDpidList)):
      if ChangeFlag[tmpDpidList[i] - 1] == True:
        tmpPath = Path[tmpDpidList[i] - 1]
        if FirstEnterFlag == True:
          tmpPath.pop()
        tmpPath.append(oldDpid)
        tmpPath.append(tmpDpidList[i])
        Path[tmpDpidList[i] - 1] = tmpPath
    oldDpid = tmpMinIndex
    if FirstEnterFlag == True:
      FirstEnterFlag = False
    print "Path:"
    print Path
    print "Value Dict: "
    print oldValueDict
  print "Dijkstra Over"
LinkCounter = 0
class DiscoveryTopo(object):
  def __init__(self):
    global LinkList
    def startup():
      core.openflow.addListeners(self)
      core.openflow_discovery.addListeners(self)
    core.call_when_ready(startup,('openflow','openflow_discovery'))
    LinkList = []
  def _handle_LinkEvent(self,event):
    global LinkCounter
    LinkCounter += 1
    print "LinkCounter: %d" %LinkCounter
    global LinkList
    tmpLink = (event.link.dpid1,event.link.dpid2)
    tmpLink2 = (event.link.dpid2,event.link.dpid1)
    if (tmpLink not in LinkList) and (event.added == True):
      if tmpLink2 not in LinkList:
        LinkList.append(tmpLink)
        print "LinkEvent:"
        print tmpLink
mac_map = {}
loc = None
old_loc = None
buffer_id_1st = 0
TimeDpidDict = {}
PassedDpidList = []
Src = None
Dst = None
CallCounter = 0
class LinkStateController(object):
  def __init__(self,connection):
    global ConnectionList
    self.connection = connection
    connection.addListeners(self)
  def _handle_ConnectionUp(self,event):
    global DpidListV
    DpidListV.append(event.connection.dpid)
  def _handle_ConnectionDown(self,event):
    global DpidListV
    del DpidListV[DpidListV.index(event.connection.dpid)]
  def _handle_PacketIn(self,event):
    global loc,old_loc,mac_map
    global buffer_id_1st,TimeDpidDict,PassedDpidList
    global LinkList,CostDict
    global Src,Dst,CallCounter
    packet = event.parsed
    packet_in = event.ofp
    if buffer_id_1st == 0:
      buffer_id_1st = packet_in.buffer_id
      time_1st = datetime.datetime.now()
      TimeDpidDict[event.connection.dpid] = time_1st
      PassedDpidList.append(event.dpid)
    elif packet_in.buffer_id == buffer_id_1st:
      def DpidListInLinkList(dpid,linklist):
        ResultDpidList = []
        for i in range(len(linklist)):
          if dpid == linklist[i][0]:
            ResultDpidList.append(linklist[i][1])
            return ResultDpidList
      def IndexByDpidInLinkList(dpid1,dpid2,linklist):
        for i in range(len(linklist)):
          if (dpid1 == linklist[i][0]) or (dpid1 == linklist[i][1]):
            if (dpid2 == linklist[i][0]) or (dpid2 == linklist[i][1]):
              return i
      if not (event.dpid in PassedDpidList):
        PassedDpidList.append(event.dpid)
        TimeDpidDict[event.dpid] = datetime.datetime.now()
      tmpDpidList = DpidListInLinkList(event.dpid,LinkList)
      for i in range(len(tmpDpidList)):
        if TimeDpidDict.has_key(tmpDpidList[i]):
          passedTime = TimeDpidDict[event.dpid] - TimeDpidDict[tmpDpidList[i]]
          CostTime = (passedTime.microseconds + 500)/1000
          k = IndexByDpidInLinkList(tmpDpidList[i],event.dpid,LinkList)
          dpid_1 = LinkList[k][0]
          dpid_2 = LinkList[k][1]
          tmpDpid = (dpid_1 if dpid_1 <= dpid_2 else dpid_2)
          dpid_2 = (dpid_1 if dpid_1 > dpid_2 else dpid_2)
          dpid_1 = tmpDpid
          CostDict[dpid_1,dpid_2] = CostTime
    loc = (event.dpid,event.port)
    if packet.src in mac_map:
      old_loc = mac_map[packet.src]
    else:
      old_loc = None
    if old_loc == None:
      mac_map[packet.src] = loc
    elif old_loc != None and old_loc != loc and core.openflow_discovery.is_edge_port(loc[0],loc[1]):
      mac_map[packet.src] = loc
    if len(PassedDpidList) == len(DpidListV):
      if CallCounter == 0:
        CallCounter = 1
        MacList = mac_map.keys()
#        print MacList
        for i in range(len(MacList)):
          for j in range(i+1,len(MacList)):
            Dijkstra(mac_map[MacList[i]][0],mac_map[MacList[j]][0])
    msg = of.ofp_packet_out()
    msg.buffer_id = packet_in.buffer_id
    msg.in_port = packet_in.in_port
    msg.data = event.ofp
    action = of.ofp_action_output(port = of.OFPP_FLOOD)
    msg.actions.append(action)
    self.connection.send(msg)
  def _handle_portstats_received(event):
    pass
def launch():
  def start_switch(event):
    log.debug("Controlling %s" %(event.connection,))
    LinkStateController(event.connection)
  core.openflow.addListenerByName("ConnectionUp",start_switch)
  core.registerNew(DiscoveryTopo)
  def _timer_func3():
    return True
  Timer(5,_timer_func3,recurring = True)
