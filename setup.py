"""
Setup the wispy package.
"""
import setuptools

with open("README.md", "r") as readme:
    LONG_DESC = readme.read()

DESC = ("Will's Super Python Utilities")

CATAGORIES = ["Programming Language :: Python :: 3",
              "License :: OSI Approved :: Apache Software License",
              "Operating System :: OS Independent"]

setuptools.setup(
    name="wispy",
    author="William E. Fondrie",
    author_email="fondriew@gmail.com",
    description=DESC,
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    url="https://github.com/wfondrie/wispy",
    packages=setuptools.find_packages(),
    license="Apache 2.0",
    classifiers=CATAGORIES,
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "seaborn"
    ],
    use_scm_version=True,
    setup_requires=["setuptools_scm"]
)
