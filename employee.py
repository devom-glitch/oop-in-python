class Employee:
    def __init__(self,eid,ename,dept,sal,role):
        self.eid = eid
        self.ename = ename
        self.dept = dept
        self.sal = sal
        self.role = role
        
    def calculateIncentive(self,roleIncentivePercentage):
        if roleIncentivePercentage.get(self.role.lower(),0):
            incentive = self.sal*(roleIncentivePercentage[self.role.lower()]/100)
            return incentive
        return 0
    
def calculateEmployeeSalaryByRole(role,employees,dictRP):
    x = []
    for emp in employees:
        if emp.role == role:
            emp.sal += emp.calculateIncentive(dictRP)
            x.append(emp)
    return x

if __name__ == '__main__':
    nroles = int(input())
    dictRP = {}
    emps = []
    for _ in range(nroles):
        role = input()
        percentage = int(input())
        dictRP[role] = percentage
    n1 = int(input())
    for i in range(n1):
        obj = Employee(int(input()),input(),input(),int(input()),input())
        emps.append(obj)
    role = input()
    x = calculateEmployeeSalaryByRole(role,emps,dictRP)
    for i in x:
        print(f'{i.eid} {i.ename} {i.sal}')