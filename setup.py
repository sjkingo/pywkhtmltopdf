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
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
