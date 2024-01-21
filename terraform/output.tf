output "private_key" {
  description = "EC2 private key."
  value       = tls_private_key.tls_gen_key.private_key_pem
  sensitive   = true
}

output "ec2_ip" {
    value = aws_instance.ec2_retail.public_ip
}