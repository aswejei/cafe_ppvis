from config.config import CLIENT
from tools.tools import load_class


class ClientHandler:
    _client_class = load_class(CLIENT['class'])

    def __init__(self):
        self._current_client = None

    def create_client(self):
        self._current_client = self._client_class(**CLIENT['init_params'])
