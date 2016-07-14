import os
import shutil
import subprocess
import tempfile

__version__ = '0.1.3'

class HTMLToPDFConverter(object):
    """Class to convert HTML documents to PDF using wkhtmltopdf."""

    args_to_bin = {
        'margin_bottom': '1cm',
        'margin_left': '1cm',
        'margin_right': '1cm',
        'margin_top': '1cm',
    }

    def __init__(self, path_to_bin='/usr/bin/wkhtmltopdf', **kwargs):
        self.path_to_bin = path_to_bin
        if not os.path.isfile(self.path_to_bin):
            raise Exception('wkhtmltopdf not found at %s; see https://github.com/sjkingo/pywkhtmltopdf#obtaining-wkhtmltopdf' % self.path_to_bin)

        for k, v in kwargs.items():
            self.args_to_bin[k] = v

    def convert(self, input_obj, header=None, footer=None, orientation='portrait'):
        """Convert the given input to PDF and return the binary text of the PDF, suitable for writing to file.

        Arguments:
        input_obj -- a string or file-like object representing the HTML document to convert

        Keyword arguments:
        header -- a string representing the HTML header that should appear on each page of the PDF (optional)
        footer -- a string representing the HTML footer that should appear on each page of the PDF (optional)
        orientation -- either 'portrait' or 'landscape'
        """
        temp_dir = tempfile.mkdtemp()
        try:
            r = self._convert(temp_dir, input_obj, header, footer, orientation)
        except:
            raise
        finally:
            shutil.rmtree(temp_dir)
        return r

    def _convert(self, temp_dir, input_obj, header, footer, orientation):
        # construct path for exec
        args = [self.path_to_bin, '-q']
        for k, v in self.args_to_bin.items():
            args.append('--%s' % k.replace('_', '-'))
            args.append(v)

        # write out header if it was given
        if header is not None:
            header_filename = os.path.join(temp_dir, 'header.html')
            with open(header_filename, 'w') as fp:
                fp.write(header)
            args += ['--header-html', header_filename]

        # write out footer if it was given
        if footer is not None:
            footer_filename = os.path.join(temp_dir, 'footer.html')
            with open(footer_filename, 'w') as fp:
                fp.write(footer)
            args += ['--footer-html', footer_filename]

        # orientation
        args += ['-O', orientation]

        args += ['-', '-'] # input from stdin, output to stdout

        p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)

        if hasattr(input_obj, 'read'):
            i = input_obj.read()
        else:
            i = input_obj
        stdout, stderr = p.communicate(i)

        return stdout
