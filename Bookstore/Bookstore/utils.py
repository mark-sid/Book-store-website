import os
import uuid


def get_upload_path(instanse, filename):
    unique_id = uuid.uuid4()
    ext = filename.split('.')[-1]
    new_filename = f"{unique_id}.{ext}"

    return os.path.join('images/', new_filename)