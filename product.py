class Product:
    def __init__(self,productName,productType,productPrice,quantityOnHand,reorderingQuantity):
        self.productName = productName
        self.productType = productType
        self.productPrice = productPrice
        self.quantityOnHand = quantityOnHand
        self.reorderingQuantity = reorderingQuantity
        

def findAvailableStock(products,productsname):
    map = {}
    for pro in products:
        if pro.productName.lower() in productsname:
            map[pro.productName] = pro.quantityOnHand
    if(len(map)>0):
        return map
    return None

def updateStockByProductType(products,quantity,type):
    flag = 0
    for pro in products:
        if pro.productType == type and pro.quantityOnHand <= pro.reorderingQuantity:
            pro.quantityOnHand += quantity
            flag = 1
    if flag:
        return products
    return None


if __name__ == '__main__':
    proObj = []
    for i in range(5):
        proName = input()
        proType = input()
        proPrice = int(input())
        quantHand = int(input())
        reorderQuant = int(input())
        proObj.append(Product(proName,proType,proPrice,quantHand,reorderQuant))
    nameCount = int(input())
    proNames = []
    for i in range(nameCount):
        proNames.append(input().lower())
    quant = int(input())
    type = input()
    updateStockByProductType(proObj,quant,type)
    x = findAvailableStock(proObj,proNames)
    if(x):
        for i,j in x.items():
            print(f'{i} {j}')
    
    
            
    
    
    
        