# Sample Input

# 4
# 101
# Sales.pptx
# 10/02/2020, Rajesh, 5MB
# 102
# Report.pptx
# Rohit, 2MB, 12/12/2019
# 103
# Design Document.docx
# 4038KB, 01/01/2020, Vijay
# 104
# Test_Approach.docx
# 385KB, Sujay, 28/03/2020
# docx


class Document:
    def __init__(self,docId,docName,docDetails):
        self.docId = docId
        self.docName = docName
        self.docDetails = docDetails

class DocumentArchive:
    def __init__(self,archiveId,documentList):
        self.archiveId = archiveId
        self.documentList = documentList
    
    def findDateFromDocumentDetails(self):
        doclis = []
        for doc in self.documentList:
            check = doc.docDetails.count('/') == 2
            x = list(doc.docDetails.strip().split(','))
            for a in x:
                if check and '/' in a:
                    doclis.append((doc.docId,a))
        return doclis
    
    def countDocumentsOfGivenType(self,docType):
        c = 0
        for doc in self.documentList:
            docT = doc.docName.strip().split('.')[1]  
            if docT == docType:
                c += 1
        return c
            

if __name__ == '__main__':
    n = int(input())
    docList = []
    for _ in range(n):
        docList.append(Document(int(input()),input(),input()))
    da = DocumentArchive(1,docList)
    docType = input()
    print('-------------output---------------')
    id_dates = da.findDateFromDocumentDetails()
    if len(id_dates) > 0 :
        for id_date in id_dates:
            print(f'{id_date[0]} {id_date[1]}')
    count = da.countDocumentsOfGivenType(docType)
    print(f'Document Count = {count}')