from setuptools import setup, find_packages

with open('requirements.txt', 'r') as _f:
    requirements = [line for line in _f.read().split('\n')]
    
setup(
    name="summarize",
    description="cli tool to summarize text from a given file",
    author="Mohammed Mahmood",
    packages=find_packages(),
    entry_points=
    """
    [console_scripts]
    summarize=summarize.main:main
    """,
    install_requires=requirements,
    version="0.0.1",
    url="https://github.com/Torx402/MLOps/MLOps/Projects"
)