import uvicorn
import server_service


def service_start():
    uvicorn.run(app=server_service.app, host='127.0.0.1', port=8000)


if __name__ == '__main__':
    # server = HttpServer('127.0.0.1', 8000, '128.5.9.79', 8500, 'student-service')
    # server.startServer()
    service_start()
    pass
