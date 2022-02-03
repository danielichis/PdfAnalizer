import pdfplumber
with pdfplumber.open("IGA.PDF") as temp:
  first_page = temp.pages[5]
  print(first_page.extract_text())
