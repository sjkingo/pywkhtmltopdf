#!/usr/bin/python

from StringIO import StringIO

import sys
sys.path.append('../..')
from pywkhtmltopdf import HTMLToPDFConverter

def main():
    s = StringIO('<p>This document is in landscape.</p>')
    c = HTMLToPDFConverter()
    o = c.convert(s, orientation='landscape')

    output_filename = 'landscape.pdf'
    with open(output_filename, 'wb') as fp:
        fp.write(o)
    print('Wrote %d bytes to %s' % (len(o), output_filename))


if __name__ == '__main__':
    main()
