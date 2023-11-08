import json
import uvicorn
from fastapi import FastAPI, APIRouter
from time import sleep
import logging

import consul
from config import Config
from consul_client import ConsulClient, ConsulRegisterServer
import typer

# from register_service import register as register_to_consul

configuration = Config()

shell_app = typer.Typer()

router = APIRouter()

# app = create_app()
SERVICE_NAME: str = 'student-service'
app = FastAPI(title=SERVICE_NAME)

fake_dbs = [
    {'name': 'Bilal', 'class': 'V', 'school_id': 1},
    {'name': 'Ganta', 'class': 'IX', 'school_id': 1},
    {'name': 'Azril', 'class': 'IV', 'school_id': 2}
]


@router.on_event("startup")
def startup_event():
    """
        将向 consul 注册服务添加至 fastapi 的 startup 事件中
        本 fastapi 启动时向 consul 注册服务
    :return:
    """
    # register_to_consul()
    # register_to_consul()
    server = ConsulRegisterServer('127.0.0.1', 8000, '128.5.9.79', 8500, SERVICE_NAME)
    server.register()
    pass


@router.get("/")
async def list_students():
    return fake_dbs


@router.get("/health")
async def health_status():
    return {"status": "healthy"}


@router.get("/name/")
async def get_student(name: str):
    filter_res = filter(lambda x: x.get('name') == name, fake_dbs)
    return list(filter_res)


@router.get("/school/")
async def filter_student_by_school(school_id: int):
    """
        TODO:[*] 23-11-07
        ValueError: [ValueError('dictionary update sequence element #0 has length 3; 2 is required'),
        TypeError('vars() argument must have __dict__ attribute')]
    :param school_id:
    :return:
    """
    filter_res = filter(lambda x: x.get("school_id") == school_id, fake_dbs)
    return list(filter_res)


app.include_router(router)
