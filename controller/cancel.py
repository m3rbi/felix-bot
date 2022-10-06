from telegram import Update
from telegram.ext import CallbackContext


async def handle_cancel(update: Update, context: CallbackContext):
    if update.message.reply_to_message:
        await context.bot.edit_message_text(text='Canceling action.', 
                                            message_id=update.message.reply_to_message.message_id,
                                            chat_id=update.message.chat_id)
    else:
        await update.message.reply_text(text='Reply to a message in order to cancel.')
