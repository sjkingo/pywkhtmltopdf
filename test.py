#!/usr/bin/python

from StringIO import StringIO

from __init__ import HTMLToPDFConverter

def main():
    s = StringIO('<p>Hello there!</p><p><strong>How are you today?</strong></p>')

    c = HTMLToPDFConverter()
    o = c.convert(s, header='<p>Header</p>', footer='<p style="font-size: 8pt;">Footer</p>')

    output_filename = 'test.pdf'
    with open(output_filename, 'wb') as fp:
        fp.write(o)
    print('Wrote %d bytes to %s' % (len(o), output_filename))


if __name__ == '__main__':
    main()
