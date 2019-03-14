#!/usr/bin/python
# coding=utf-8
# Produces new PDF file with all pages rotated by 90 degrees.
# by Ben Byram-Wigfield v2.1


import os

from objc_util import *
from pathlib import Path
import dialogs

PDFDocument = ObjCClass('PDFDocument')
NSURL = ObjCClass('NSURL')
home = "/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/"

def rotate(filename):
		shortName = Path(filename).stem
		outFilename = home + shortName + "+90.pdf"
		pdfURL = NSURL.fileURLWithPath_(filename)
		pdfDoc = PDFDocument.alloc().initWithURL_(pdfURL)
		if pdfDoc:
			pages = pdfDoc.pageCount()
			for p in range(0, pages):
				page = pdfDoc.pageAtIndex_(p)
				existingRotation = page.rotation()
				newRotation = existingRotation + 90
				page.setRotation_(newRotation)

			pdfDoc.writeToFile_(outFilename)

if __name__ == '__main__':
		filename = dialogs.pick_document(types=['public.data'])
		rotate(filename)
