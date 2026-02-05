from setuptools import setup, Extension, find_packages

module = Extension(
    name="vml.vml_engine",
    sources=["vml/vml_engine.c"],
)

setup(
    name="vml-logger",
    version="0.1.0",
    packages=find_packages(),
    ext_modules=[module],
)