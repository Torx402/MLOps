# Introduction

Before we define what exactly MLOps is, we first need to get a grasp on what DevOps is, as MLOps can more or less be treated as an extension to the latter. **DevOps** is a set of methods, approaches and practices to *automate* and *standardize* operations that are involved with software development and maintenance. The goal is to *minimize* friction and *promote* smoother integration with other units. With that out of the way, let's define some keywords:

* **MLOps** - A combination of DevOps-like methods and ML best practices focused on deployment and operation of ML Models into production systems
* **CI/CD** - Continuous Integration and Continuous Delivery, which are key practices in DevOps workflows. CI involves automated testing and validation of incrementally-built software while CD takes care of continuous automatic updates to existing environments like production. 
* **Maturity Model** - Consists of levels, 4-5 typically, that describe the state of an MLOps solution, described using words like *manual*, *siloed*, *unreliable*, or *scalable*, *autonomous*, *resilient*, etc.
* **DataOps** - An adaptation of DevOps to data oriented workloads which makes use of the automation oriented approach and applies it to practices such as aggregation, transformation, storage, analysis, among others.
* **Feature Store** - A hub for managing features to manage, store, and serve ML features for model building and retraining, optimizing pipelines and reuse.

With that being said, it is important to define some *motivation* for why we even need MLOps to begin with, and the short answer to that is to increase the *clarity* of the pursued objective, and *standardize* the practices used to reach said objective.  For a long time now, the lack of specific practices used by data scientists lead to inefficiency in delivering results. While exploration is an inherent aspect, delivering results is ultimately the goal to be achieved in a production environment. To this end, MLOps delivers on this by standardizing many of the decision making, such that what is left to be done is to be aware of the best practices to implement. 

To better understand MLOps, Noah Gift, an instructor of the course and author of [Practical MLOps](https://www.oreilly.com/library/view/practical-mlops/9781098103002/) breaks MLOps down to 4 equivalent parts

* DevOps
* Data
* Models
* Business

The idea here is that choosing a single approach isn't practical enough to deliver a solution, while one may have a data-centric approach, which sees the key to delivering optimal ML solutions as being in how the data is modified, or a model-centric approach, which prioritizes developing more sophisticated models as the solution, the reality is that an optimal solution *combines* different approaches. 

In addition, the data and model aren't the only pieces of the puzzle, concepts in automation and standardization found in DevOps are instrumental to this process. Equally as important is understanding the business goal, or value, of a project, does it even make sense to choose such an approach to, for example, increase engagement with a social media platform, or increase watch-time on a streaming platform, etc.

# DevOps

DevOps is more of an umbrella term rather than a rigid label. It composes of three main parts:

* Software Engineering Best Practices
	* Refers to the best practices implemented in the software engineering field, an example of this is containerization.
* Culture
	* Describes the culture of continuous improvement, *Kaizen*, a japanese phrase used to refer to this. Ultimately, this introduces the idea of continuously improving the approach taken to reach some solution, which in our case, are ML solutions.
* Automation
	* At the core of automation is CI/CD, which describes the continuous addition of features to some system, and validating its compatibility with the already existing parts of the system.

# DataOps

DataOps builds off of the foundations of DevOps: Automation and continuous incremental additions to a system, infused with the culture of collaboration and breaking down problems into smaller chunks. This approach is applied to data systems.

