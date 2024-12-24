#!/usr/bin/env python
# -*- coding: utf-8 -*-
import boto3
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from botocore.exceptions import BotoCoreError, NoCredentialsError

app = FastAPI()

# Инициализация сессии и клиента для Yandex Cloud
session = boto3.session.Session()
s3_client = session.client(
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net',
    aws_access_key_id='your-access-key-id',
    aws_secret_access_key='your-secret-access-key',
    region_name='ru-central1'  # Регион для Yandex Cloud
)

S3_BUCKET_NAME = "hse.wr"

@app.post("/upload")
async def upload_file(file: UploadFile):
    """Загрузка файла в Yandex Cloud Object Storage."""
    try:
        # Загружаем файл в бакет
        s3_client.upload_fileobj(
            file.file, S3_BUCKET_NAME, file.filename,
            ExtraArgs={"ContentType": file.content_type}
        )
        return JSONResponse(content={"status": "success", "filename": file.filename}, status_code=201)
    except (BotoCoreError, NoCredentialsError) as e:
        raise HTTPException(status_code=500, detail=f"Failed to upload file: {str(e)}")

@app.get("/files/{file_name}")
async def get_file(file_name: str):
    """Получение файла из Yandex Cloud Object Storage."""
    try:
        # Получаем файл из бакета
        local_path = f"/tmp/{file_name}"
        s3_client.download_file(S3_BUCKET_NAME, file_name, local_path)
        return FileResponse(local_path, media_type="application/octet-stream", filename=file_name)
    except s3_client.exceptions.NoSuchKey:
        raise HTTPException(status_code=404, detail="File not found")
    except (BotoCoreError, NoCredentialsError) as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve file: {str(e)}")

@app.get("/list_files")
async def list_files():
    """Получить список всех объектов в бакете Yandex Cloud."""
    try:
        # Список всех объектов в бакете
        response = s3_client.list_objects(Bucket=S3_BUCKET_NAME)
        if 'Contents' in response:
            return JSONResponse(content={"files": [obj['Key'] for obj in response['Contents']]}, status_code=200)
        else:
            return JSONResponse(content={"files": []}, status_code=200)
    except (BotoCoreError, NoCredentialsError) as e:
        raise HTTPException(status_code=500, detail=f"Failed to list files: {str(e)}")

@app.delete("/delete_file/{file_name}")
async def delete_file(file_name: str):
    """Удаление файла из Yandex Cloud Object Storage."""
    try:
        # Удаление объекта
        s3_client.delete_objects(
            Bucket=S3_BUCKET_NAME,
            Delete={'Objects': [{'Key': file_name}]}
        )
        return JSONResponse(content={"status": "success", "filename": file_name}, status_code=200)
    except (BotoCoreError, NoCredentialsError) as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete file: {str(e)}")