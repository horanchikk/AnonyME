import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyanonyme",
    version="1.0.0",
    author="AVOCAT",
    author_email="social.ethosa@gmail.com",
    description="Python anonyme client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/horanchikk/anonyme/tree/dev/client/python",
    packages=setuptools.find_packages(),
    license="LGPLv3",
    keywords="Python Gql",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Github": "https://github.com/horanchikk/anonyme/tree/dev/client/python",
        "Documentation": "https://github.com/horanchikk/anonyme",
    },
    python_requires=">=3",
    install_requires=[
        'requests'
    ]
)
