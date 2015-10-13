from setuptools import find_packages, setup

from pywkhtmltopdf import __version__

setup(
    name='pywkhtmltopdf',
    version=__version__,
    license='BSD',
    author='Sam Kingston',
    author_email='sam@sjkwi.com.au',
    description='Python wrapper library around wkhtmltopdf',
    url='https://github.com/sjkingo/pywkhtmltopdf',
    packages=find_packages(),
)
