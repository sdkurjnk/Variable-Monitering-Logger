from setuptools import setup, Extension, find_packages

module = Extension(
    name="vml.vml_engine",
    sources=["src/vml/vml_engine.c"], 
)

setup(
    name="vml-logger",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    ext_modules=[module],
    author="Your Name",
    description="A Variable Monitoring Logger with C-Engine and Visualizer",
    python_requires=">=3.7",
)