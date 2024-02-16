from googleapiclient.discovery import build
import os
import isodate
import datetime
from dotenv import load_dotenv

load_dotenv()

class PlayList:
    #Класс для плейлиста
    api_key: str = os.getenv('YT_API_KEY')
    #Специальный объект для работы с API
    youtube = build('youtube', 'v3', developerKey=api_key)
    #Другие необходимые атрибуты
    _playlist_data: dict = None
    _video_response: dict = None

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.url = "https://www.youtube.com/playlist?list=" + self.playlist_id
        self.playlist_title = self.youtube.playlists().list(id=self.playlist_id, part='snippet').execute()
        self.title = self.playlist_title['items'][0]['snippet']['title']
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_response()['items']]
        self.right_id: str = ''

    def playlist_response(self) -> dict:
        """Если информации в словаре нет, возвращает информацию о плейлисте"""
        if self._playlist_data is None:
            self._playlist_data = (self.youtube.playlistItems().list(
                playlistId=self.playlist_id, part='contentDetails,snippet').execute())
        return self._playlist_data

    @property
    def total_duration(self) -> datetime.timedelta:
        """Выводит длительносить всего плейлиста"""
        total_duration = datetime.timedelta()
        for video in self.video_response()['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += datetime.timedelta(seconds=duration.total_seconds())
        return total_duration

    def video_response(self) -> dict:
        """Если информации в словаре нет, возвращает информацию о видео."""
        if self._video_response is None:
            self._video_response = self.youtube.videos().list(part='contentDetails,statistics',
                                                              id=','.join(self.video_ids)
                                                              ).execute()
        return self._video_response

    def show_best_video(self) -> str:
        """Показывает видео с наибольшим количеством лайков из плейлиста"""
        more_likes: int = 0
        for video in self.video_response()['items']:
            like_count: int = video['statistics']['likeCount']
            video_id = video['id']
            if int(like_count) > int(more_likes):
                more_likes = like_count
                self.right_id = video_id
        return f"https://youtu.be/{self.right_id}"

    def most_viewed_video(self) -> str:
        """Показывает видео с наибольшим количеством просмотров из плейлиста."""
        more_viewed: int = 0
        for video in self.video_response()['items']:
            view_count: int = video['statistics']['viewCount']
            video_id = video['id']
            if int(view_count) > int(more_viewed):
                more_viewed = view_count
                self.right_id = video_id
        return f"https://youtu.be/{self.right_id}"

    def most_commented_video(self) -> str:
        """Показывает видео с наибольшим количеством комментариев из плейлиста."""
        more_comments: int = 0
        for video in self.video_response()['items']:
            comment_count: int = video['statistics']['commentCount']
            video_id = video['id']
            if int(comment_count) > int(more_comments):
                more_comments = comment_count
                self.right_id = video_id
        return f"https://youtu.be/{self.right_id}"

    def show_longest_video(self) -> str:
        """Показывает самое длинное видео из плейлиста."""
        total_dur = datetime.timedelta()
        for video in self.video_response()['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration = datetime.timedelta(seconds=duration.total_seconds())
            video_id = video['id']
            if total_duration > total_dur:
                total_dur = total_duration
                self.right_id = video_id
        return f"https://youtu.be/{self.right_id}"
