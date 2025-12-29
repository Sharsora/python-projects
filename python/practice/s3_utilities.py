import boto3

s3_client = boto3.client("s3")
responce = s3_client.list_buckets()

for bucket in responce["Buckets"]:
    print(bucket["Name"])
