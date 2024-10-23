As we start to hone in on an exact definition of MLOps, we need to gain a better understanding of what exactly makes up the bigger picture. Let's start by going over the key terms.

* **MLOps Platform** - A specialized software solution and workflow for operationalizing machine learning models. Such platforms have capabilities like data labeling, model monitoring, feature stores, and optimized model serving.
* **Continuous Integration (CI)** - An automated software engineering practice which involves frequent merges of code changes into a share repository, which are then tested for issues to be caught early on.
* **Continuous Delivery (CD)** - A software development concept where teams continuously produce software in short cycles, ensuring that software can be released at any time, this depends on automation like infrastructure as code to replicate testing and production environments.
* **Infrastructure as Code** - Entails the management and configuration of infrastructure as code rather than manual steps, which allows for automated and repeatable management of different development stages and environments.
* **Feature Store** - A centralized repository that stores curated features for machine learning models, this helps in managing data for model creation, storage, and discovery while preventing data drift

Nowadays, you can see development environments being integrated into the cloud, and it is rather rare to find platforms that are locally hosted or in a private data center elsewhere. MLOps is no exception, MLOps has been integrated into the cloud, as such, it is important to understand how the Cloud MLOps landscape looks like, consider the following:

![[Pasted image 20241022142836.png]]

This is what a cloud environment may look like, it's important to be familiar with the key components of such a platform. **Elastic Storage Systems** can provide mount points for entire compute clusters, acting as basically another directory for your artifacts. This goes hand-in-hand with other components such as **Elastic Compute Systems** and **Serverless and Containerized Managed Services** as they can work together. At the bottom, you can see different tools that range from being developer centric to MLE centric tools, such as **Storage Query Tools and Dashboards**which allow for making queries and perform other operations on databases. Moving right, Cloud Development Environments could also integrate 3rd party solutions such as DataBricks or Snowflake for DataOps, specialized databases like Graph Databases or Time-series databases. Thus, when learning about MLOps, it is important to be aware of all the solutions of the cloud environment and be able to make the most out of it.

As cloud environments may differ in the exact features and solutions they implement, it is important to have some kind of metric or measure to describe how developed or **mature** the cloud environment is. To this end, a **MLOps Maturity** scale can be used to describe the maturity or sophistication level of an MLOps implementation in the cloud. As an example, Google uses [3 levels](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) to describe the maturity level:

* Level 0 - No MLOps, everything is done manually and releases are infrequent and not smooth, there is a separation in between the ML and DevOps team
* Level 1 - Implements continuous testing, and hence continuous deliver of the prediction service. This automates the data and model validation, but doesn't result in consistent releases as packaging is still left to the DevOps team. Thus there still is a separation between the ML and DevOps team.
* Level 2 - CI/CD Pipeline Automation, which automates model training, continuous integration and delivery, which means that packaging is automated too, combining concepts from ML automation and DevOps. 

# Continuous Integration (CI)

**Continuous Integration (CI)** is a software development methodology that implements continuous additions and checking the compatibility of said additions with the rest of the system in question. A cornerstone of this concept is the *separation* of the **development** and **production** environments. Though separate, there also needs to be parity between the two environments, if everything is fine on one environment, say development, then everything should work fine in the production environment. To achieve this, the concept of **Infrastructure as Code** is introduced. The role of separate environments ensures that experiments and tests could 

**Infrastructure as Code** describes the ability to configure and setup a coding environment through code, to set up and ensure consistency across different environments. There are different tools and practices used to implement this consistency. Configuration files such as `requirements`, which defines the required packages for a project, as well as **`Makefile`**, which can automate installation, testing, linting, and environment configuration is crucial to the process. Another layer is that of **Virtualization** via **Containerization**, this approach creates a container, which is practically a virtual machine of sorts whose resources adapt to the needs of the application. However, this will be covered later on. 

The contents of a `requirements` file was described in [[Requirements and Dependencies]]. So let's talk about the `Makefile`. Suppose you'd like to have a `Makefile` to automate the installation of your packages, test the code you've written, and apply proper styling via linting. Since these steps could happen at almost every iteration of development, wouldn't it be nice if there was a way to automate this? Enter the humble **`Makefile`**. The structure of a simple `Makefile` looks like:

```Makefile
install:
	pip install -r requirements.txt

test:
	python -m pytest -vv test_hello.py

format:
	black *.py

lint:
	pylint --disable=R,C hello.py

all: install lint test format
```

Given a simple `Makefile` like the above, it performs the following:

* Install the packages defined in `requirements.txt`, labeled `install`
* Test the program by running the `test_hello.py` with `pytest` and passing the `-vv`  flag which defines the level of verbosity, where adding more v's increases the verbosity, labeled `test`
* Format all `.py` files using `black`, a formatting utility to ensure consistency in code appearance and style, labeled `format`
* Check for errors in `hello.py` without actually running the script using the `pylint` tool, labeled `lint`
* Run everything in the order (labeled `all`):
	* `install`
	* `lint`
	* `test`
	* `format`

As mentioned previously, one might want to run these every time they make a change to their code, or add something new. This automated workflow can be taken to the next level with the use of **GitHub Actions**. A high level description of this would be that GitHub actions can be used to automate things based on some specific trigger, usually on *pushing* new code to a repository. To illustrate, let's define such an automated action, which is a configuration placed in the `.github/workflows/` directory, in a `.yml` file.

```yml

name: Python application test with Github Actions

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.8
      uses: actions/setup-python@v1
      with:
        python-version: 3.8
    - name: Install dependencies
      run: |
        make install
    - name: Lint with pylint
      run: |
        make lint
    - name: Test with pytest
      run: |
        make test
    - name: Format code
      run: |
        make format
    
```

We can see that this defines a series of actions to be executed on a git push operation, defined as `on: [push]`. The file defines, among other things, the OS and version it runs on, python version, and defines names for each action. 