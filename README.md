# Running the EKS Cluster Existence Checker Script
 
This Python script checks the existence of an Amazon Elastic Kubernetes Service (EKS) cluster using both AWS SDK for Python (Boto3) and Azure SDK for Python.
 
## Prerequisites
 
Before running the script, ensure you have the following:
 
- Python installed on your machine.
- AWS CLI configured with appropriate credentials (if checking AWS resources).
- Azure CLI configured with appropriate credentials (if checking Azure resources).
 
## Setup
 
1. **Install Dependencies**: Install the required Python packages using pip:
 
    ```bash
    pip install boto3 azure-identity azure-keyvault-secrets botocore
    ```
 
2. **Configure Azure Key Vault**: If you are using Azure credentials, ensure you have a Key Vault set up with secrets for accessing Azure resources. Replace `"Access-key"` and `"secret-Access-key"` in the script with the appropriate secret names from your Azure Key Vault.
 
3. **Update Script**: Open the provided Python script (`check_eks_cluster.py`) in a text editor and update the following variables:
 
    - `eks_name_to_check`: Replace `<enter eks name>` with the name of the EKS cluster you want to check.
    - `region_to_check`: Replace `<enter the region>` with the AWS region where the EKS cluster is located.
 
## Running the Script
 
1. **Execute Script**: Run the Python script from the command line:
 
    ```bash
    python check_eks_cluster.py
    ```
 
2. **View Output**: The script will output whether the specified EKS cluster exists in the specified region. If the cluster is found, it will display a success message; otherwise, it will display a failure message.
 
## Notes
 
- Ensure that your AWS and Azure credentials have sufficient permissions to access the resources being checked.
- Make sure the AWS CLI and Azure CLI are properly configured with the appropriate credentials.
- Customize the script or add error handling as needed for your specific use case.
 
---
 
Feel free to copy and paste this Markdown text into your README.md file and customize it further if needed.
