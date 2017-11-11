from PyPDF2 import PdfFileReader, PdfFileWriter
import os
dir_path = os.path.dirname(os.path.realpath('PDFSplitter.py'))
for file in os.listdir(dir_path + '/Files'):
    if file != '.DS_Store':
        inputpdf = PdfFileReader(open('Files/' + file, "rb"))
        for i in range(inputpdf.numPages):
            if i in [0, 1, 2]:
                y = i + 1
            elif i == 3:
                y = 45
            elif i == 4:
                y = i
            elif i == 5:
                y = i
            output = PdfFileWriter()
            output.addPage(inputpdf.getPage(i))
            with open('Outputs/G2' + file.replace('.pdf','') + "_d%s.pdf" % str(y), "wb") as outputStream:
                output.write(outputStream)
