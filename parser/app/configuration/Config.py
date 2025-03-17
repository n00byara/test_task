import os
from dotenv import load_dotenv

from configuration import СhangeError

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

dotenv_path = os.path.join(f"{BASE_DIR}/config", ".env")
load_dotenv(dotenv_path)

class Config:
    class _Postgres:
        username: str = None
        userpassword: str = None
        database: str = None
        host: str = None
        port: str = None

        def __init__(self):
            self._username = os.getenv("POSTGRES_USER")
            self._database = os.getenv("POSTGRES_DB")
            self._userpassword = os.getenv("POSTGRES_PASSWORD")
            self._host = os.getenv("POSTGRES_HOST")
            self._port = os.getenv("POSTGRES_PORT")

        @property
        def username(self) -> str:
            return self._username
        
        @username.setter
        def username(self, value):
            raise СhangeError()
        
        @property
        def database(self) -> str:
            return self._database
        
        @database.setter
        def database(self, value):
            raise СhangeError()

        @property
        def userpassword(self) -> str:
            return self._userpassword
        
        @userpassword.setter
        def userpassword(self, value):
            raise СhangeError()
        
        @property
        def host(self) -> str:
            return self._host
        
        @host.setter
        def host(self, value):
            raise СhangeError()
        
        @property
        def port(self) -> str:
            return self._port
        
        @port.setter
        def port(self, value):
            raise СhangeError()
        
    debug: bool = None
    host: str = None
    port: int = None
    log_level: str = None
    postgres: _Postgres = None

    def __init__(self):
        self._debug = os.getenv("DEBUG")
        self._host = os.getenv("HOST")
        self._port = int(os.getenv("PORT"), 0)
        self._log_level = "debug" if self.debug else "info"
        self._postgres = self._Postgres()

    @property
    def debug(self) -> bool:
        return self._debug
    
    @debug.setter
    def debug(self, value):
        raise СhangeError()
    
    @property
    def host(self) -> str:
        return self._host
    
    @host.setter
    def host(self, value):
        raise СhangeError()
    
    @property
    def port(self) -> int:
        return self._port
    
    @port.setter
    def port(self, value):
        raise СhangeError()

    @property
    def log_level(self) -> str:
        return self._log_level
    
    @log_level.setter
    def log_level(self, value):
        raise СhangeError()

    @property
    def postgres(self) -> _Postgres:
        return self._postgres
    
    @postgres.setter
    def postgres(self, value):
        raise СhangeError()