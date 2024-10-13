from setuptools import setup, Extension
from Cython.Build import cythonize

# define C extension
ext_modules = [
    Extension(
        "qrng_wrapper",                        # module name
        sources=["qrng_wrapper.pyx", "qrng.c"] # source files
    )
]

setup(
    name="qrng_wrapper",
    ext_modules=cythonize(ext_modules),
)