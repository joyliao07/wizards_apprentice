from . import app
import boto3, botocore
import os


def upload_file_to_s3(file, filename, extension, bucket_name, acl="public-read"):
    """
    Docs: http://zabana.me/notes/upload-files-amazon-s3-flask.html
    """
    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.environ.get('S3_KEY'),
        aws_secret_access_key=os.environ.get('S3_SECRET_ACCESS_KEY'),
    )

    try:
        print('trying file upload')
        s3.upload_fileobj(
            file,
            bucket_name,
            filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": f'image/{extension}'
            }
        )
        new_path = "{}{}".format('https://s3-us-west-1.amazonaws.com/wizardphoto/', filename)

    except Exception as e:
        print('error msg from upload')
        print("Something Happened: ", e)
        return e

    return new_path
