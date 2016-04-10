#class Station
# coding=gbk
import MetroLine
class Station:
    #Initialize metro station
    #One station may lie in many lines
    def __init__(self,StationName,Line):
        self.StationName = StationName
        self.Line = Line.LineNum
    def out(self):
        print '%s station is ' %self.StationName,
        print 'Line ',
        print self.Line,
        print
Line = MetroLine.LineList
_StationName_ = []
_StationName_.append("XinZhuang WaiHuanLu LianHuaLu JinJiangLeYuan ShangHaiNanZhan CaoBaoLu ShangHaiTiYuGuan XuJiaHui HengShanLu ChangShuLu ShanXiNanLu HuangPiNanLu RenMinGuangChang XinZhaLu HanZhongLu ShangHaiHuoCheZhan ZhongShanBeiLu YanChangLu ShangHaiMaXiCheng WenShuiLu PengPuXinCun GongKangLu TongHeXinCun HuLanLu GongFuXinCun BaoAnGongLu YouYiXiLu FuJinLu")
_StationName_.append("PuDongGuoJiJiChang HaiTianSanLu YuanDongDaDao LingKongLu ChuanSha HuaXiaDongLu ChuangXinZhongLu TangZhen GuangLanLu JinKeLu ZhangJiangGaoKe LongYangLu ShiJiGongYuan ShangHaiKeJiGuan ShiJiDaDao DongChangLu LuJiaZui NanJingDongLu RenMinGuangChang NanJingXiLu JingAnSi JiangSuLu ZhongShanGongYuan LouShanGuanLu WeiNingLu BeiXinJin SongHongLu HongQiao2HaoHangZhanLou HongQiaoHuoCheZhan XuJinDong")
_StationName_.append("ShangHaiNanZhan ShiLongLu LongCaoLu CaoXiLu YiShanLu HongQiaoLu YanAnXiLu ZhongShanGongYuan JinShaJiangLu CaoYangLu ZhenPingLu ZhongTanLu ShangHaiHuoCheZhan BaoShanLu DongBaoXingLu HongQiaoZuQiuChang ChiFengLu DaBaiShu JiangWanZhen YinGaoXiLu ChangJiangNanLu SongFaLu ZhangHuaBang SongBinLu ShuiChanLu BaoYangLu YouYiLu TieLiLu JiangYangBeiLu")
_StationName_.append("YiShanLu ShangHaiTiYuGuan ShangHaiTiYuChang DongAnLu DaMuQiaoLu LuBanLu XiZangNanLu NanPuDaQiao TangQiao LanCunLu PuDianLu ShiJiDaDao PuDongDaDao YangShuPuLu DaLianLu LinPingLu HaiLunLu BaoShanLu ShangHaiHuoCheZhan ZhongTanLu ZhenPingLu CaoYangLu JinShaJiangLu ZhongShanGongYuan YanAnXiLu HongQiaLu")
_StationName_.append("XinZhuang ChunShenLu YinDuLu DuanQiao BeiQiao JianChuanLu DongChuanLu JinPingLu HuaNingLu WenJinLu MinHangKaiFaQu")
_StationName_.append("GangChengLu WaiGaoQiaoBaoShuiQuBei HangJinLu WaiGaoQiaoBaoShuiQuNan ZhouHaiLu WuZhouDaDao DongJingLu JuFengLu WuLianLu BoXingLu JinQiaoLu YunShanLu DePingLu BeiYangJinLu MinShengLu YuanShenTiYuZhongXin ShiJiDaDao PuDianLu LanCunLu ShangHaiErTongYiXueZhongXin LinYiXinCun GaoKeXiLu DongMingLu GaoQingLu HuaXiaXiLu ShangNanLu LingYanNanLu DongFangTiYuZhongXin")
_StationName_.append("HuaMuLu LongYangLu FangHuaLu JinXiuLu YangGaoNanLu GaoKeXiLu YunTaiLu YaoHuaLu ChangQingLu HouTan LongHuaZhongLu DongAnLu ZhaoJiaBangLu ChangShuLu JingAnSi ChangPingLu ChangShouLu ZhenPingLu LanGaoLu XinCunLu DaHuaSanLu XingZhiLu DaChangZhen CHangZhongLu ShangDaLu NanChenLu ShangHaiDaXue QiHuaLu GuCunGongYuan LiuHang PanGuangLu LuoNanXinCun MeiLanHu")
_StationName_.append("ShenDuGongLu LianHangLu JiangYueLu PuJiangZhen LuHengLu LingZhaoXinCun DongFangTiYuZhongXin YangSi ChengShanLu YaoHuaLu ZhongHuaYiShuGong XiZangNanLu LuJiaBangLu LaoXiMen DaShiJie RenMinGuangChang QuFuLu ZhongXingLu XiZangBeiLu HongKouZuQiuChang QuYangLu SiPingLu AnShanXinCun JiangPuLu HuangXingLu YanJiZhongLu HuangXingGongYuan XiangYinLu NengJiangLu ShiGUangLu")
_StationName_.append("YangGaoZhongLu ShiJiDaDao ShangChengLu XiaoNanMen LuJiaBangLu MaDangLu DaPuQiao JiaShanLu ZhaoJiaBangLu XuJiaHui YiShanLu GuiLinLu CaoHeJinKaiFaQu HeChuanLu XingZhongLu QiBao ZhongChunLu JiuTing SiJin SheShan DongJin SongJiangDaXueCheng SongJiangXinCheng SongJiangTiYuZhongXin ZuiBaiChi SongJiangNanZhan")
_StationName_.append("XinJiangWanCheng YinGaoDongLu SanMenLu JiangWanTiYuChang WuJiaoChang GuoQuanLu TongJiDaXue SiPingLu YouDianXinCun HaiLunLu SiChuanBeiLu TianTongLu NanJingDongLu YuYuan LaoXiMen XinTianDi ShanXiNanLu ShangHaiTuShuGuan JiaoTongDaXue HongQiaoLu SongYuanLu YiLiLu ShuiChengLu LongXiLu ShangHaiDongWuYuan HongQiao1HaoHangZhanLou HongQiao2HaoHangZhanLou HongQiaoHuoCheZhan LongBaiXinCUn ZiTengLu HangZhongLu")
_StationName_.append("KangXinGongLu XiuYanLu LuoShanLu YuQiao PuSanLu SanLinDong SanLin DongFangTiYuZhongXin LongYaoLu YunJinLu LongHua ShangHaiYouYongGuan XuJiaHui JiaoTongDaXue JiangSuLu LongDeLu CaoYangLu FengQiaoLu ZhenRu ShangHaiXiZhan LiZiYuan QiLianShanLu WuWeiLu TaoPuXinCun NanXiang MaLu JiaDingXinCheng BaiYinLu JiaDingXi JiaDingBei ShangHaiSaiCheChang ChangJiDongLu ShangHaiQiCheCheng AnTing ZhaoFengLu GuangMingLu HuaQiao")
_StationName_.append("JinHaiLu ShenJiangLu JinJingLu YangGaoBeiLu JuFengLu DongLuLu FuXingDao AiGuoLu LongChangLu NingGuoLu JiangPuGongYuan DaLianLu TiLanQiao GuoJiKeYunZhongXing TianTongLu QuFuLu HanZhongLu NanJingXiLu ShanXiNanLu JiaShanLu DaMuQiaoLu LongHuaZhongLu LongHua LongCaoLu CaoBaoLu GuiLinGongYuan HongCaoLu HongMeiLu DongLanLu GuDaiLu HongXinLu QiXinLu")
_StationName_.append("JinYunLu JinShaJiangXiLu FengZhuang QiLianShanNanLu ZhenBeiLu DaDuHeLu JinShaJiangLu LongDeLu WuNingLu ChangShouLu JiangNingLu HanZhongLu ZiRanBoWuGuan NanJingXiLu HuaiHaiZhongLu XinTianDi MaDangLu ShiBoHuiBoWuGuan ShiBoDaDao")
_StationName_.append("DiShuiHu LinGangDaDao ShuYuan HuiNanDong HuiNan YeShengDongWuYuan XinChang HangTouDong HeShaHangCheng ZhouPuDong LuoShanLu HuaXiaZhongLu LongYangLu")
TimeCost = []
SplitStr = ' '
TimeCost.append([120, 120, 180, 180, 180, 180, 120, 120, 120, 120, 120, 180, 120, 120, 180, 120, 180, 120, 120, 180, 180, 120, 120, 180, 180, 120, 120])
if len(TimeCost[0]) != (len(_StationName_[0].split(SplitStr))-1):
  print "Error1"
