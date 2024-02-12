import json

from googleapiclient.discovery import build
import isodate
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()
api_key: str = os.getenv('YT_API_KEY')
moscowpython = []
class Channel:
    """Класс для ютуб-канала"""
    __youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = self.__youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        pprint(json.dumps(self.channel, indent=2, ensure_ascii=False))

    def to_json(self, file_name: str) -> None:
        data = json.dumps(self.channel)
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(data)


    @property
    def channel_id(self):
        return self.__channel_id

    @property
    def title(self):
        # print(self.channel)
        return self.channel['items'][0]['snippet']['title']

    @property
    def video_count(self):
        return f'{moscowpython_list['items']['statistics']['videoCount']}'

    @property
    def url(self):
        return f'{moscowpython_list['items']['snippet']['thumbnails']['url']}'

    @classmethod
    def get_service(cls):
        return cls.__youtube


