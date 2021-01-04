from storages.backends.s3boto3 import S3Boto3Storage


class ThumbnailsStorage(S3Boto3Storage):
    location = "thumbnails"
