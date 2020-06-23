import setuptools


setuptools.setup(
    name="github-web-hook",
    version="0.0.2",
    author="drunkpig",
    author_email="xuchaoo@gmail.com",
    description="github webhook",
    long_description=open("README.md", "r", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/drunkpig/githubwebhook",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=open('requirements.txt').read().splitlines(),
    scripts=['bin/startwebhook'],
    python_requires='>=3.7',
)