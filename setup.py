from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        name="qrng_wrapper",
        sources=["qrng.pyx", "main.c"],
        language="c",
    )
]

setup(
    ext_modules=cythonize(extensions),
)