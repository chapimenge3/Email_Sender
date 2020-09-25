import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-send-e-mail", 
    version="0.1",
    author="Temkin Mengistu",
    author_email="chapimenge3@gmail.com",
    description="Easy Email sender Python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chapimenge3/Email_Sender",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)