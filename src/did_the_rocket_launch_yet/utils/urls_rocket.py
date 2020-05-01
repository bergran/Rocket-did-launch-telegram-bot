from urllib import parse

from bernard.conf import settings


def get_url_rocket():
    return f'{settings.API_URL}{parse.quote(settings.VIDEO_NAME)}'


def get_url_rocket_frame(frame: int):
    return f'{get_url_rocket()}/frame/{frame}/'
