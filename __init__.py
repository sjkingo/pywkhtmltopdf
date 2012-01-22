import os
import subprocess

class HTMLToPDFConverter(object):
    args_to_bin = {
        'margin_bottom': '1cm',
        'margin_left': '1cm',
        'margin_right': '1cm',
        'margin_top': '1cm',
    }

    def __init__(self, path_to_bin='/usr/bin/wkhtmltopdf', **kwargs):
        self.path_to_bin = path_to_bin
        for k, v in kwargs.items():
            setattr(self.args_to_bin, k, v)

    def convert(self, input_obj):
        # construct path for exec
        args = [self.path_to_bin, '-q']
        for k, v in self.args_to_bin.items():
            args.append('--%s' % k.replace('_', '-'))
            args.append(v)
        args += ['-', '-'] # input from stdin, output to stdout

        if not os.path.isfile(self.path_to_bin):
            raise Exception('wkhtmltopdf not found at %s' % self.path_to_bin)

        p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)

        if hasattr(input_obj, 'read'):
            i = input_obj.read()
        else:
            i = input_obj
        stdout, stderr = p.communicate(i)

        if len(stderr) != 0:
            raise Exception(stderr)

        return stdout
