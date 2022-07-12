# Complete these setps before running this program: 
# 1. In terminal, run "pip install awscli", which will install the amazon web services client.
# 2. Again in terminal, run "aws configure", which will ask you for your S3 Access Key, Secret Key, server location
# Once you have done this, your access key and secret key will be saved as a environment variable and will not need to 
# be entered in the code itself.
# Finally, run the following code and check to see if the files are in your s3 bucket, which they should be

from fileinput import filename
import os
import boto3
import sys
import requests
import re

url = sys.argv[1]

s3 = boto3.client("s3")
bucketName = "bucketName" # Inpyt your S3 Bucket Name here

download = requests.get(url)
fileName = ''
if "Content-Disposition" in download.headers.keys():
    fileName = re.findall("filename=(.+)", download.headers["Content-Disposition"])[0]
else:
    fileName = url.split("/")[-1]

with open(fileName, "wb") as f:
    f.write(download.content)

s3.upload_file(fileName, bucketName, fileName)
os.remove(fileName)
print("Uploaded " +  fileName + " to S3 Bucket " + bucketName)











