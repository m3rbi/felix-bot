from telegram import Update
from telegram.ext import ContextTypes

from torrent_controller import TorrentController
from env import get_torrent_client_url


async def delete_torrent_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    found = TorrentController(get_torrent_client_url()).list_finished_torrents()

    if len(found) == 0:
        await update.message.reply_text('No finished torrents found!')
        return
    
    keyboard = [[InlineKeyboardButton(str(i), callback_data=f"{DELETE}{i.record.info_hash()}")] for i in found]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text('Choose torrent:', reply_markup=reply_markup)
