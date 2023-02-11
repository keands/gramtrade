import logging

from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,  MessageHandler, filters

TOKEN='5884157462:AAERSKDOqxKuipBW1eEAhz_dg4Z_Msrem_k'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def order_type(order):
    print(f'decode order')


def stop_loss_pips(entry, sl):
    print(f'determine SL in pips')


def start(update, context):
    update.message.reply_text("Salut, on va faire des pips mtn !")


if __name__ == '__main__':
    logger.info("launch dispatcher telegram")
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.MessageFilter, start))

    app.run_polling()
