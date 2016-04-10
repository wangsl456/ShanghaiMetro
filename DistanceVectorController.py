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
from MetroStation import *
from MetroTopo import *
import time
import datetime
import operator
log = core.getLogger()
DpidList = []
#LinkList = []
PassedLinkList = []
PassedDpidList = []
TimeDpidDict = {}
TmpDpidDict = {}
unPassedDpidList = []
CostDict = {}
CostDictHop = {}
ValueDict = {}
loc = None
old_loc = None
mac_map = {}
buffer_id_1st = 0
Src = None
Dst = None
CallCounter = 0
Init = True
Path = []
INFTY = float("inf")
PrePath = {}
FirstEnter = True
FirstBellman = True
def FindMin(costlist):
      return costlist.index(min(costlist))
  pass
def DpidListNearDpid(dpid,linklist):
  ResultDpidList = []
  for i in range(len(linklist)):
    if dpid == linklist[i][0]:
      ResultDpidList.append(linklist[i][1])
    elif dpid == linklist[i][1]:
      ResultDpidList.append(linklist[i][0])
  return ResultDpidList
  pass
def isInLinkList(dpid,link):
  if (dpid == link[0]) or (dpid == link[1]):
    return True
  else:
    return False
  pass
def LinkListNearDpid(dpid,linklist):
  ResultLinkList = []
  for i in range(len(linklist)):
    if isInLinkList(dpid,linklist[i]):
      ResultLinkList.append(linklist[i])
  return ResultLinkList
  pass
def printpath(root):
  global PrePath
  while root != PrePath[root]:
    print "%s-->" %StationNameList[root],
    root = PrePath[root]
  if root == PrePath[root]:
    print "%s" %StationNameList[root]
def Bellman():
  global Init
  global CostDict,ValueDict
  global LinkList
  global DpidList
  global INFTY
  global PrePath
  global Src,Dst
  if Init:
    for i in range(len(LinkList)):
      if TimeCostDict.has_key(LinkList[i]):
        CostDict[LinkList[i]] = TimeCostDict[LinkList[i]]
      else:
        CostDict[LinkList[i]] = 300
    Init = False
    print "Enter the start station name: ",
    while True:
      SrcName = raw_input()
      if not (SrcName in StationNameList):
        print "Please enter a correct station name"
      else:
        break
    print "Enter the end station name: ",
    while True:
      DstName = raw_input()
      if not (DstName in StationNameList):
        print "Please enter a correct station name"
      else:
        break
    Src = StationNameList.index(SrcName)
    Dst = StationNameList.index(DstName)
    PrePath[Src] = Src
    for i in range(len(DpidList)):
      ValueDict[DpidList[i]] = 0 if DpidList[i] == Src else INFTY
  for i in range(len(DpidList)):
    for j in range(len(LinkList)):
      if(ValueDict[LinkList[j][0]] > (ValueDict[LinkList[j][1]] + CostDict[LinkList[j]])):
        ValueDict[LinkList[j][0]] = ValueDict[LinkList[j][1]] + CostDict[LinkList[j]]
        PrePath[LinkList[j][0]] = LinkList[j][1]
      elif (ValueDict[LinkList[j][1]] > (ValueDict[LinkList[j][0]] + CostDict[LinkList[j]])):
        ValueDict[LinkList[j][1]] = ValueDict[LinkList[j][0]] + CostDict[LinkList[j]]
        PrePath[LinkList[j][1]] = LinkList[j][0]
  print "Path:",
    printpath(Dst)
  pass
#_LinkList = []
#class DiscoveryTopo(object):
#  def __init__(self):
#    def startup():
#      core.openflow.addListeners(self)
#      core.openflow_discovery.addListeners(self)
#    core.call_when_ready(startup,('openflow','openflow_discovery'))
#  def _handle_LinkEvent(self,event):
#    global FirstBellman
#    global _LinkList,CostDict
#    tmpLink = (event.link.dpid1,event.link.dpid2) if(event.link.dpid1 < event.link.dpid2) else (event.link.dpid2,event.link.dpid1)
#    if (tmpLink not in _LinkList):# and (event.added == True):
#      _LinkList.append(tmpLink)
#      if TimeCostDict.has_key(tmpLink):
#        CostDict[tmpLink] = TimeCostDict[tmpLink]
#      else:
#        CostDict[tmpLink] = 300
#    if (len(_LinkList) == 445) and FirstBellman:
#      FirstBellman = False
#      print "LinkList len: %d" %len(_LinkList)
#      Bellman()
class DistanceVectorController(object):
  def __init__(self,connection):
    self.connection = connection
    connection.addListeners(self)
  def _handle_ConnectionUp(self,event):
    global DpidList
    global FirstBellman
    DpidList.append(event.connection.dpid)
    if (len(DpidList) == 373) and FirstBellman:
      FirstBellman = False
      Bellman()
