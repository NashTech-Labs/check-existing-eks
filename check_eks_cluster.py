import boto3
import botocore
 
def check_eks_cluster(eks_name, region):
    try:
        access_key_secret = "<Access-key>"
        secret_access_key_secret = "<secret-Access-key>"
 
 # Initialize the Boto3 EKS client with retrieved AWS credentials
        eks_client = boto3.client('eks', region_name=region, access_key_secret=aws_access_key, secret_access_key_secret=aws_secret_access_key)
 
        # Describe the EKS cluster
        response = eks_client.describe_cluster(name=eks_name)
 
        # If the cluster is found, return True
        return True
 
    except botocore.exceptions.ClientError as e:
        error_code = e.response.get("Error", {}).get("Code")
        if error_code == "ResourceNotFoundException":
            # If the cluster is not found, return False
            return False
        else:
            # Handle other exceptions if needed
            print(f"Error: {e}")
            return False
 
# Example usage
eks_name_to_check = "<enter-eks-name>"
region_to_check = "<enter-the-region>"
 
cluster_exists = check_eks_cluster(eks_name_to_check, region_to_check)
 
if cluster_exists:
    print(f"EKS cluster '{eks_name_to_check}' exists in region '{region_to_check}'.")
else:
    print(f"EKS cluster '{eks_name_to_check}' does not exist in region '{region_to_check}'.")
