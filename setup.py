from setuptools import setup, find_packages

setup(
    name="py3d",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        # Add your dependencies here
    ],
) 