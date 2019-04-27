from setuptools import setup

setup(
    name="pymail",
    version="1.0.1",
    description="Send emails from the command line",
    author="Amit kumar",
    url="https://github.com/amyth07/pymail",
    author_email="amitkumar21326@gmail.com",
    install_requires=["requests"],
    scripts=["pymail.py"],
)
