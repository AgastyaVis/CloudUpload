# This program is only 3 lines of code, but for it to function, there are a
# few things that need to be completed. 
# 1. In terminal, run "pip install awscli", which will install the amazon web services client.
# 2. Again in terminal, run "aws configure", which will ask you for your S3 Access Key, Secret Key, server location
# Once you have done this, your access key and secret key will be saved as a environment variable and will not need to 
# be entered in the code itself.
# Finally, install boto3 for python and run the following code
import boto3

s3 = boto3.client('s3')

print("Enter the local file name(including file type, like .txt, .py, etc.): ")
localFile = str(input())
print("Enter the name of the S3 Bucket you want to upload the file to: ")
bucketName = str(input())
print("Enter the name which the file should be saved as in the bucket (including file type, such as .txt, .py, etc.): ")
finalName = str(input())
s3.upload_file(localFile, bucketName, finalName)
