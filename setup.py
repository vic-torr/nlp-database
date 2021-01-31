"""
    nlp_db
"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
req_file = 'requirements.txt'

# read requirements
with open(req_file) as f:
    required = f.read().splitlines()
    
setuptools.setup(
    name="nlp_db",
    version="0.0.2",
    author="vektor",
    author_email="timtkd2@yahoo.com.br",
    description="nlp_db",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=required,
    url="https://github.com/vic-torr/nlp_db",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    include_package_data=True

)
