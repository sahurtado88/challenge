
variable "region" {
  description = "AWS region to deploy resources to"
  default     = "us-east-1"
}

variable "prefix" {
  description = "Prefix to be assigned to resources."
  default     = "pizza-delivery"
}

variable "db_password" {
  description = "Password for the RDS database instance."
}

variable "environment" {
  description = "Environment"
  type        = string
  default     = "dev"
}