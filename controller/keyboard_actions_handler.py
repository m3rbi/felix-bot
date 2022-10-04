from telegram import Update, CallbackQuery
from telegram.ext import CallbackContext
from torrent_controller import TorrentController
from env import get_torrent_client_url


DOWNLOAD = "DOWNLOAD"
DELETE = "DELETE"


async def handle_download(download_data: str, query: CallbackQuery):
    TorrentController(get_torrent_client_url()).download_magnet(download_data)

    await query.edit_message_text(text="Starting download!")


async def handle_delete(info_hash: str, query: CallbackQuery):
    TorrentController(get_torrent_client_url()).delete_info_hash(info_hash)
    await query.edit_message_text(text="Deleted successfully!")


CALLBACK_ACTIONS = {
    DOWNLOAD: handle_download,
    DELETE: handle_delete
}


async def handle_keyboard_callback(update: Update, context: CallbackContext):
    query = update.callback_query

    query.answer()

    for key, action in CALLBACK_ACTIONS.items():
        if query.data.startswith(key):
            return await action(query.data[len(key):], query)
