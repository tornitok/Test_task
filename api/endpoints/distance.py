from api.http_client import HTTPClient


class Distance(HTTPClient):

    def __init__(self, session, endpoint, distance_data):
        super().__init__(session, endpoint)
        self.distance_data = distance_data
        self.headers = {
            'Content-Type': 'application/json'
        }

    def get_distance(self):
        response = self.get(self.endpoint, headers=self.headers)
        return response

    def post_distance(self):
        response = self.post(self.endpoint, json=self.distance_data, headers=self.headers)
        return response
