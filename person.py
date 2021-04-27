insensitive = lambda inp:inp.lower()

class Person:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height 
        self.weight = weight
        self.bmi = 0
        self.bmi_status = ""  
    def calculateBmi(self):
        self.bmi = round(self.weight/(self.height*self.height))
        
class Society:
    def __init__(self,bmi_status,person_list):
        self.bmi_status = bmi_status
        self.person_list = person_list
    def getStatus(self,bmi):
        for status,bmi_limit in self.bmi_status.items():
            low , high = sorted(bmi_limit)
            if low<=bmi and bmi<=high:
                return status
        return ""    
    def calculateBmiAndStatusByName(self,name):
        updatePersons = []
        anyUpdate = 0
        for person in self.person_list:
            if person.name == name:
                person.calculateBmi()
                person.bmi_status = self.getStatus(person.bmi)
                updatePersons.append(person)
                anyUpdate = 1
        if anyUpdate:
            return True , updatePersons
        return False
    def removeInvalidPersons(self,checkbmi):
        filterPersons = []
        for person in self.person_list:
            person.calculateBmi()
            if person.bmi < checkbmi:
                filterPersons.append(person)
        return filterPersons
 
if __name__ == '__main__':
    nperson = int(input())
    personList = [Person(insensitive(input()),int(input()),int(input())) for _ in range(nperson)]
    nbmis = int(input())
    dictbmiStatus = {}
    for _ in range(nbmis):
        key = input()
        value1 = int(input())
        value2 = int(input())
        dictbmiStatus[key] = (value1,value2)
    socitey = Society(dictbmiStatus,personList)
    check , updatePersons = socitey.calculateBmiAndStatusByName(insensitive(input()))
    filterPersons = socitey.removeInvalidPersons(int(input()))
    print()
    for per in updatePersons:
        print(f'{per.bmi} {per.bmi_status}')
    if not check :
        print("No Person Exists")
    for person in filterPersons:
        print(f'{person.name} {person.bmi}')    
    
                        
# Sample Input
# 5
# Rajesh
# 5
# 50
# Suman
# 4
# 89
# Gopi
# 5
# 99
# Radhika
# 6
# 120
# Rajesh
# 5
# 120
# 4
# Normal
# 2
# 3
# Over Weight
# 4
# 6
# under weight
# 0
# 1
# Abnormal
# 7
# 10
# Rajesh
# 5