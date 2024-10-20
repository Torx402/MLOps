# ArgParse Framework

One of the things you may be interested in as part of MLOps is that of adding support for your scripts to be run from the command line interface (CLI). Enabling this requires support for many functionalities such as help menus and parsing arguments and options that would be supplied when the script is run. To this end, the `argparse` module can be used to achieve this. To begin, suppose that you'd like to run a script that format arguments from a json file and supports command line arguments and options. This looks something like:

```python
import os
import sys
import json

def formatter(string, sort_keys=True, indent=4):
	# load incoming string into json
	loaded_json = json.loads(string)
	# dump as string
	return json.dumps(loaded_json, sort_keys=sort_keys, indent=indent)

def main(path, no_sort):
	if no_sort:
		sort_keys = False
	else: 
		sort_keys = True
	with open(path, 'r') as _f:
		print(
			formatter(_f.read(), sort_keys=sort_keys)
		)

if __name__ = "__main__":
	main(sys.argv[-1], no_sort=False)
```

The above will take the last command-line argument as a path and pass its contents to the `formatter` function with the `no_sort` flag set to `False`. However, in the above implementation, there are some problems.

* We are unable to provide a help menu to let the user know how to use this script
* We are unable to pass an option to set the `no_sort` flag to `True`

This is where the `argparse` framework comes into play, the main change will be made to the if conditional at the end.

```python
import argparse

if __name__ = "__main__":
	parser = parseargs.ArgumentParser(description="This is the jformat tool")
	args = parser.parse_args()
	main(sys.argv[-1], no_sort=False)
```

With these simple changes, we are now able to accept command-line arguments (options) that can change the behavior of the script. For example, we may define an argument `--sort` to set the `no_sort` flag to `True`. 

```python
if __name__ = "__main__":
	parser = parseargs.ArgumentParser(description="This is the jformat tool")
	parser.add_argument("--sort", action="store_true", help="Option to enable sorting")
	args = parser.parse_args()
	main(sys.argv[-1], no_sort=False)

```

With these changes, the `--sort` option will now show up in the help menu, and the value of this flag is now stored as an attribute in the `args` object, i.e. `args.sort` is a boolean that is `False` by default, and `True` when the `--sort` option is passed. The terminal output of the `jformat` script with the `-h` option can be seen below.

```terminal
usage: jformat.py [-h] [--sort]

This is the jformat tool

options:
  -h, --help  show this help message and exit
  --sort      Option to enable sorting
```

# Click Framework

You saw that the `argparse` framework enabled us to run scripts in the terminal and pass command-line arguments and options to said script. The next step would be to implement the logic of checking command-line argument numbers, if they are of the right type, and in case of our formatter, make sure the path being passed through actually exists, etc. This is a lot of work, in fact this is work that does not need to be done thanks to the `click` framework.

The `click` framework allows implementing command-line scripts using function decorators to define what arguments to take, their type, and how they should be treated. Let's start by recreating the same thing we last presented but in the click framework.

```python
import json
import click  

def formatter(string, sort_keys=True, indent=4):

	# load incoming string into json
	loaded_json = json.loads(string)
	# dump as string
	return json.dumps(loaded_json, sort_keys=sort_keys, indent=indent)

@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--sort', '-s', is_flag=True, help="Sort JSON file by keys")
def main(path, *sort):
	with open(path, 'r') as _f:
		print(
			formatter(_f.read(), sort_keys=sort)
		)

if __name__ == "__main__":

	main()
```

We can notice many changes here, so let's go over them one by one:

* `@click.command()` uses the decorate function as callback and passes subsequent options and arguments to it
* `@click.argument('path', type=click.Path(exists=True))` defines an argument, `path`, whose type is define as `click.Path`, which has the argument `exists=True` passed to it.
	* `exists=True` ensures that the path that is being passed through actually exists
* `@click.option('--sort', '-s', is_flag=True)` defines a new option with aliases `--sort` and `-s`, alongside the argument `is_flag=True` which specifies that this is a flag and hence, a boolean. 
* The defined argument and option are passed through as their names in the definition of the main function

And that's it! Let's try running the script with the `--help` flag and see its output.

```terminal
format_click.py --help
Usage: jformat_click.py [OPTIONS] PATH

Options:
  -s, --sort  Sort JSON file by keys
  --help      Show this message and exit.
```

Passing a path that does not exist results in

```terminal
python jformat_click.py sth
Usage: jformat_click.py [OPTIONS] PATH
Try 'jformat_click.py --help' for help.

Error: Invalid value for 'PATH': Path 'sth' does not exist.
```

As we can see, click takes care of a lot of the logic required to define and pass valid command-line arguments and options, which makes life a lot easier!