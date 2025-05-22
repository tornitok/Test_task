from api.http_client import HTTPClient


class Airports(HTTPClient):

    def __init__(self, session, endpoint):
        super().__init__(session, endpoint)
        self.headers = {
            'Content-Type': 'application/json'
        }

    def get_airports(self):
        response = self.get(self.endpoint, headers=self.headers)
        return response
