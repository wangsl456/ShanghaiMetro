#calss Line
class Line:
    def __init__(self,LineNum):
        self.LineNum = LineNum
    def out(self):
        print 'Line %d' %self.LineNum
LineList = []
for i in range(1,14):
    tmpLine = Line(i)
    LineList.append(tmpLine)
LineList.append(Line(16))
Line1 = LineList[0]
Line2 = LineList[1]
Line3 = LineList[2]
Line4 = LineList[3]
Line5 = LineList[4]
Line6 = LineList[5]
Line7 = LineList[6]
Line8 = LineList[7]
Line9 = LineList[8]
Line10 = LineList[9]
Line11 = LineList[10]
Line12 = LineList[11]
Line13 = LineList[12]
Line16 = LineList[13]
if __name__ == "__main__":
    for i in range(1,15):
        LineList[i - 1].out()
