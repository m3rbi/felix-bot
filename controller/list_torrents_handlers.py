from typing import List
from telegram import Update
from telegram.ext import ContextTypes

from torrent_controller import TorrentController
from torrent_state import TorrentState


def get_list_all_torrents_handler(client_location: str):
    async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
        found = TorrentController(client_location).list_all_torrents()

        # TODO: change to reply_poll
        await update.message.reply_text(format_torrent_list(found))
    
    return handler

def get_list_downloading_torrents_handler(client_location: str):
    async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
        found = TorrentController(client_location).list_downloading_torrents()

        # TODO: change to reply_poll
        await update.message.reply_text(format_torrent_list(found))

    return handler


def get_list_finished_torrents_handler(client_location: str):
    async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
        found = TorrentController(client_location).list_finished_torrents()

        # TODO: change to reply_poll
        await update.message.reply_text(format_torrent_list(found))

    return handler


def format_torrent_list(torrents: List[TorrentState]):
    if len(torrents) == 0:
        return "No torrents found."

    return "\n\n".join(map(str, torrents))
