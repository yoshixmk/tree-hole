from pdf2docx import Converter

for i in range(1, 8):
  pdf_file = f'./samples/{i}.pdf'
  docx_file = f'./samples/{i}.docx'

  # convert pdf to docx
  cv = Converter(pdf_file)
  cv.convert(docx_file, start=0, end=None)
  cv.close()
