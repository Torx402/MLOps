Another important task is to specifically define the exact packages required to run the project. This is defined line by line in a requirements.txt file in the project directory. Suppose a project you have requires numpy and pandas, the requirements look like:

```text
numpy
pandas
```

and that's it! All that is left is to run

```bash
pip install requirements.txt
```

If you would like to define specific versions, you may do so very simply

```bash
numpy==1.0
pandas==1.0
```