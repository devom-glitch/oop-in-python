class Document:
    def __init__(self,docId,docName,docDetails):
        self.docId = docId
        self.docName = docName
        self.docDetails = docDetails

class DocumentArchive:
    def __init__(self,archiveId,documentList):
        self.atchiveId = archiveId
        self.documentList = documentList
    
    def findDateFromDocumentDetails(self):
        doclis = []
        for doc in self.documentList:
            x = list(doc.docDetails.strip().split(','))
            for a in x:
                if '/' in a:
                    doclis.append((doc.docId,a))
        return doclis
        