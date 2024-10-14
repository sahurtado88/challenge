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