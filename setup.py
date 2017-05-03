import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname+'.md')).read()

setup(
    name = "minhash",
    version = "0.0.1",
    author = "Anastasia Aizman",
    author_email = "anastasia.aizman@gmail.com",
    description = ("minhash"),
    license = "BSD",
    keywords = "minhash",
    url = "",
    packages=['minhash'],
    long_description=read('README'),
)