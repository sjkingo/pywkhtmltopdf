# pywkhtmltopdf

pywkhtmltopdf is a small Python wrapper library around
[wkhtmltopdf](http://wkhtmltopdf.org/), allowing HTML to PDF conversion from
Python code.

It fully supports Python 2.7, with basic Python 3 support provided in version 0.1.1.

## Obtaining wkhtmltopdf

This library requires the `wkhtmltopdf` binary be present on your system. A
dependency of this binary is Qt4. Most distributions provide a wkhtmltopdf
package, however it will be dynamically linked against vanilla Qt4 and will
only support very basic conversion options.

The creators of wkhtmltopdf have patched Qt4 to support the extra features such
as headers and footers. To use this version, we must download a statically
linked binary from their website, instead of using your distribution's package:

1. Go to the [wkhtmltopdf downloads page](http://wkhtmltopdf.org/downloads.html#testing)

2. Pick the correct architecture of the Testing version and download it

3. Extract and move the binary to a location on your `$PATH`:

   ```bash
   $ tar -xf wkhtmltox-*.xz
   $ cp -p wkhtmltox/bin/wkhtmltopdf $BIN_PATH
   ```

4. Install the required dependencies from your system's package manager:

   * libXrender
   * libXext
   * libX11

5. Verify the output of `wkhtmltopdf -V` contains `(with patched qt)`

## Usage

A simple example to output some text to a PDF file on disk (example in Python 2.7):

```python
>>> from StringIO import StringIO
>>> import pywkhtmltopdf as pdf
>>> html = StringIO('<p>Hello, world!</p>')
>>> c = pdf.HTMLToPDFConverter()
>>> output = c.convert(html)
>>> with open('test.pdf', 'wb') as fp:
...     fp.write(output)
```

If you haven't installed the `wkhtmltopdf` binary into a location on `$PATH`,
you must specify the absolute path to the binary using the `path_to_bin`
keyword argument to the constructor, for example:

```python
>>> c = pdf.HTMLToPDFConverter(path_to_bin='/home/user/wkhtmltopdf')
```

Other options may be given as keyword arguments to `HTMLToPDFConverter.convert()`.

Full API documentation is available by running `pydoc pywkhtmltopdf`, and
example scripts can be found under the `samples/` directory of this repository.
