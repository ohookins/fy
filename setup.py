# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ""

setup(
    long_description=readme,
    name="fy",
    version="1.0.14",
    python_requires="==3.*,>=3.7.0",
    author="Rob Wilson",
    author_email="roobert@gmail.com",
    entry_points={"console_scripts": ["fy = fy.__main__:main"]},
    packages=[
        "fy",
        "fy.environment",
        "fy.infra",
        "fy.kubernetes",
        "fy.skeleton",
        "fy.terraform",
        "fy.vault",
    ],
    package_dir={"": "."},
    package_data={"fy": ["*.txt"]},
    install_requires=["pyyaml==5.*,>=5.3.0", "sh==1.*,>=1.12.14"],
)
