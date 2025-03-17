from requests import Session

from constants import Constants
from models import UserModel

class Request:
    session: Session
    
    def __init__(self, user: UserModel):
        self.session = self.__get_session(user.email, user.password)

    def __get_session(self, email, password):
        data = {
            "user_login": f"{email}",
            "password": f"{password}",
            "dispatch[auth.login]": "Войти"
        }

        headers = {
            "User-Agent": Constants.USER_AGENT.value
        }

        session = Session()
        session.headers.update(headers)
        session.post(Constants.URL.value, data=data)
        return session
    
    def get_page_from_uri(self, uri):
        return self.session.get(f"{Constants.URL.value}/{uri}/")
    
    def get_page_from_url(self, url):
        return self.session.get(url)