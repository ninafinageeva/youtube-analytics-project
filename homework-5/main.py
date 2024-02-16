import datetime

from src.playlist import PlayList

if __name__ == '__main__':
    pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
    assert pl.title == "Moscow Python Meetup №81"
    assert pl.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"

    duration = pl.total_duration
    assert str(duration) == "1:49:52"
    assert isinstance(duration, datetime.timedelta)
    assert duration.total_seconds() == 6592.0

    assert pl.show_best_video() == "https://youtu.be/cUGyMzWQcGM"

    #Мои проверки
    # print(pl.url)
    # print(pl.title)
    # print(duration)
    # print(pl.show_best_video())
    # print(pl.most_viewed_video())
    # print(pl.most_commented_video())
    # print(pl.show_longest_video())
    # from pprint import pprint
    # pprint(pl.video_response())


