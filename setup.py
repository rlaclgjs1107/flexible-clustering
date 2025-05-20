from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
from codecs import open
from os import path
import numpy

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

extensions = [
    Extension(
        "flexible_clustering.unionfind",
        ["flexible_clustering/unionfind.pyx"],
        include_dirs=[numpy.get_include()],
    )
]

setup(
    name='flexible_clustering',
    version='0.1.0',
    description='Flexible Clustering',
    long_description=long_description,
    author="Matteo Dell'Amico",
    author_email='matteo_dellamico@symantec.com',
    license='BSD 3-clause',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='clustering non-metric',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        "hdbscan (>=0.8.40,<0.9.0)",
        "numpy (>=2.2.6,<3.0.0)"
    ],
    ext_modules=cythonize(extensions),
)
