provider "aws" {
  region = var.aws_region
}

resource "aws_ecr_repository" "location_docker" {
  name = var.ecr_repository_name
}

resource "aws_lambda_function" "location_function" {
  function_name = var.lambda_function_name
  image_uri     = "${aws_ecr_repository.location_docker.repository_url}:latest"
  role          = aws_iam_role.lambda_execution_role.arn

  depends_on = [aws_ecr_repository.location_docker]
}

resource "aws_iam_role" "lambda_execution_role" {
  name = "lambda_execution_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_ecr_lifecycle_policy" "fastapi_lambda_lifecycle" {
  repository = aws_ecr_repository.location_function.name
  policy = jsonencode({
    rules = [
      {
        rulePriority = 1
        description  = "Expire old images"
        action = {
          type = "expire"
        }
        filter = {
          tagStatus = "ANY"
        }
        status = "Enabled"
      }
    ]
  })
}
