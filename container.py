class Container:
    def __init__(self,id,length,breadth,height,pricepersqft):
        self.id = id
        self.length = length
        self.breadth = breadth
        self.height = height
        self.pricepersqft = pricepersqft
        
    def findVolumne(self):
        return self.length*self.breadth*self.height
    

class PackagingCompany:
    def __init__(self,containers):
        self.contianers = containers
    
    def findContainerCost(self,id):
        cost = 0
        for container in self.contianers:
            if container.id == id:
                cost += container.findVolumne()*container.pricepersqft
                return cost
        return None
    
    def findLargestContainer(self):
        largest = 0
        container_id = None
        for container in self.contianers:
            vol = container.findVolumne()
            if vol > largest:
                largest = vol
                container_id = container.id
        for container in self.contianers:
            if container_id == container.id:
                return container
        return None


if __name__ == "__main__":
    n = int(input())
    containers = []
    for _ in range(n):
        containers.append(Container(int(input()),int(input()),int(input()),int(input()),int(input())))
    packagingCompany = PackagingCompany(containers)
    contianer_id = int(input())
    cost = packagingCompany.findContainerCost(contianer_id)
    if cost:
        print(cost)
    else:
        print("No container found")
    largest = packagingCompany.findLargestContainer()
    largest_id = largest.id
    largest_vol = largest.findVolumne()
    print(f'{largest_id} {largest_vol}')
        