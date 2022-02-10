
import json
from re import A
from tkinter import font
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
pdf.cell(-114,8, txt= 'Hard Skills', ln=2, align= 'R')

#The following data are not true lol
pdf.set_font('Times', '', size= 12)
pdf.set_text_color(0,0,0)
pdf.cell(-48,3, txt= mydata['Skills'][1]['Hard Skill1'], ln=1, align= 'R')
pdf.cell(133,8, txt= mydata['Skills'][1]['Hard Skill2'], ln=1, align= 'R')
pdf.cell(94,3, txt= mydata['Skills'][1]['Hard Skill3'], ln= 1, align= 'R')
pdf.line(x1=200,x2=12, y1= 105, y2= 105)

#the next part will be my educational attainment
pdf.set_font('Courier', 'B', size=15)
pdf.set_text_color(102,71,34)
pdf.cell(0,13, txt= 'Educational Attainment', border=0, ln=2, align= 'C')

#this will be a lot huhuhu pardon me po.
pdf.set_font('Times', 'B', size=12)
pdf.set_text_color(0,0,0)
pdf.cell(40,3, txt= 'Tertiary Level',ln= 2, align='R')
pdf.set_font('Times', '', size=12)
pdf.cell(150,-3, txt=mydata['Education'][0]['Tertiary'], ln=0, align='R')
pdf.cell(-2.7,8, txt=mydata['Education'][0]['school1'], ln=1, align= 'R')
pdf.cell(158,3, txt= mydata['Education'][0]['Course'], ln=1, align='R')

#this will be really a lot huhuhu I'm really sorry but this will be for Senior High since i didn't graduate in hs, only completed.
pdf.set_font('Times', 'B', size=12)
pdf.set_text_color(0,0,0)
pdf.cell(44,13, txt= 'Secondary Level',ln= 2, align='R')
pdf.set_font('Times', '', size=12)
pdf.cell(132,-13, txt=mydata['Education'][1]['Secondary'], ln=0, align='R')
pdf.cell(-19,-2, txt=mydata['Education'][1]['school2'], ln=1, align='R')
pdf.cell(169,13, txt=mydata['Education'][1]['track'], ln=1, align='R')

#last for the educ attainment, swear T.T
pdf.set_font('Times', 'B', size=12)
pdf.set_text_color(0,0,0)
pdf.cell(40,6, txt= 'Primary Level',ln= 2, align='R')
pdf.set_font('Times', '', size=12)
pdf.cell(131,-6, txt= mydata['Education'][2]['Primary'], ln=0, align= 'R')
pdf.cell(32,4, txt= mydata['Education'][2]['school3'], ln=1, align= 'R')
pdf.line(x1=200,x2=12, y1= 165, y2= 165)

#Last part na po cguro, experience kuno hehe :>>
pdf.set_font('Courier', 'B', size=14)
pdf.set_text_color(102,71,34)
pdf.cell(40,14, txt= 'Profile', ln=2, align='L')
pdf.set_font('Times', '', size=12)
pdf.set_text_color(0,0,0)
pdf.multi_cell(0,5, txt=mydata['Experience'][0]['Profile'])

#Last na po talaga hehe, experience experience na :>>
pdf.line(x1=200,x2=12, y1= 195, y2= 195)
pdf.set_font('Courier', 'B', size=14)
pdf.set_text_color(102,71,34)
pdf.cell(0,15, txt= 'Work Experiences', ln=1, align= '')
pdf.set_text_color(0,0,0)
pdf.set_font('Times', 'B', size=12)
pdf.cell(30,1, txt=mydata['Experience'][0]['work'], ln= 1, align= 'R')
pdf.set_font('Times', '', size=12)
pdf.set_text_color(0,0,0)
pdf.cell(43,8, txt=mydata['Experience'][0]['company1'], ln= 1, align= 'R')




pdf.output("AZUELA, JULLIANE MAEVE.pdf")
