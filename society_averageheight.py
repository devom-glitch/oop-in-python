class Person:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight

class Society:
    def __init__(self,persons):
        self.persons = persons
    def findAverageHeight(self):
        avg = 0
        for per in self.persons:
            avg += per.height
        avg /= len(self.persons)
        return avg
    def findTallerThanAveragePerson(self):
        societyavg = self.findAverageHeight()
        name = ''
        for per in self.persons:
            if(per.height > societyavg):
                name = per.name
        return name

if __name__ == '__main__':
    n = int(input())
    persons = []
    for _ in range(n):
        persons.append
        