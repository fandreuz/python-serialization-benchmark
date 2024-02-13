from setuptools import find_packages, setup

setup(
    name="python-serialization-benchmark",
    version="0.0.0",
    url="https://github.com/fandreuz/python-serialization-benchmark.git",
    author="Francesco Andreuzzi",
    author_email="fandreuz@cern.ch",
    description="Simple serialization benchmark",
    packages=find_packages(),    
    install_requires=["numpy"],
)