
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.64.0"
    }
  }
    backend "s3" {
  } 
  required_version = "1.8.0"
}

provider "aws" {
  region = var.region
}

data "aws_availability_zones" "available" {}