from setuptools import setup, find_packages

setup(
    name="py3d",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "ipython>=8.0.0",
        "jupyter>=1.0.0",
        "notebook>=6.0.0",
        "numpy>=1.20.0",
        "pandas>=1.3.0",
        "d3>=0.0.1"
    ],
) 