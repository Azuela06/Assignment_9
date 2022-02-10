import json
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image('pktyur ko.png', 10, 8, 25)
        self.ln(20)

pdf = FPDF()

pdf.add_page()

pdf.set_font('Times','B', size=20)

with open('resume.json', 'r') as f:
    mydata = json.loads(f.read())


pdf.cell(200, 10, txt= mydata['basic info'][0]['Fullname'], ln= 1) #this is for the name of the interviewee which is me

#the following texts are my contact details
pdf.set_font('Times','BU', size=16)
pdf.cell(0,5, txt= mydata['basic info'][0]['Email'], ln=1)
pdf.set_font('Times','B', size=12)
pdf.cell(0,9, txt= mydata['basic info'][0]['Contact.no'], ln=1)
pdf.cell(0,3, txt= mydata['basic info'][0]['Address'], ln=1)


pdf.output("AZUELA, JULLIANE MAEVE.pdf")
