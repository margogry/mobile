from docxtpl import DocxTemplate
import comtypes.client

from lab1 import *
from lab2 import *

resLab1 = tarific1()
resLab2 = tarific2()

doc = DocxTemplate("lab3_tmpl.docx")
context = { 'bank' : 'ОАО Твой Банк',
            'bik' : '123456',
            'kpp':'123456',
            'reciever':'ОАО Интернет',
            'first': '12345678910',
            'second': '12345678910',
            'inn': '123456789',
            'address1' : 'г. Санкт-Петербург, ул. Леносовета, 23',
            'index' : '123456',
            'address2' : 'г. Санкт-Петербург, ул. Вавиловых, 12к2',
            'osnovanie':'Договор №6 от 01.03.2045',
            'name1':'Телефония',
            'name2':'Интернет',
            'sum1': resLab1,'sum2': resLab2,
            'overall': resLab1 + resLab2,
            'director':'Брунова.А.М.',
            'accountant':'Брунова.А.М.',
            'n':'2','d':'1 июня','y':'20', 'buy':'ООО Что-то Интересное', 'rus': 'rub'}
doc.render(context)
doc.save("lab3.docx")
wdFormatPDF = 17

in_file = r"C:\\Users\\Анастасия\\PycharmProjects\\mobile\\lab3\\lab3.docx"
out_file = r"C:\\Users\\Анастасия\\PycharmProjects\\mobile\\lab3\\lab3.pdf"

word = comtypes.client.CreateObject('Word.Application')
doc = word.Documents.Open(in_file)
doc.SaveAs(out_file, FileFormat=wdFormatPDF)
doc.Close()
word.Quit()