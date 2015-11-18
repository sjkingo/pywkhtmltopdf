# pywkhtmltopdf

pywkhtmltopdf is a Python wrapper library around
[wkhtmltopdf](http://code.google.com/p/wkhtmltopdf/), allowing HTML to PDF
conversion from Python code. It supports the most common options (including
headers and footers).

It fully supports Python 2.7, with basic Python 3 support provided in version 0.1.1.

To use, you must have wkhtmltopdf installed (either system-wide or locally).
Some features (such as headers and footers) require it to be linked aginst
their modified version of Qt4, so it is recommended you use the version that
is statically linked against Qt4. It depends on the following packages:

* libXrender
* libXext

It has been tested against version [0.11.0_rc1 on
amd64](http://wkhtmltopdf.googlecode.com/files/wkhtmltopdf-0.11.0_rc1-static-amd64.tar.bz2),
though it should work with newer versions.

## Installation

1. Install wkhtmltopdf 0.11.0\_rc1:

    ```
    $ curl https://raw.githubusercontent.com/sjkingo/pywkhtmltopdf/master/install_wkhtmltopdf_binary.sh | sh
    $ sudo dnf install libXrender libXext
    ```

2. Install this package:

    ```
    $ pip install pywkhtmltopdf
    ```

## Usage

A simple example to output some text to a PDF file on disk:

```python
>>> from StringIO import StringIO
>>> import pywkhtmltopdf as pdf
>>> h = StringIO('<p>Hello, world!</p>')
>>> c = pdf.HTMLToPDFConverter()
>>> output = c.convert(s)
>>> with open('test.pdf', 'wb') as fp:
...     fp.write(output)
```

If you haven't installed wkhtmltopdf system-wide, you must specify the path
to the binary using the `path_to_bin` keyword argument to the constructor, for example:

```python
>>> c = pdf.HTMLToPDFConverter(path_to_bin='/home/user/wkhtmltopdf')
```

Other options may be given as keyword arguments to `HTMLToPDFConverter.convert()`.

Full API documentation is available by running `pydoc pywkhtmltopdf`, and
example scripts can be found under the `samples/` directory.
