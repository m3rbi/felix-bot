import os

def get_bot_token():
    token = os.getenv('TELEGRAM_TOKEN')
    if not token:
        raise EnvironmentError('TELEGRAM_TOKEN is not set!')
    
    return token


def get_torrent_client_url():
    url = os.getenv('TORRENT_CLIENT')
    if not url:
        raise EnvironmentError('TORRENT_CLIENT is not set!')
    
    return url
