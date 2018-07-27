import os
from setuptools import setup


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setup(
    name="samplify-python",
    version="0.0.9.5",
    author="Samplify Limited",
    author_email="developers@samplify.io",
    description="Python wrapper for Samplify API",
    license="MIT",
    keywords="",
    url="https://samplify.io",
    packages=['samplify'],
    package_data={},
    test_suite='',
    long_description=read('README.rst'),
    install_requires=[
        'requests'
    ],
    tests_require=[
    ],
    classifiers=[
    ],
)
