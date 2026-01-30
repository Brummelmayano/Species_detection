from minio import Minio
from minio.error import S3Error
from ..config import settings

minio_client = Minio(
    settings.minio_endpoint,
    access_key=settings.minio_access_key,
    secret_key=settings.minio_secret_key,
    secure=settings.minio_secure
)

def ensure_bucket_exists(bucket_name: str):
    try:
        if not minio_client.bucket_exists(bucket_name):
            minio_client.make_bucket(bucket_name)
    except S3Error as exc:
        print(f"Erreur MinIO: {exc}")
        raise

def upload_file(bucket_name: str, object_name: str, file_path: str, content_type: str = "application/octet-stream"):
    try:
        ensure_bucket_exists(bucket_name)
        minio_client.fput_object(bucket_name, object_name, file_path, content_type=content_type)
        return f"{settings.minio_endpoint}/{bucket_name}/{object_name}"
    except S3Error as exc:
        print(f"Erreur upload MinIO: {exc}")
        raise

def get_file_url(bucket_name: str, object_name: str, expires: int = 3600):
    try:
        return minio_client.presigned_get_object(bucket_name, object_name, expires)
    except S3Error as exc:
        print(f"Erreur génération URL MinIO: {exc}")
        raise

def delete_file(bucket_name: str, object_name: str):
    try:
        minio_client.remove_object(bucket_name, object_name)
    except S3Error as exc:
        print(f"Erreur suppression MinIO: {exc}")
        raise