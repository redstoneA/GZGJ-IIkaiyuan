import docx
from decimal import Decimal


def mb(type, max):
    doc = docx.Document()
    if type == "Π表":
        doc.add_heading("Π表")
        pa = doc.add_paragraph()
        pi = Decimal(3.14)
        for i in range(1, max + 1):
            id = Decimal(i)
            pa.add_run(str(i)+"Π≈"+str(id*pi.quantize(Decimal('0.01')))+"    ")
    if type == "平方表":
        doc.add_heading("平方表")
        pa = doc.add_paragraph()
        for i in range(1, max + 1):
            id = Decimal(i)
            pa.add_run(str(i)+"²="+str(id*id)+"    ")
    if type == "乘法表":
        doc.add_heading("乘法表")
        pa = doc.add_paragraph()
        for i in range(1, max + 1):
            for j in range(1, max + 1):
                id = Decimal(i)
                jd = Decimal(j)
                pa.add_run(str(i)+"×"+str(j)+"="+str(id*jd)+"    ")
    doc.save(str(type)+".docx")
