# ========================================================================
# CRA Global Integrity Engine - Setup Script
# Author: Cory Miller
# License: Apache 2.0
# Year: 2025
# ========================================================================

from setuptools import setup, find_packages

setup(
    name="cra-integrity-engine",
    version="0.1.0",
    author="Cory Miller",
    author_email="cmiller@example.com",
    description="Tamper-evident, verifiable integrity engine for digital artifacts",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cmiller9851-wq/cra-integrity-engine",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "pytest>=7.0",
        "mermaid-cli>=9.0",
        "python-dateutil>=2.8"
    ],
    entry_points={
        "console_scripts": [
            "cra=src.cra:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.11",
)