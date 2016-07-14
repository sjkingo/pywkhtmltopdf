#!/usr/bin/env python

import os.path
from pywkhtmltopdf import HTMLToPDFConverter

def convert(filename):
    output_filename = os.path.splitext(filename)[0] + '.pdf'
    c = HTMLToPDFConverter()
    in_fp = open(filename, 'r')
    b = c.convert(in_fp)
    with open(output_filename, 'wb') as out_fp:
        out_fp.write(b)

if __name__ == '__main__':
    in_filename = os.path.join(os.path.dirname(__file__), 'unicode.html')
    convert(in_filename)
