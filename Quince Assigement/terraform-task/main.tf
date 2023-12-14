 module "vpc" {

   source                       = "./modules/vpc"
   name                         = var.name
   env                          = var.env
   vpc_cidr_block               = var.vpc_cidr_block
   private_subnet_cidr_block_1a = var.private_subnet_cidr_block_1a
   private_subnet_cidr_block_1b = var.private_subnet_cidr_block_1b
   
   public_subnet_cidr_block_1a  = var.public_subnet_cidr_block_1a
   public_subnet_cidr_block_1b  = var.public_subnet_cidr_block_1b
   
 }	

 module "s3" {


 source     =  "./modules/s3"

 }

 module "iam" {
  source = "./modules/iam"
}


 module "security-group" {
  source = "./modules/security-group"
}

 module "ec2-instance" {
  source = "./modules/ec2-instance"
  subnet_id = "${var.vpc.outpout.aws_subnet.public_subnet_1b.id}"
  
}

