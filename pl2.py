import pdfplumber
import re
from docxtpl import DocxTemplate
doc=DocxTemplate("PlantillaPrincipal.docx")
with pdfplumber.open("IGA.PDF") as temp:
  first_page = temp.pages[0]
  texto1=first_page.extract_text()

titulo=re.findall(r'\".*\"',texto1,flags=re.S|re.I)
titu=titulo[0].replace("\n","")
ruc=re.findall(r'\d{11}',texto1,flags=re.M|re.I)
distrit=re.findall(r'Distrito:\D.*.',texto1,flags=re.M|re.I)
prov=re.findall(r'Provincia:\D.*.',texto1,flags=re.M|re.I)
dep=re.findall(r'Departamento:\D.*.',texto1,flags=re.M|re.I)
especialista=re.findall(r'Nombre del profesional responsable: \D.*.',texto1,flags=re.M|re.I)
dni_especialista=re.findall(r'DNI: \d{8}',texto1,flags=re.M|re.I)
dni_titular=re.findall(r'Documento de identidad Nº: \d{8}',texto1,flags=re.M|re.I)
prof_especialista=re.findall(r'de  profesión\D.*\n.?\D.*[,]',texto1,flags=re.M|re.I)
titular=re.findall(r'Nombres completos:\D.*',texto1,flags=re.M|re.I)
domicilio_proponente=re.findall(r'[]  Domicilio Legal:\D.*?[]',texto1,flags=re.S|re.I)
nro_colegiatura_especialista=re.findall(r'Número de colegiatura: \d{6}',texto1,flags=re.M|re.I)
institucion=re.findall(r'Razón Social:\D.*',texto1,flags=re.M|re.I)
print(titu)

context={
    "Especialist":"Ingeniero ambiental",
    "Fecha":"29/01/2022",   
    "Titulo":"29/01/2022",
}

#doc.render(context)
#doc.save("plantilla2.docx")
