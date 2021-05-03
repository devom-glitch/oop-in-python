class Product:
    def __init__(self,productName,productType,unitPrice,qtyOnHand):
        self.productName = productName
        self.productType = productType
        self.unitPrice = unitPrice
        self.qtyOnHand = qtyOnHand
        
class Store:
    def __init__(self,products):
        self.products = products
        
    def purchaseProduct(self,proName,proQty):
        bill = 0
        for product in self.products:
            if product.productName == proName:
                if proQty >= product.qtyOnHand:
                    bill = product.unitPrice * product.qtyOnHand
                    product.qtyOnHand = 0
                else:
                    bill = product.unitPrice * proQty
                    product.qtyOnHand -= proQty
                return bill
        return None
if __name__=="__main__":
    n=int(input())
    ProductList=[]
    for i in range(n):
        name=input()
        type=input()
        price=int(input())
        qty=int(input())
        p=Product(name,type,price,qty)
        ProductList.append(p)
    productRequired=input()
    productQuantity=int(input())
    obj=Store(ProductList)
    x=obj.purchaseProduct(productRequired,productQuantity)
    if x==None:
        print("Product not available")
        for i in obj.products:
            print(i.productName,i.qtyOnHand)
    else:
        print("Product available")
        for i in obj.products:
            print(i.productName,i.qtyOnHand)
            
# Sample Input

# 3
# White board
# stationary
# 200
# 4
# Duster
# stationary
# 20
# 10
# marker
# stationary
# 40
# 0
# marker
# 5