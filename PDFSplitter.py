from PyPDF2 import PdfFileReader, PdfFileWriter
import os
dir_path = os.path.dirname(os.path.realpath('PDFSplitter.py'))
for file in os.listdir(dir_path + '/Files'):
    if file != '.DS_Store':
        inputpdf = PdfFileReader(open('Files/' + file, "rb"))
        for i in range(inputpdf.numPages):
            y = i + 1
            output = PdfFileWriter()
            output.addPage(inputpdf.getPage(i))
            with open('Outputs/' + file.replace('.pdf','') + "_d%s.pdf" % str(y), "wb") as outputStream:
                output.write(outputStream)
