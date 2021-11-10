import setuptools

with open("README.md") as file:
    read_me_description = file.read()

setuptools.setup(
    name="cookpad",
    version="0.1",
    author="Baklaza",
    author_email="baklaza.dev@bk.ru",
    description="API interface of the most popular website with recipes",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="package_github_page",
    packages=['cookpad'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)