TimeCost.append([180, 420, 300, 180, 300, 180, 180, 300, 180, 120, 240, 60, 180, 180, 120, 120, 180, 180, 120, 120, 180, 180, 120, 180, 120, 180, 420, 120, 120])
if len(TimeCost[1]) != (len(_StationName_[1].split(SplitStr))-1):
  print "Error2"
TimeCost.append([120, 120, 120, 180, 120, 120, 120, 180, 120, 120, 180, 120, 240, 120, 120, 180, 120, 120, 180, 180, 180, 120, 120, 120, 180, 120, 180, 120])
if len(TimeCost[2]) != (len(_StationName_[2].split(SplitStr))-1):
  print "Error3"
TimeCost.append([120, 120, 120, 60, 120, 180, 120, 180, 120, 120, 120, 180, 120, 120, 120, 120, 180, 180, 180, 120, 180, 60, 180, 120, 120, 120])
if len(TimeCost[3]) != len(_StationName_[3].split(SplitStr)):
  print "Error4"
TimeCost.append([180, 120, 180, 240, 180, 120, 120, 180, 120, 120])
if len(TimeCost[4]) != (len(_StationName_[4].split(SplitStr))-1):
  print "Error5"
TimeCost.append([180, 120, 180, 180, 120, 120, 180, 120, 120, 120, 180, 120, 180, 120, 120, 120, 180, 120, 180, 180, 120, 180, 120, 180, 120, 120, 120])
if len(TimeCost[5]) != (len(_StationName_[5].split(SplitStr))-1):
  print "Error6"
