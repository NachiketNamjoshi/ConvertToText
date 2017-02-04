#!/usr/bin/env python

from distutils.core import setup
import re

VERSIONFILE = "version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
        verstr = mo.group(1)
else:
        raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE))

long_description = """
An Easy-to-Use and implement python library that converts
following types of file types to PURE TEXT file:

- PDF

By being Pure-Python, it should run on any Python platform with
dependencies on following external libraries:

- PyPDF2

It is therefore a useful tool for projects that rely on heavy
use of conversion of several file types. Just import this module
and you are ready to rumble!
"""

setup(
        name="ConvertToText",
        version=verstr,
        description="File to Text toolkit",
        long_description=long_description,
        author="Nachiket Namjoshi",
        author_email="nachiketnamjoshi@gmail.com",
        maintainer="Nachiket Namjoshi",
        maintainer_email="nachiketnamjoshi@gmail.com",
        url="https://github.com/NachiketNamjoshi/ConvertToText",
        classifiers = [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: BSD License",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
            "Topic :: Software Development :: Libraries :: Python Modules",
            ],
        packages=["ConvertToText"],
        data_files=[('/bin', ['antiword'])]
)
