from pathlib import Path
from setuptools import setup, find_packages


def read(fname):
    p = Path(__file__).parent / fname
    with p.open(encoding="utf-8") as f:
        return f.read()

setup(
    name="test-cmd",
    version="0.4.6",
    author="Esukhia developers",
    author_email="esukhiadev@gmail.com",
    description="OpenPecha Toolkit allows state of the art for distributed standoff annotations on moving texts",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    license="Apache2",
    url="https://github.com/OpenPoti/openpecha-toolkit",
    packages=find_packages(),
    install_requires=[
        'Click==7.0',
        'PyGithub==1.43.8',
        'GitPython==3.1.0',
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": ["test-cmd=cli:cli"] # command=package.module:function
    },
)
