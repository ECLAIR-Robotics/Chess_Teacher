from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        "py_hello",
        ["hello_python.cpp"],
        include_dirs=[pybind11.get_include()],
        language='c++',
    ),
]

setup(
    name='py_hello',
    ext_modules=ext_modules,
)

print('finished')
