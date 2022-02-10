
import json
from textwrap import indent
from fpdf import FPDF

        
pdf = FPDF()

pdf.add_page()
pdf.set_auto_page_break

pdf.set_font('Times','B', size=20)

with open('resume.json', 'r') as f:
    mydata = json.loads(f.read())

pdf.set_text_color(122,86,42)
pdf.cell(200, 10, txt= mydata['basic info'][0]['Fullname'], ln= 1) #this is for the name of the interviewee which is me
pdf.image('photo.png', x=160, y=9, w= 32, h= 32, type= '', link= '' )

#the following texts are my contact details
pdf.set_text_color(102,71,34)
pdf.set_font('Times','BU', size=14)
pdf.cell(0,5, txt= mydata['basic info'][0]['Email'], ln=1)
pdf.set_font('Times','B', size=13)
pdf.cell(0,9, txt= mydata['basic info'][0]['Contact.no'], ln=1)
pdf.cell(0,3, txt= mydata['basic info'][0]['Address'], ln=1)
pdf.line(x1=200,x2=12, y1= 47, y2= 47)

#The next lines are the 'skills' I possess
pdf.set_font('Courier', 'B', size=17)
pdf.cell(0,26, txt= 'Skills', border=0, ln=2, align= 'C')

pdf.set_font('Courier', 'I', size=14)
pdf.cell(0,5, txt= 'Soft Skills', ln=1)

#The following are the soft skills 
pdf.set_font('Times', '', size=12)
pdf.set_text_color(0,0,0)
pdf.cell(40,8, txt= mydata['Skills'][0]['Soft Skill1'], ln=1, align= 'R')
pdf.cell(150,-8, txt= mydata['Skills'][0]['Soft Skill2'], ln= 0, align= 'R')
pdf.cell(-102,3, txt= mydata['Skills'][0]['Soft Skill3'], ln=1, align= 'R')
pdf.cell(148,-3, txt= mydata['Skills'][0]['Soft Skill4'], ln=0, align= 'R')

#hard skills na pi
pdf.set_text_color(102,71,34)
pdf.set_font('Courier', 'I', size=14)
pdf.cell(0,8, txt= 'Hard Skills', ln=2)


pdf.output("AZUELA, JULLIANE MAEVE.pdf")
