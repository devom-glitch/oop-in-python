class Doctor:
    def __init__(self,doctorId,doctorName,deptName,consultFee,sunAvail):
        self.doctorId = doctorId
        self.doctorName = doctorName
        self.deptName = deptName
        self.consultFee = consultFee
        self.sunAvail = sunAvail
        
class Hospital:
    def __init__(self,doctorList):
        self.doctorList = doctorList
        
    def getDoctorList(self,deptName):
        deptDoctors = []
        for doctor in self.doctorList:
            if doctor.deptName == deptName and doctor.sunAvail == "available":
                deptDoctors.append(doctor)
        if(len(deptDoctors)>0):
            return deptDoctors
        else:
            return None
    
    def selectDoctor(self,fee):
        for doctor in self.doctorList:
            if doctor.sunAvail == 'not available' and doctor.consultFee > fee:
                self.doctorList.remove(doctor)
                return True
        return False
    
if __name__ == '__main__':
    doctorListObj = []
    for _ in range(5):
        doctorIdObj = int(input())
        doctorNameObj = input()
        doctorDeptObj = input()
        doctorCFeeObj = int(input())
        doctorSunAvailObj = input()
        doctorListObj.append(Doctor(doctorIdObj,doctorNameObj,doctorDeptObj,doctorCFeeObj,doctorSunAvailObj))
    hosptialObj = Hospital(doctorListObj)
    deptNameSearch = input()
    docList = hosptialObj.getDoctorList(deptNameSearch)
    docFeeFilter = int(input())
    selectedDoc = hosptialObj.selectDoctor(docFeeFilter)  
    print('---------------------------------------------------')    
    if(len(docList)>0):
        for doc in docList:
            print(doc.doctorId)
            print(doc.doctorName)
    else:
        print('Doctor Not Found')
    if(selectedDoc):
        selectedDocs = hosptialObj.doctorList
        selectedDocs.sort(key=lambda x: x.consultFee)
        for i in selectedDocs:
            print(i.doctorId)
            print(i.doctorName)
            print(i.consultFee)
    else:
        print('Returning the original List')
        for i in hosptialObj.doctorList:
            print(i.doctorId)
            print(i.doctorName)
            
        