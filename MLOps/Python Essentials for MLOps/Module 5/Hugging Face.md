Hugging Face is a Python Library which provides APIs for various pre-trained models and datasets. We will start by covering the pre-trained models, which are called transformers in hugging face. 

# Transformers

Transformers are pipelines which are basically an end-to-end machine learning project, providing necessary pre-processing steps as well. Transformers have an API which makes it easy to use. Let's take a look at how to implement a model using this. 

We will implement an NLP pipeline which will summarize the a given text.

```python
from transformers import pipeline

# defines a pipeline for a specific application and specifies the
# model in as an argument
generator = pipeline("summmariz", model="t5-base")
```

Afterwards, we can pass the text via

```python
generator("summarize: ...")
```

Which will basically summarize the given text, the specific usage for any pipeline can be found [here](https://huggingface.co/docs/transformers/index).

# Datasets

Hugging face a large number of datasets which can be used for use with models. In code, this looks like

```python
from datasets import load_dataset, list_datasets

available = list_datasets()
print(len(available))
print([i for i in available if '/' not in i])
```

which will basically print all datasets provided by hugging face, '/' indicates that it is user submitted.

To load a dataset, it is simply enough to pass the dataset name to the `load_dataset` function as follows:

```python
movie_rationales = load_dataset("movie_rationales")
```

In the above loaded dataset, it consists of 3 keys which are `train`, `validation`, and `test`, which represent the training, validation, and test sets, respectively. You can then proceed to do whatever your heart desires with the data, explore, extract, transform, train a model, make yourself at home! More info about datasets can be found [here](https://huggingface.co/docs/datasets/index). 