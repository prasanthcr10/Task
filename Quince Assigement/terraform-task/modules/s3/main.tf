########################
# Bucket creation
########################
resource "aws_s3_bucket" "my_protected_bucket" {
  bucket = var.bucket_name
}

