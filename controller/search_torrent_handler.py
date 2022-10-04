from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackContext
from torrent_controller import TorrentController
from keboard_actions_handler import DOWNLOAD

from torrent_query import TorrentQuery


async def search_torrent_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    requested_torrent = update.message.text
    torrents = TorrentQuery().query(requested_torrent)

    if len(torrents) == 1 and torrents[0].size == 0:
        await update.message.reply_text(f"Could not find any results for {requested_torrent}")
        return

    keyboard = [[InlineKeyboardButton(str(i), callback_data=f"{DOWNLOAD}{i.get_magnet()}")] for i in torrents]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text('Choose torrent:', reply_markup=reply_markup)
