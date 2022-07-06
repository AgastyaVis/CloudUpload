# Complete these setps before running this program: 
# 1. In terminal, run "pip install awscli", which will install the amazon web services client.
# 2. Again in terminal, run "aws configure", which will ask you for your S3 Access Key, Secret Key, server location
# Once you have done this, your access key and secret key will be saved as a environment variable and will not need to 
# be entered in the code itself.
# Finally, run the following code and check to see if the files are in your s3 bucket, which they should be

import os
import boto3
import time
from pathlib import Path
import shutil

s3 = boto3.client("s3")

myPath = r"/Path/To/File/Folder" # Input the path to the folder that you want to upload files from
s3Bucket = "BucketName" # Input the name of the S3 Bucke where you want the files to go
splitPath = os.path.split(myPath)
pathTail = splitPath[1]

startTime = time.time()

fileList = os.listdir(myPath)

print("Beginning upload to Amazon S3 Bucket %s " % (s3Bucket))
for path, subdirs, files in os.walk(myPath):
    for file in files:
        destPath = path.replace(myPath,"")
        s3UploadPath = os.path.normpath(pathTail + '/' + destPath + '/' + file)
        filePath = os.path.join(path, file)
        s3.upload_file(filePath, s3Bucket, s3UploadPath)
shutil.rmtree(pathTail) # Deletes the folder/file/folders that have been uploaded to s3
        

endTime = time.time()

print("Files Uploaded")
print("Time taken for program to run = ", (endTime - startTime))
