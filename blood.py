class Blood:
    def __init__(self,bloodgroup,unitInHand):
        self.bloodgroup = bloodgroup
        self.unitInHand = unitInHand
    
class BloodBank:
    def __init__(self,bloods):
        self.bloods = bloods
    
    def isBloodAvailable(self,bloodgroup,unitreq):
        for blood in self.bloods:
            if blood.bloodgroup.lower() == bloodgroup.lower() and blood.unitInHand >= unitreq:
                return True
        return False
    
    def findMinBloodStock(self):
        runningshort = []
        mini = min(self.bloods,key = lambda blood:blood.unitInHand)
        for blood in self.bloods:
            if mini.unitInHand == blood.unitInHand:
                runningshort.append(blood)
        return runningshort
        


if __name__ == "__main__":
    n = int(input())
    bloods = []
    for _ in range(n):
        bloods.append(Blood(input(),int(input())))
    bloodbank = BloodBank(bloods)
    bloodgroup = input()
    low = int(input())
    if bloodbank.isBloodAvailable(bloodgroup,low):
        print("Blood Available")
    else:
        print("Blood not Available")
    for bg in bloodbank.findMinBloodStock():
        print(bg.bloodgroup)
    