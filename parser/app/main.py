from uvicorn import run

from app import app
from configuration import config

if __name__ == "__main__":
    run(
        "main:app",
        host=config.host,
        port=config.port,
        log_level=config.log_level,
        reload=config.debug
    )