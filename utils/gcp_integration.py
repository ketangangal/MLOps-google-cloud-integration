from google.cloud import storage


def create_bucket(config=None, storage_client=storage.Client()):
    try:
        bucket = storage_client.bucket(config['param']['bucket_name'])
        bucket.storage_class = config['param']['storage_class']
        bucket.location = config['param']['location']
        bucket = storage_client.create_bucket(bucket)
        return f"Bucket {config['param']['bucket_name']} Created. Status : {bucket}"
    except Exception as e:
        return f"An Error Occurred While creating bucket : {e.__str__()}"


def upload_to_bucket(config=None, storage_client=storage.Client()):
    try:
        bucket = storage_client.get_bucket(config['param']['bucket_name'])
        blob = bucket.blob(config['param']['blob_name'])
        blob.upload_from_filename(config['param']['file_path'])
        return f"Successfully uploaded Run : {config['param']['blob_name']}"
    except Exception as e:
        return f"An Error Occurred While Uploading to the bucket : {e.__str__()}"

