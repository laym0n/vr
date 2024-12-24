#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import JSONResponse, FileResponse
app = FastAPI(
    title="Storage",
    root_path="/api-gateway/storage-service",
    swagger_ui_parameters={"openapiUrl": "/api-gateway/storage-service/openapi.json"}
)



# Директория для локального хранения файлов
LOCAL_STORAGE_DIR = "./storage"
os.makedirs(LOCAL_STORAGE_DIR, exist_ok=True)  # Убедимся, что директория существует

@app.post("/upload")
async def upload_file(file: UploadFile):
    """Загрузка файла в локальное хранилище."""
    try:
        file_path = os.path.join(LOCAL_STORAGE_DIR, file.filename)
        
        # Сохраняем файл локально
        with open(file_path, "wb") as f:
            while contents := file.file.read(1024):
                f.write(contents)

        return JSONResponse(content={"status": "success", "filename": file.filename}, status_code=201)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to upload file: {str(e)}")

@app.get("/files/{file_name}")
async def get_file(file_name: str):
    """Получение файла из локального хранилища."""
    try:
        file_path = os.path.join(LOCAL_STORAGE_DIR, file_name)

        # Проверяем, существует ли файл
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="File not found")

        return FileResponse(file_path, media_type="application/octet-stream", filename=file_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve file: {str(e)}")

@app.get("/list_files")
async def list_files():
    """Получить список всех файлов в локальном хранилище."""
    try:
        files = os.listdir(LOCAL_STORAGE_DIR)
        return JSONResponse(content={"files": files}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to list files: {str(e)}")

@app.delete("/delete_file/{file_name}")
async def delete_file(file_name: str):
    """Удаление файла из локального хранилища."""
    try:
        file_path = os.path.join(LOCAL_STORAGE_DIR, file_name)

        # Проверяем, существует ли файл
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="File not found")

        # Удаляем файл
        os.remove(file_path)
        return JSONResponse(content={"status": "success", "filename": file_name}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete file: {str(e)}")
