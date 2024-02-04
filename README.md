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
1. Create config file for access to aws
  - Create a config.txt file in the root of the project.
  - Add the following content to config.txt:
  ```
  [default]
  AWS_ACCESS_KEY_ID="your_aws_access_key"
  AWS_SECRET_ACCESS_KEY="your_aws_secret_key"
  ```
  Replace "your_aws_access_key" and "your_aws_secret_key" with your actual AWS credentials.

2. Create a .env file
  - Create a .env file in the root of the project.
  - Add the following content to file:
    ```
        host= 'localhost'
        port= 5432
        dbname='preferred dbname'
        user= 'postgres'
        password='preferred password'
    ```

### Usage
1. To deploy the infrastructure, navigate to the Terraform directory and run:
    ```
    terraform init
    ```
    This command initializes your working directory, downloading the necessary providers and modules.
    
    ```
    terraform apply --auto-approve
    ```
    The terraform apply command deploys the infrastructure
    
    To clean up and destroy the infrastructure, run:
    ```
    terraform destroy --auto-approve
    ```
