import posixpath

from storages.backends.s3boto3 import S3Boto3Storage

from .uuid import uuid


def upload_to_factory(prefix):
    """
    An upload path generator that uses compact UUIDs for filenames.
    """

    def get_upload_path(instance, filename):
        name, ext = posixpath.splitext(filename)
        return posixpath.join(prefix, uuid() + ext)

    return get_upload_path


def upload_to(instance, filename):
    """
    An upload path generator that generates an upload prefix based
    on the instance model name, and uses a compact UUID for the filename.
    """
    opts = instance._meta
    return upload_to_factory(
        posixpath.join(opts.app_label, instance.__class__.__name__.lower(),)
    )(instance, filename)


class StaticRootS3Boto3Storage(S3Boto3Storage):
    location = "static"
    default_acl = "public-read"


class MediaRootS3Boto3Storage(S3Boto3Storage):
    location = "media"
    file_overwrite = False