TimeCost.append([180, 120, 180, 120, 180, 120, 120, 120, 120, 180, 120, 120, 180, 120, 180, 120, 120, 180, 120, 120, 120, 120, 180, 120, 120, 180, 180, 180, 180, 120, 240, 120])
if len(TimeCost[6]) != (len(_StationName_[6].split(SplitStr))-1):
  print "Error7"
TimeCost.append([120, 120, 120, 240, 180, 180, 180, 120, 120, 120, 120, 180, 120, 120, 60, 180, 120, 120, 180, 120, 120, 120, 120, 120, 180, 120, 120, 120, 60])
if len(TimeCost[7]) != (len(_StationName_[7].split(SplitStr))-1):
  print "Error8"
TimeCost.append([180, 120, 240, 180, 120, 120, 120, 180, 120, 180, 240, 180, 180, 180, 180, 120, 240, 420, 240, 180, 300, 180, 180, 180, 240])
if len(TimeCost[8]) != (len(_StationName_[8].split(SplitStr))-1):
  print "Error9"
TimeCost.append([120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 180, 120, 120, 180, 120, 120, 120, 120, 120, 180, 120, 180, 180, 60, 240, 120, 120])
if len(TimeCost[9]) != (len(_StationName_[9].split(SplitStr))-1):
  print "Error10"
TimeCost.append([180, 180, 180, 300, 180, 120, 300, 180, 120, 120, 180, 180, 180, 180, 180, 120, 120, 120, 180, 120, 180, 120, 120, 240, 360, 180, 180, 240, 120, 240, 360, 180, 120, 120, 180, 120])
if len(TimeCost[10]) != (len(_StationName_[10].split(SplitStr))-1):
  print "Error11"
TimeCost.append([240, 120, 120, 180, 120, 180, 120, 120, 180, 120, 120, 120, 180, 180, 120, 180, 180, 120, 180, 120, 180, 180, 120, 180, 120, 120, 120, 180, 120, 180, 120])
if len(TimeCost[11]) != (len(_StationName_[11].split(SplitStr))-1):
  print "Error12"
TimeCost.append([180, 180, 120, 180, 180, 180, 180, 120, 120, 120, 180, 120, 120, 180, 180, 60, 180, 180])
if len(TimeCost[12]) != (len(_StationName_[12].split(SplitStr))-1):
  print "Error13"
TimeCost.append([180, 360, 660, 300, 480, 420, 360, 240, 360, 420, 240, 300])
if len(TimeCost[13]) != (len(_StationName_[13].split(SplitStr))-1):
  print "Error16"
#TimeCost.append()
def Change(y):
  return [60*y[a] for a in range(len(y))]
TimeCostDict = {}
k = 0
for i in range(len(TimeCost)):
  tmp = Change(TimeCost[i])
  for j in range(len(TimeCost[i])):
    TimeCostDict[j+k,j+k+1]=TimeCost[i][j]
  k = k + len(TimeCost[i])
TransferTime = 0
for i in range(len(TimeCost)):
  for j in range(len(TimeCost[i])):
    TransferTime = TransferTime + TimeCost[i][j]
#print TimeCostDict
#TimeCostList = []
#for i in range(len(TimeCost)):
#  TimeCostList[len(TimeCostList):len(TimeCostList)] = TimeCost[i]
StationList = []
StationListStr = []
StationNameList = []
for i in range(0,14):
    tmpList = _StationName_[i].split(SplitStr)
    tmpLen = len(tmpList)
    for j in range(0,tmpLen):
        StationList.append(Station(tmpList[j],MetroLine.LineList[i]))
        StationNameList.append(tmpList[j])
#if __name__ == "MetroStation":
if __name__ == '__main__':
#    for i in range(0,len(StationList)):
#        StationList[i].out()
#        print "Index: ",
#        print i
