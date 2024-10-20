So it is finally here, your big day, you are ready to release the CLI project you have been working on for months, feels good doesn't it? It would feel amazing if only you knew how to package your project in such a way that doesn't require you to run `python your_project.py`, so how do you do that?

Let's consider the program that we have been working on, except the filename is `main.py` in a folder called `jformatter`. A tree looks like:

```terminal
├── jformatter  
│   └── main.py  
└── setup.py
```

The contents of `setup.py` would be:
```python
from setuptools import setup, find_packages

setup(
	name="jformat",
	version="0.0.1",
	description="Reformats JSON files to stdout",
	install_requires=["click"],
	entry_points="""
	[console_scripts]
	jformat=jformat.main:main
	"""
	author="Your Name",
	author_email="Your email here",
	packages=find_packages(),
)
```

There a few important things to point out here:

* `install_requires` can be explicitly defined here or it could also be parsed from requirements.txt
* `entry_points` defines a console script `jformat` which points to the `main` function of `main.py` module which is part of `jformat`

And voila! You can now run `python setup.py develop` which will install the tool! Now, it is enough to run `jformat` from the terminal to run your command-line tool!