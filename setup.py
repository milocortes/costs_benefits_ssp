from setuptools import find_packages, setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="costs_benefits_ssp",
    version="0.0.1",
    author="Hermilo Cortés",
    author_email="hermilocg@tec.com",
    description="Costs and Benefits package ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/milocortes/costs_benefits_ssp.git",
    install_requires=[
        "SQLAlchemy>=2.0.36"
    ],
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    tests_require=['pytest'],
)
