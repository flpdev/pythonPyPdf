import sys, os, pdfrw
writer = pdfrw.PdfWriter()
soma = 0
for page in pdfrw.PdfReader('Doc1.pdf').pages:
    for y in [0, 0.5]:
        soma = soma + 1
        newpage = pdfrw.PageMerge()
        newpage.add(page, viewrect=(0, y, 1, 0.5))
        writer = pdfrw.PdfWriter()
        writer.addpages([newpage.render()])
        writer.write(f'divididos/output{soma}.pdf')
        print()
