from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="py4mbd",
    version="0.0.1",
    description="Framework for implementing Model Based Design in Python",
    py_modules=["py4mbd/inner", "py4mbd/outer"],
    package_dir={"": "SRCS"},
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/Palani-SN/py4mbd",
    author="Palani-SN",
    author_email="psn396@gmail.com",

    install_requires = [
        "blessings ~= 1.7"
    ],

    extras_require = {
        "dev": [
            "pytest >= 3.7",
            "check-manifest",
            "twine",
        ],
    },
)
