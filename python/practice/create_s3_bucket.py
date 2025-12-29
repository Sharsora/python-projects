import boto3

def get_connections():
    return boto3.client("s3")

def show_buckets(s3_client):
    responce = s3_client.list_buckets()

    for bucket in responce["Buckets"]:
        print(bucket["Name"])

def create_bucket(s3_client, bucket_name):
    response = s3_client.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
        'LocationConstraint': 'eu-north-1',
    },)
    if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
        print("Bucket created successfully")
    else:
        print("Error occure while creating bucket")    

s3 = get_connections()
show_buckets(s3)
create_bucket(s3,"created-bucket-using-python-2")
