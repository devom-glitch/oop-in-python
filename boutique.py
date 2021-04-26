class Boutique:
    def __init__(self,bid,bname,btype,brating,points):
        self.bid = bid
        self.bname = bname
        self.btype = btype
        self.brating = brating
        self.points = points

class OnlineBoutique:
    def __init__(self,bDict):
        self.bDict = bDict
    def getBoutique(self,low,up,extrapoints,type):
        blist = []
        if self.bDict.get(type,0):
            for boutique in self.bDict[type]:
                if low <= boutique.brating and boutique.brating <= up:
                    boutique.points += extrapoints
                blist.append(boutique)
            blist.sort(key=lambda x:x.points,reverse=True)
            return blist
        return None
    
if __name__ == '__main__' :
    bDict = {}
    c = int(input())
    for _ in range(c):
        tempB = Boutique(int(input()),input(),input(),float(input()),int(input()))
        if bDict.get(tempB.btype,0):
            bDict[tempB.btype].append(tempB)
        else:
            bDict[tempB.btype] = [tempB]
    onlineB = OnlineBoutique(bDict)
    blist = onlineB.getBoutique(float(input()),float(input()),int(input()),input())
    for boutique in blist:
        print(f'{boutique.bid} {boutique.bname} {boutique.points}')
    
                
        