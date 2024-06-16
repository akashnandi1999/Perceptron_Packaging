import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PKG_NAME = "perceptron_pkg"
USER_NAME = "akashhnandi1999"
PROJECT_NAME = "perceptron-pkg"

setuptools.setup(
    name=f"{PKG_NAME}-{USER_NAME}",
    version="0.0.3",
    author=USER_NAME,
    author_email="akashnandi446@gmail.com",
    description="A small package for perceptron",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{USER_NAME}/{PROJECT_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{USER_NAME}/{PROJECT_NAME}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[
        "numpy==1.26.4",
        "pandas==2.2.2",
        "joblib==1.4.2"
    ]
)