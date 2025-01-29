from setuptools import setup, find_packages

setup(
    name="chess_analyzer",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "python-chess>=1.9.0",
        "pandas>=2.0.0",
        "streamlit>=1.22.0",
    ],
)