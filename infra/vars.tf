variable "aws_region" {
  description = "AWS region"
  default     = "us-east-1"  
}

variable "ecr_repository_name" {
  description = "ECR repository name"
}

variable "lambda_function_name" {
  description = "Lambda function name"
}