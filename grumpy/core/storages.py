from django.contrib.staticfiles.storage import StaticFilesStorage
from django.core.files.storage import FileSystemStorage

#########################################
# FileSystem storages (for development) #
#########################################


class LocalStaticStorage(StaticFilesStorage):
    pass


class LocalMediaStorage(FileSystemStorage):
    pass


# EXTEND THIS IF I EVER USE PROPER S3 STORAGE IN DEPLOYMENT
# (INSTEAD OF WHITENOISE)


# class StaticS3Storage(S3Boto3Storage):
#     """
#     Used to manage static files for the web server
#     """
#     location = settings.STATIC_LOCATION
#     default_acl = settings.STATIC_DEFAULT_ACL


# class PublicMediaS3Storage(S3Boto3Storage):
#     """
#     Used to store & serve dynamic media files with no access expiration
#     """
#     location = settings.PUBLIC_MEDIA_LOCATION
#     default_acl = settings.PUBLIC_MEDIA_DEFAULT_ACL
#     file_overwrite = False


# class PrivateMediaS3Storage(S3Boto3Storage):
#     """
#     Used to store & serve dynamic media files using access keys
#     and short-lived expirations to ensure more privacy control
#     """
#     location = settings.PRIVATE_MEDIA_LOCATION
#     default_acl = settings.PRIVATE_MEDIA_DEFAULT_ACL
#     file_overwrite = False
