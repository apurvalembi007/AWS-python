__author__ = 'Apurvalembi'

# aws_access_key_id = "AKIAJQQSASDTS536M6FQ"
# aws_secret_access_key = "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"

from boto.s3.connection import S3Connection

conn = S3Connection("AKIAJQQSASDTS536M6FQ","Ww4RT70UyiHfCObGmGd4kJPJYjhM5wJeeTtHbmOm")
print("  connected to aws \n ")




file = "a.txt"
bucket = conn.get_bucket("ablembi") # set the bucket name

# # creating a new key
def upload():

    key = bucket.new_key(file) #create new key// create a file
    key.set_contents_from_filename(file) # set values to write in the file created

#caluate time to upload
from time import time

start_time=time()
upload()
end_time=time()
print("uploaded file")
print("time to upload: {time} seconds". format(time=end_time-start_time))