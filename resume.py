import docx2txt
import re
class RequiredData:
    def __init__(self,filename):
        self.doc = docx2txt.process(filename)
        print(self.doc)
    def getdata(self):
        try:
            mobile=re.findall(r'\b\d{10}\b ',self.doc)
            email = re.findall(r'\S+@\S+',self.doc)
            return (mobile,email)
        except:
            return 'exception'

    def getdata1(self):
        try:
            skills = {'Quick learner','Positive attitude','Good communication  skills','Hard work','Work Smart'}
            document=set(self.doc)
            reqired_skills=re.findall(r'%s' % '|'.join(skills),self.doc, re.IGNORECASE)
            return reqired_skills
        except:
            return 'exception'

    def getdata2(self):
        try:
           education = {'B.tech','M.tech','Bachelor of Science','Bachelor of Arts','Bachelor of commerce','Bachelor of Communication'}
           document=set(self.doc)
           reqired_education=re.findall(r'%s' % '|'.join(education),self.doc, re.IGNORECASE)
           return reqired_education
        except:
           return 'exception'
    def getdata3(self):
        try:
            document = set(self.doc)
            reqired_names = re.compile(r'([A-Z][a-z]+(?: [A-Z][a-z]\.)? [A-Z][a-z]+)')
            print(reqired_names.findall(document))
            return reqired_names
        except:
            return 'exception'


obj = RequiredData('a1.docx')
print(obj.getdata())
print(obj.getdata1())
print(obj.getdata2())
print(obj.getdata3())
