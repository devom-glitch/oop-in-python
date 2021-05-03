class Employee:
    def __init__(self,employee_name,designation,salary,leaveBalance):
        self.employee_name = employee_name #String
        self.designation = designation #String
        self.salary = salary #Number
        self.leaveBalance = leaveBalance # leavetype:leaveBalance >> leaveType UpperCase
    
class Organization:
    def __init__(self,employees):
        self.employees = employees # List Of Employees
    
    def cheackLeaveEligibility(self,empName,leaveType,leaveDays):
        for emp in self.employees:
            if emp.employee_name == empName and leaveType.upper() in emp.leaveBalance.keys() and emp.leaveBalance[leaveType.upper()]>=leaveDays:
                emp.leaveBalance[leaveType.upper()] -= leaveDays
                return True
        return False

if __name__ == '__main__':
    nemp = int(input())
    emps = []
    for _ in range(nemp):
        name = input()
        designation = input()
        salary = int(input())
        leaveBalance = {}
        countleave = int(input())
        for _ in range(countleave):
            ltype = input()
            btype = int(input())
            leaveBalance[ltype] = btype
        emps.append(Employee(name,designation,salary,leaveBalance))
    org = Organization(emps)
    queryname = input()
    querytype = input()
    querydays = int(input())
    check = org.cheackLeaveEligibility(queryname,querytype,querydays)
    print(check)
    if check == True:
        print('leave granted.')
        for e in emps:
            if e.employee_name == queryname:
                for typ,lev in e.leaveBalance.items():
                    print(f'{typ} : {lev}')

# Sample input
# 5
# Sunita
# Faculty
# 23000
# 2
# CL
# 2
# SL
# 3
# Arun
# Admin
# 30000
# 3
# CL
# 4
# EL
# 12
# SL
# 10
# Dipak
# Admin
# 25000
# 3
# CL
# 2
# EL
# 5
# SL
# 3
# Balen
# HR
# 12000
# 3
# CL
# 2
# EL
# 5
# SL
# 3
# Tarun
# HR
# 78000
# 3
# CL
# 8
# EL
# 12
# SL
# 10
# Arun
# sl
# 8