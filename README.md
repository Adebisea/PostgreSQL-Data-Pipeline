# PostgreSQL-Data-Pipeline

## Description
This project demonstrates the process of transferring CSV data from a local environment to a PostgreSQL server deployed on Docker, which is hosted on an EC2 instance.
The demonstration includes utilizing two distinct Python clients, namely psycopg2 and sqlalchemy, showcasing alternative approaches for seamless data migration to a PostgreSQL database.

## Getting Started

### Prerequisites
- Terraform
- Ansible
- AWS Account with Access Key and Secret Key

### Configurations
- Create a config.txt file in the root of the project.
- Add the following content to config.txt:
```
[default]
AWS_ACCESS_KEY_ID="your_aws_access_key"
AWS_SECRET_ACCESS_KEY="your_aws_secret_key"
```
Replace "your_aws_access_key" and "your_aws_secret_key" with your actual AWS credentials.

### Initializing Terraform
Run the following command in the terminal to initialize Terraform:
```
terraform init
```
This command initializes your working directory, downloading the necessary providers and modules.

### Usage
To deploy the VPC infrastructure, navigate to the Terraform directory and run:
```
terraform apply --auto-approve
```
To clean up and destroy the infrastructure, run:
```
terraform destroy --auto-approve
```
