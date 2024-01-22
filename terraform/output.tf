output "ec2_ip" {
    value = aws_instance.ec2_retail.public_ip
}

output "ec2_dns" {
    value = aws_instance.ec2_retail.public_dns
}