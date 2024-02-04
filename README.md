# PostgreSQL-Data-Pipeline

## Description
This project demonstrates the process of transferring CSV data from a local environment to a PostgreSQL server deployed on Docker, which is hosted on an EC2 instance.
The demonstration includes utilizing two distinct Python clients, namely psycopg2 and sqlalchemy, showcasing alternative approaches for seamless data migration to a PostgreSQL database.

![Alt text](https://github.com/Adebisea/PostgreSQL-Data-Pipeline/blob/f3e7bfbc09c81fdb9faa100a48820859ea62d0f0/etl_process.png)


## Getting Started

### Prerequisites
- Terraform
- Ansible
- AWS Account with Access Key and Secret Key

### Configuration
Create config file for access to aws
  - Create a config.txt file in the root of the project.
  - Add the following content to config.txt:
  ```
  [default]
  AWS_ACCESS_KEY_ID="your_aws_access_key"
  AWS_SECRET_ACCESS_KEY="your_aws_secret_key"
  ```
  Replace "your_aws_access_key" and "your_aws_secret_key" with your actual AWS credentials.


### Usage

1. Create a key pair on the aws console and name it `pgmig.pem`
2. To deploy the infrastructure, navigate to the Terraform directory and run:
    ```
    terraform init
    ```
    This command initializes your working directory, downloading the necessary providers and modules.
    
    ```
    terraform apply --auto-approve
    ```
    The terraform apply command deploys the infrastructure
    
Note: The terraform apply command after execution will output the newly created ec2 instance ip address, copy and keep it in a safe place, you'll need it in the next step.

3. Run Ansible playbook to automate dependencies installation
    - Navigate to the ansble directory and edit the inventory.ini file.
    - replace <instance_ip> in `ansible_host=<instance_ip>` with the instance ip gotten from step 2
    - replace <keypair_file_path> in `ansible_ssh_private_key_file=<keypair_file_path>` with the path to the keypair created in step 1
    - Now run;
      
        ```
        ansible-playbook -i inventory.ini playbook.yml
        ```
        
4. ssh into the ec2 instance
   - run;
      ```
      ssh -i <keypair_file_path> ubuntu@<instance_ip>
      ```
      replace <keypair_file_path> and <instance_ip> with the appropriate values

5. Migrate csv files to Postgres db
  - Navigate to PostgreSQL-Data-Pipeline directory on the instance.
  - Create a .env file in the root of the folder
      - Add the following content to file:
        ```
            host= 'localhost'
            port= 5432
            dbname='preferred dbname'
            user= 'postgres'
            password='preferred password'
        ```
- To connect and migrate using the pyscopg2 client, run;
  ```
     python3 pyscog2_pipeline.py
  ```
Note: This command will create an onlineretail table in the postgresdb and migrate the `onlineretail.csv`

- To connect and migrate using the sqlalchemy client, run;
  
  ```
     python3 sqlalchemy_pipeline.py
  ```
  
Note: This command will create two tables(greentrips and taxizone) and migrate the `green_tripdata_2019-09.csv` and `taxi+_zone_lookup.csv` to their respective tables

### Clean up

    To clean up and destroy the infrastructure, Navigate to the terraform directory and run:
    ```
    terraform destroy --auto-approve
    ```
