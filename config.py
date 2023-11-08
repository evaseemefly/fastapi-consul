import socket
import os


class Config:
    port = os.getenv('PORT', 8000)
    address = os.getenv('ADDRESS') or 'student_service'
    # CONSUL_HOST = os.getenv('CONSUL_HOST') or 'consul'
    CONSUL_HOST = '128.5.9.79'
    CONSUL_PORT = os.getenv('CONSUL_PORT') or 8500
    MAX_TRY_COUNT = 5  # 反复请求总数
