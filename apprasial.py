class Apparel:
    def __init__(self,apparelbrand,type,price,inStock):
        self.apparelbrand = apparelbrand
        self.type = type
        self.price = price
        self.inStock = inStock
        
class Store:
    def __init__(self,apparelList):
        self.apparelList = apparelList
    def display_available(self,brand,type):
        for apparel in self.apparelList:
            if apparel.apparelbrand == brand and apparel.type == type:
                for k,v in apparel.inStock.items():
                    print(f'{k}:{v}')
    def checkApparelAvailability(self,brand,type,size,count):
        for apparel in self.apparelList:
            if(apparel.apparelbrand == brand and apparel.type == type):
                for apparelSize,avail in apparel.inStock.items():
                    if(apparelSize == size):
                        if(avail>=count):
                            apparel.inStock[apparelSize] -= count
                            return 1
                        else:
                            return 0
        return -1
            
                    
if __name__ == '__main__':
    apparelList = []
    numberOfApparel = int(input())
    for _ in range(numberOfApparel):
        brand = input()
        type = input()
        price = int(input())
        inStock = {}
        countStock = int(input())
        for i in range(countStock):
            size = input()
            avail = int(input())
            inStock[size] = avail
        apparelList.append(Apparel(brand,type,price,inStock))
    checkBrand = input()
    checkType = input()
    checkSize = input()
    checkAvail = int(input())
    store = Store(apparelList)
    checkApprael = store.checkApparelAvailability(checkBrand,checkType,checkSize,checkAvail)
    if(checkApprael==1):
        print('Size is Available') 
        store.display_available(checkBrand,checkType)
    elif(checkApprael == 0): 
        print('Size is not available')
        store.display_available(checkBrand,checkType)
    else:
        print('Size not Available')
        print('Apparel not found')
    