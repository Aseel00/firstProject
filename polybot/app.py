import flask
from flask import request
import os
from polybot.bot import Bot, QuoteBot, ImageProcessingBot

app = flask.Flask(__name__)

TELEGRAM_BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
BOT_APP_URL = os.environ['BOT_APP_URL']
YOLO_URL=os.environ['YOLO_URL']
BUCKET_NAME=os.environ['BUCKET_NAME']
REGION=os.environ['REGION']
polybot_env=os.environ['POLYBOT_ENV']

@app.route('/', methods=['GET'])
def index():
    return 'Ok'


@app.route(f'/{TELEGRAM_BOT_TOKEN}/', methods=['POST'])
def webhook():
    req = request.get_json()
    bot.handle_message(req['message'])
    return 'Ok'


if __name__ == "__main__":
    #bot = Bot(TELEGRAM_BOT_TOKEN, TELEGRAM_APP_URL)
    #bot = Bot(TELEGRAM_BOT_TOKEN, BOT_APP_URL)
    #bot = QuoteBot(TELEGRAM_BOT_TOKEN, BOT_APP_URL)
    bot = ImageProcessingBot(TELEGRAM_BOT_TOKEN, BOT_APP_URL,polybot_env,BUCKET_NAME,REGION,YOLO_URL)

    app.run(host='0.0.0.0', port=8443)
