# Complete these setps before running this program: 
# 1. In terminal, run "pip install awscli", which will install the amazon web services client.
# 2. Again in terminal, run "aws configure", which will ask you for your S3 Access Key, Secret Key, server location
# Once you have done this, your access key and secret key will be saved as a environment variable and will not need to 
# be entered in the code itself.
# Finally, run the following code and check to see if the files are in your s3 bucket, which they should be

import os
import boto3

s3 = boto3.client("s3")

myPath = r"pathToFile" # Replace pathToFile with the path to the folder that you want to upload files from
s3Bucket = "s3BucketName" # Replace s3BucketName with the name of the S3 Bucke where you want the files to go
fileList = os.listdir(myPath)
print(fileList)
for root, dirs, files in os.walk(myPath):
    for file in files:
        filePath = os.path.join(root, file)
        for fileName in fileList:
            s3.upload_file(filePath, s3Bucket, fileName)

print("Files Uploaded")