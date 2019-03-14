from objc_util import *
import dialogs
	
PDFDocument = ObjCClass('PDFDocument')
NSURL = ObjCClass('NSURL')


def pageCount(pdfPath):
	pdfURL = NSURL.fileURLWithPath_(pdfPath)
	pdfDoc = PDFDocument.alloc().initWithURL_(pdfURL)
	if pdfDoc:
		return pdfDoc.pageCount()


if __name__ == '__main__':
	

	filename = dialogs.pick_document(types=['public.data'])
	print(pageCount(filename))
