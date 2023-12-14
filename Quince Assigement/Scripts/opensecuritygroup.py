import boto3

def find_open_security_groups():
    # Create an EC2 client
    ec2_client = boto3.client('ec2', region_name='ap-south-1')

    # Get a list of all regions
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

    for region in regions:
        print(f"Checking region: {region}")

        # Create an EC2 resource in the specified region
        ec2_resource = boto3.resource('ec2', region_name=region)

        # Get all security groups in the region
        security_groups = ec2_resource.security_groups.all()

        for security_group in security_groups:
            group_id = security_group.id

            # Check if any inbound rule allows all traffic
            for ingress_rule in security_group.ip_permissions:
                for ip_range in ingress_rule['IpRanges']:
                    if ip_range['CidrIp'] == '0.0.0.0/0':
                        print(f"Open Security Group found in region {region} - Group ID: {group_id}")
                        break

if __name__ == "__main__":
    find_open_security_groups()
