import telegram
from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackQueryHandler, CommandHandler
from list_torrents_handlers import get_list_all_torrents_handler, get_list_downloading_torrents_handler, get_list_finished_torrents_handler
from search_torrent_handler import search_torrent_handler

from keyboard_actions_handler import handle_keyboard_callback
from delete_torrent_handler import delete_torrent_handler


from env import get_bot_token, get_torrent_client_url


def main():
    client_url = get_torrent_client_url()

    application = ApplicationBuilder().token(get_bot_token()).build()

    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), search_torrent_handler))
    application.add_handler(CommandHandler('delete', delete_torrent_handler))
    application.add_handler(CallbackQueryHandler(handle_keyboard_callback))
    
    application.add_handler(CommandHandler('all', get_list_all_torrents_handler(client_url)))
    application.add_handler(CommandHandler('downloading', get_list_downloading_torrents_handler(client_url)))
    application.add_handler(CommandHandler('finished', get_list_finished_torrents_handler(client_url)))

    application.run_polling()


if __name__ == '__main__':
    main()
