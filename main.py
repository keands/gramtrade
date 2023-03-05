import logging

from jproperties import Properties
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackContext

from gramTrade import find_pair, order_type, find_values, retrieve_position

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

configs = Properties()

with open('app-config.properties', 'rb') as config_file:
    configs.load(config_file)

TOKEN_BOT = configs.get("TOKEN").data


async def detect_keywords(update: Update, context: CallbackContext):
    message = update.message.text

    pair = None
    tps = []
    sl = None
    order = None

    lines = message.split("\n")

    # retrieve pair
    for line in lines[:2]:
        if pair is None:
            pair = find_pair(line)

    if pair is None:
        logger.info("This pair is not used actually")
        await update.message.reply_text("This pair is not used actually, contact support")
        return
    else:
        for line in lines[:2]:
            order = order_type(line)

        for line in lines[:]:
            if "SL" in line and sl is None:
                sl = await find_values(line)

            if "TP" in line:
                tps.append(await find_values(line))

        if order is None:
            order = await retrieve_position(sl, tps)

        response = None

        if len(tps) <= 1:
            response = "order: {} \n pair: {} \n SL: {} \n TP: {}".format(order, pair, sl, tps[0])
            logger.debug(response)
        else:
            response = "order: {} \n pair: {} \n SL: {} \n TP: {}".format(order, pair, sl, tps)
            logger.debug(response)

        await update.message.reply_text(response)


def main():
    logger.info("launch dispatcher telegram")
    app = ApplicationBuilder().token(TOKEN_BOT).build()

    keyword_handler = MessageHandler(filters.TEXT, detect_keywords)
    app.add_handler(keyword_handler)

    app.run_polling()


if __name__ == '__main__':
    main()
