import boto3

def list_public_s3_buckets():
    # Create an S3 client
    s3_client = boto3.client('s3')

    # List all S3 buckets in the account
    response = s3_client.list_buckets()

    # Iterate through each bucket
    for bucket in response['Buckets']:
        bucket_name = bucket['Name']

        # Check if the bucket is publicly accessible
        try:
            bucket_acl = s3_client.get_bucket_acl(Bucket=bucket_name)
            for grant in bucket_acl['Grants']:
                if 'URI' in grant['Grantee'] and grant['Grantee']['URI'] == 'http://acs.amazonaws.com/groups/global/AllUsers':
                    print(f"Public S3 bucket: {bucket_name}")
                    break
        except Exception as e:
            # Handle exceptions, e.g., if the bucket ACL is private
            print(f"Error checking bucket {bucket_name}: {str(e)}")

if __name__ == "__main__":
    list_public_s3_buckets()