#    if event.connection.dpid >= 1000:
#      del DpidList[DpidList.index( event.connection.dpid)]
#  def _handle_ConnectionDown(self,event):
#    global DpidList
#    del DpidList[DpidList.index(event.connection.dpid)]
#    global DpidList
#    del DpidList[DpidList.index(event.connection.dpid)]
  def _handle_PacketIn(self,event):
#    global buffer_id_1st,TmpDpidDict,PassedDpidList
#    global LinkList,CostDict,CostDictHop
#    global loc,old_loc,mac_map
#    global Src,Dst,CallCounter
#    global TimeDpidDict
#    global Src,Dst,Src_Mac,Dst_Mac
    global FirstEnter,FirstBellman
    packet = event.parsed
    packet_in = event.ofp
#    if FirstBellman:
#      FirstBellman = False
#      Bellman()
#    print "Packet_In"
#    if FirstEnter:
#      FirstEnter = False
#      Src_Mac = packet.src
#      Dst_Mac = packet.dst
#      print "Src_Mac: ",
#      print Src_Mac
#      print "Dst_Mac: ",
#      print Dst_Mac
#    if buffer_id_1st == 0:
#      buffer_id_1st = packet_in.buffer_id
#      time_1st = datetime.datetime.now()
#      TimeDpidDict[event.connection.dpid] = time_1st
#      PassedDpidList.append(event.dpid)
#    elif packet_in.buffer_id == buffer_id_1st:
#      def DpidListInLinkList(dpid,linklist):
#        ResultDpidList = []
#        for i in range(len(linklist)):
#          if dpid == linklist[i][0]:
#            ResultDpidList.append(linklist[i][1])
#          elif dpid == linklist[i][1]:
#            ResultDpidList.append(linklist[i][0])
#        return ResultDpidList
#      def IndexByDpidInLinkList(dpid1,dpid2,linklist):
#        for i in range(len(linklist)):
#          if (dpid1 == linklist[i][0]) or (dpid1 == linklist[i][1]):
#            if (dpid2 == linklist[i][0]) or (dpid2 == linklist[i][1]):
#              return i
#      if not (event.dpid in PassedDpidList):
#        PassedDpidList.append(event.dpid)
#        TimeDpidDict[event.dpid] = datetime.datetime.now()
#      tmpDpidList = DpidListInLinkList(event.dpid,LinkList)
#      for i in range(len(tmpDpidList)):
#        if TimeDpidDict.has_key(tmpDpidList[i]):
#          passedTime = TimeDpidDict[event.dpid] - TimeDpidDict[tmpDpidList[i]]
#          CostTime = (passedTime.microseconds + 500)/1000
#          k = IndexByDpidInLinkList(tmpDpidList[i],event.dpid,LinkList)
#          dpid_1 = LinkList[k][0]
#          dpid_2 = LinkList[k][1]
#          tmpDpid = (dpid_1 if dpid_1 <= dpid_2 else dpid_2)
#          dpid_2 = (dpid_1 if dpid_1 > dpid_2 else dpid_2)
#          dpid_1 = tmpDpid
#          CostDict[dpid_1,dpid_2] = CostTime
#          CostDictHop[dpid_1,dpid_2] = 1

#    loc = event.dpid
#    if packet.src in mac_map:
#      old_loc = mac_map[packet.src]
#    else:
#      old_loc = None
#    if old_loc == None:
#      mac_map[packet.src] = loc
#    elif old_loc != None and old_loc != loc:
#      mac_map[packet.src] = loc
#    loc = event.dpid
#    if not (packet.src in mac_map):
#      mac_map[packet.src] = loc
#      print mac_map

#    if len(PassedDpidList) == len(DpidList):
#      if CallCounter == 0:
#        CallCounter = 1
#    MacList = mac_map.keys()
#        print MacList
#        for i in range(len(MacList)):
#          for j in range(i+1,len(MacList)):
#            print "MacList",
#            print MacList
#            print "Mac_Map",
#            print mac_map
#            print "Cost"
#            print CostDict
#    if (len(MacList) == 2) and FirstBellman:
#      FirstBellman = False
#      print "Bellman"
#      Src = mac_map[MacList[0]]
#      Dst = mac_map[MacList[1]]
#      print "Src: %s"%(StationNameList[Src]),
#      print "Dst: %s"%(StationNameList[Dst])
#      Bellman()
#            Bellman()
#    else:
#      msg = of.ofp_packet_out()
#    msg.buffer_id = packet_in.buffer_id
#      msg.in_port = packet_in.in_port
#      msg.data = event.ofp
#      action = of.ofp_action_output(port = of.OFPP_FLOOD)
#      msg.actions.append(action)
#      self.connection.send(msg)
  def _handle_portstats_received(event):
    pass
def launch():
  def start_switch(event):
    log.debug("Controlling %s" %(event.connection,))
    DistanceVectorController(event.connection)
  core.openflow.addListenerByName("ConnectionUp",start_switch)
#  core.registerNew(DiscoveryTopo)
