# REQUIREMENTS

Ensure you have the following installed in advance of the stream:

Terraform: https://developer.hashicorp.com/terra...
Docker: https://docs.docker.com/engine/install/
Kubernetes CLI (kubectl): https://kubernetes.io/docs/tasks/tool...
Helm: https://helm.sh/docs/intro/quickstart...
AWS account: https://aws.amazon.com/free/
GIT



# Provision Infraestructure

first we  want to create the backend to store our tf.state for this we are use the files that are in S3backend
to execute this terraform files you need to go to teh folder S3Backend/ in this folder you need to creat a 
create a .tfvar to configure the values on the variables according to the needs and environment

In this example:
```
# prod.tfvars
environment = "dev"
iam_user    = "terraform-dev"
bucket_name = "sterraform-remote-backend-s3-sahr2024-dev"
table_name  = "terraform_state_locks-dev"
region      = "us-east-1"
```

The IAM user terraform is created.
An S3 bucket named sterraform-remote-backend-s3-sahr2024 is provisioned to store the Terraform state files.
A DynamoDB table named terraform_state_locks is created for state locking in the region us-east-1 .

# How to Apply the Module

## Initialize the Terraform Working Directory:

Navigate to your Terraform project directory and run:
```
terraform init
```

## Plan the Terraform Deployment:

Review the changes that Terraform will make to your infrastructure by running terraform plan in this case we use terraform.tfvars to use these variables in case you create another file change the name of the file in the command:
```
terraform plan --var-file prod.tfvars
```
## Apply the Terraform Configuration:

Execute the plan and deploy the resources by running terraform apply --var-file namefile.tfvars in this case we use terraform.tfvars to use these variables in case you create another file change the name of the file in the command::
```
terraform apply --var-file prod.tfvars -auto-approve
```

## Manage the State:

After the resources are created, Terraform will store its state file in the S3 bucket created by this module. The DynamoDB table will be used to lock the state during operations to ensure no concurrent modifications occur.


# Notes
## Resource Deletion Protection:

Both the S3 bucket and DynamoDB table have prevent_destroy lifecycle rules enabled to prevent accidental deletion. To delete these resources, you must first remove the prevent_destroy attribute from the configuration.

## AWS Credentials:

Ensure that the AWS credentials configured in your environment have the necessary permissions to create IAM users, S3 buckets, and DynamoDB tables.

This module is essential for managing Terraform state files securely and ensuring consistency during Terraform operations by using AWS best practices.

Know you have configured your backend its tiem to create the infraestructure in AWS 

This Terraform project allows you to create a basic AWS infrastructure that includes:

A VPC with public and private subnets.
Route tables for each subnet.
A security group to allow traffic on ports 80 and 443.
An Elastic Load Balancer (ELB) listening on ports 80 and 443.
A hosted zone in Route 53 and a CNAME record pointing to the ELB.
The project is designed to be modular, making it easy to create and manage different environments (development, staging, production).

Each module and environment has a variables.tf file where you can configure the specific values for your infrastructure.

This project uses the partial configuration of the backend so you can deploy the infrastructure in different environments for this you need to edit or create in the folder state_configuration the values of bucket, key, dynamotable and region where you have your bucket and dynamo.

Example partial configuration in state_configuration/dev-s3-state.hcl
```
bucket = "sterraform-remote-backend-s3-sahr2024-dev"
key = "dev/terraform.tfstate"
dynamodb_table = "terraform_state_locks-dev"
region = "us-east-1"
```