import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cpb",
    version="1.0.0",
    author="Leonardo Guarnieri de Bastiani",
    author_email="leogbastiani@gmail.com",
    description="Clipboard history on Windows",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leobastiani/cpb",
    install_requires=[
        'pyperclip',
    ],
    packages=setuptools.find_packages(),
    entry_points = {
        'console_scripts': ['cpb=cpb:main'],
    },
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: Microsoft :: Windows",
    ]
)
