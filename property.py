insensitive = lambda inp:inp.lower()

class Property:
    # assume max_bid > property_value
    def __init__(self,type,value,max_bid):
        self.type = type
        self.value = value
        self.max_bid = max_bid

class Tender:
    def __init__(self,buyer,ptype,bidPrice):
        self.buyer = buyer
        self.ptype = ptype
        self.bidPrice = bidPrice
        

def bidProperty(properties,tenders):
    a = []
    buyers = []
    for pro in properties:
        buyer = ""
        for tender in tenders:
            if tender.ptype == pro.type and pro.value < tender.bidPrice and tender.bidPrice <= pro.max_bid:
                pro.value = tender.bidPrice
                buyer = tender.buyer
        if buyer:
            buyers.append(buyer)
            a.append(pro)
    for i in a:
        properties.remove(i)
    return buyers,properties
    

if __name__ == '__main__':
    countpro = int(input())
    properties = []
    for _ in range(countpro):
        properties.append(Property(insensitive(input()),int(input()),int(input())))
    countten = int(input())
    tenders = []
    for _ in range(countten):
        tenders.append(Tender(input(),insensitive(input()),int(input())))
    x,y = bidProperty(properties,tenders)
    if x:
        for i in x:
            print(i)
    else:
        print("Property Not Found")
    for a in y:
        print(a.type)
        
        
            
                
                
    
        
    