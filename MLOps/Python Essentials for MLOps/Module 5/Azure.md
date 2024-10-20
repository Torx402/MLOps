Azure CLI can allow to install extensions that can communicate via packages installed via pip to communicate with Azure ML Studio. To access ML studio, you need an account and to use its various credentials to be able to connect to it using the azureml package in python. The first step involves establishing a connection, which can be done using a service principal that can be set in the environment variables or if you are using codespaces, you can add the secrets there. Before continuing, feel free to take a look at [[Azure/MLStudio/Introduction|Introduction]] to learn about *workspaces* and *compute instances*.

```python
import os

# required
subscription_id = os.environ("SUBSCRIPTION_ID")
tenant_id = os.environ("TENANT_ID")
service_principal_id = os.environ("AZURE_SERVICE_PRINCIPAL_APPID")
service_principal_password = os.environ("AZURE_SERVICE_PRINCIPAL_PASSWORD")

# optional
resource_group = os.getenv("RESOURCE_GROUP", default="demo-try-azureml")
workspace_name = os.getenv("WORKSPACE_NAME", default="demo-try-azureml")
workspace_region = os.getenv("WORKSPACE_REGION", default="eastus2")
```

The above essentially defines the parameters that will be used to authenticate using the Service Principal. Next, we write the following:

```python
from azureml.core import workspaces
from azureml.core.authentication import ServicePrincipalAuthentication

service_principal = ServicePrincipalAuthentication(
					tenant_id = tenant_id,
					service_principal_id = service_principal_id,
					service_principal_password = service_principal_password
)
```

The above stores the service principal authentication in a variable called service_principal.

Afterwards, we define a workspace, which consists of the information we previously defined, and looks like:

```python
ws = Workspace.create(name = workspace_name,
					 subscription_id = subscription_id,
					 resource_group = resource_group,
					 location = workspace_region, 
					 auth = service_principal,
					 create_resource_group = True,
					 exist_ok = True)
ws.get_details() # prints details of workspace

ws.write_config() # writes config to a file in notebook library

```

Next, we will create compute cluster(s) and assign them to the workspace, this first requires the definition(s) of compute cluster(s), and then requesting their creation and assignment to a workspace, which is as follows:

```python
from azureml.core.compute import ComputeTarget, AmlCompute

# define aml compute target(s)
amlcomputes = {
	"cpu-cluster":{
		"vm_size": "STANDARD_DS3_V2",
		"min_nodes": 0,
		"max_nodes": 3,
		"idle_seconds_before_scaledown": 240,
	}
}

# create aml compute target(s)
for ct_name in amlcomputes:
	if ct_name not in ws.compute_targets:
		compute_config = AmlCompute.provisioning_configuration(**amlcomputes[ct_name])
		ct = ComputeTarget.create(ws, ct_name, compute_config)
		ct.wait_for_completion(show_output=True)
```

There are few things to note here:

* The definition is a dictionary which can define multiple computer targets, in this case, only one is defined, which is `cpu-cluster`
	* The compute target in question consists of various attributes, more info about this can be found [here](https://learn.microsoft.com/en-us/azure/machine-learning/concept-compute-target?view=azureml-api-2#azure-machine-learning-compute-managed).
* A for loop iterates over each compute target definition and checks whether the workspace we are interested in creating compute clusters for already has said compute target
	* if it does not, then it creates a configuration using `AmlCompute`'s `provisioning_configuration()` method, passing the various attributes of the compute target `ct_name` (`cpu-cluster` in this case) as keyword arguments. 
	* Afterwards, the generated configuration is passed to `ComputeTarget`'s `create()` method, passing in the workspace, compute target name, and its configuration

Following these steps, a compute cluster will be created and associated with a given workspace.

The code you ran above should have its effects visible in the Azure ML Studio portal, you should be able to see the workspace and compute instance you created there. 

At this point, you may start doing whatever you intended to do with that notebook, with all the processing being done on Azure. After you are done, you can then move on to stopping the workspace by deleting the workspace. Using the AzureML Python SDK, this is as follows:

```python
ws.delete(delete_dependant_resources=True, no_wait=False)
```

This will delete the workspace and all resources associated with it including the compute clusters. This is very important to do once you are done with your work since it can accumulate huge costs. 