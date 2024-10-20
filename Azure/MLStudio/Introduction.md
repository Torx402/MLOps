Let's start by introducing the first basic resources you need to get started with Azure ML Studio, the **Workspace** and the **Computer Instance**.

# Workspace

A workspace refers to an environment that stores all files, configurations, inputs, outputs, logs, compute instances, etc. related to what you are doing. For example, you may create a workspace dedicated to some work you are doing, some analysis or what have you, this workspace will be where you have your files and other *artifacts*, which refers to any of the above mentioned in a specific workspace. To create a workspace, you may do so via the UI in Azure MLStudio, which you can find [here](https://learn.microsoft.com/en-us/azure/machine-learning/quickstart-create-resources?view=azureml-api-2&wt.mc_id=acom_machinelearningmlcreateworkspace_webpage_gdc#create-the-workspace). If you would like to create a workspace using the Python library and Azure CLI, please refer to [[Azure]]. 

A workspace has various required and optional attributes which need to be defined based on the usage scenario. The attributes are:

* Name
	* This refers to a name that will be used to identify your workspace, hence it must be unique across the resource group
* Friendly Name
	* A name that isn't restricted by Azure naming rules, spaces and special characters are allowed
* Hub
	* A hub allows you to group related workspaces together and share resources across them.

If no hub is provided, then the following must be provided:

* Subscription
	* Select the Azure Subscription you'd like to use
* Resource Group
	* Use an existing resource group or enter a name to define a new one
* Region
	* Specify the region closest to the users

# Compute Instance

A computer instance refers to a pre-configured cloud computing resource which will handle the processing of your notebooks. There various types of compute instances which you can choose from and this depends on your specific application. This can be done in the Azure ML Studio portal, or via code, which you can also learn about, alongside stopping resources in [[Azure]].