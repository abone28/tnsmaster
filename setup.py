from distutils.core import setup

# Get the long description from the README file
with open("README.rst") as readme:
    README_TEXT = readme.read()

setup(
    name="tnsmaster",
    version="0.1.0",
    description="Toolset for mastering tnsnames",
    long_description=README_TEXT,
    author="Dirk Fuchs",
    author_email="somewhere@over-the-rain.bow",
    url="https://github.com/difu/tnsmaster",
    packages=["tnsnames"],
    python_requires='>=3.6, <4',
    install_requires=[
        "antlr4-python3-runtime>=4.5,<4.6",
        ],
    data_files=[("tests", ["__init__.py", "test_aliasFinder.py",
                           "testFiles/tnsnames.ora"])],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: System Administrators",
        "Topic :: Database",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3 :: Only',
    ],
    license="MIT"
)
