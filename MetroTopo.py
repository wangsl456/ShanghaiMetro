from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.topo import Topo
from mininet.node import CPULimitedHost
from mininet.node import Controller
from functools import partial
from MetroStation import StationList,StationNameList
from MetroLine import *
LinkNum = 0
LinkList = []
class MetroTopo(Topo):
  def __init__(self):
    global LinkNum
    Topo.__init__(self)
    self.s = []
    for i in range(len(StationList)):
      SwitchName = 's' + str(i)
      self.s.append(self.addSwitch(SwitchName))
    old_line = 0
    def FindStation(stationname,stationnamelist):
      return [a for a in range(len(stationnamelist)) if stationname == stationnamelist[a]]
    for j in range(len(StationList)):
      if StationList[j].Line == old_line:
        if StationNameList[j] == 'HongQiaoLu':
          tmpindex = StationNameList.index('YiShanLu')
          self.addLink(self.s[j],self.s[tmpindex],bw = 1000,delay = '120ms',loss = 0,max_queue_size = 100,use_htb = True)
          LinkNum = LinkNum + 1
          tmpLink = (j,tmpindex) if j < tmpindex else (tmpindex,j)
          LinkList.append(tmpLink)
        if StationNameList[j] == 'LongBaiXinCun':
          tmpindex1 = StationNameList.index('LongXiLu')
          tmpindex2 = StationNameList.index('ShangHaiDongWuYuan')
          self.addLink(self.s[j],self.s[tmpindex1],bw = 1000,delay = '120ms',loss = 0,max_queue_size = 100,use_htb = True)
          tmpLink = (j,tmpindex1) if j < tmpindex1 else (tmpindex1,j)
          LinkList.append(tmpLink)
          self.addLink(self.s[j],self.s[tmpindex2],bw = 1000,delay = '120ms',loss = 0,max_queue_size = 100,use_htb = True)
          LinkNum = LinkNum + 2
          tmpLink = (j,tmpindex2) if j < tmpindex2 else (tmpindex2,j)
          LinkList.append(tmpLink)
        if StationNameList[j] == 'ShangHaiSaiCheChang':
          tmpindex = StationNameList.index('JiaDingXinCheng')
          self.addLink(self.s[j],self.s[tmpindex],bw = 1000,delay = '120ms',loss = 0,max_queue_size = 100,use_htb = True)
          LinkNum = LinkNum + 1
          tmpLink = (j,tmpindex) if j < tmpindex else (tmpindex,j)
          LinkList.append(tmpLink)
        else:
          self.addLink(self.s[j],self.s[j - 1],bw = 1000,delay = '120ms',loss = 0,max_queue_size = 100,use_htb = True)
          LinkNum = LinkNum + 1
          LinkList.append((j-1,j))
      if StationList[j].Line != old_line:
        old_line = StationList[j].Line
      tmpindexlist = []
      tmpindexlist = FindStation(StationList[j].StationName,StationNameList[:j])
      for k in range(len(tmpindexlist)):
        self.addLink(self.s[j],self.s[tmpindexlist[k]],bw = 1000,delay = '300ms',loss = 0,max_queue_size = 100,use_htb = True)
        LinkNum = LinkNum + 1
#        tmpLink = (j,tmpindexlist[k]) if j < tmpindexlist[k] else (tmpindexlist[k],j)
#        LinkList.append(tmpLink)
#  def AddHost1(self,index):
#    h1 = self.addHost('h1')
#    self.addLink(h1,self.s[index],bw = 1000,delay = '10ms',loss = 0,max_queue_size = 100,use_htb = True)
#  def AddHost2(self,index):
#    h2= self.addHost('h2')
#    self.addLink(h2,self.s[index],bw = 1000,delay = '10ms',loss = 0,max_queue_size = 100,use_htb = True)
def run():
#  global LinkNum
  topo = MetroTopo()
#  topo.AddHost1(0)
#  topo.AddHost2(1)
#  tmpindex = None
#  print "Input station you start: ",
#  while True:
#    start = raw_input()
#    if start in StationNameList:
#      tmpindex = StationNameList.index(start)
#      print tmpindex
#      topo.AddHost1(tmpindex)
#      break
#    else:
#      print "Please enter a correct station name"
#  print "Input station name you want to go: ",
#  while True:
#    end = raw_input()
#    if end in StationNameList:
#      tmpindex = StationNameList.index(end)
#      print tmpindex
#      topo.AddHost2(tmpindex)
#      break
#    else:
#      print "Please enter a correct station name"
  net = Mininet(topo = topo,host = CPULimitedHost,link = TCLink,controller = partial(RemoteController,ip = '127.0.0.1',port = 6633))
  net.start()
  print "LinkNum: %d" %LinkNum
  CLI(net)
  net.stop()
if __name__ == '__main__':
  run()
