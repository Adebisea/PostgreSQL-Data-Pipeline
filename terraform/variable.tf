variable "vpc_id" {
    type = string
    default = "vpc-072a65c15380540d9"
}

variable "vpc_cidr_block" {
  type = string
  default = "0.0.0.0/0"
}

# Ec2 instance type
variable "instance_type" {
    type    = string
    default = "t3.micro"
}