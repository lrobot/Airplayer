from Plex_media_backend import PlexMediaBackend
import utils
import os
import time
import tempfile

def get_telegram_bot():
    import telegram
    from telegram.ext import Updater, CommandHandler
    class TelegramBot(object):
        def __init__(self, token="", chatid=""):
            self.telegram_bot_token_ = 'telegram_token'
            self.telegram_bot_chat_id_ = 'chatid1'
            self.telegram_bot_token_ = token
            self.telegram_bot_chat_id_ = chatid
            live_bot = telegram.Bot(token=self.telegram_bot_token_)
            self.live_bot_ = live_bot

            updater = Updater(telegram_bot_token, use_context=True)
            updater.dispatcher.add_handler(CommandHandler('hello', self.hello))
            updater.start_polling()
            updater.idle()
            self.updater_ = updater
        def sendMessage(self, message):
            self.live_bot_.sendMessage(chat_id=self.telegram_bot_chat_id_, text=message)
        def hello(self,update, context):
            update.message.reply_text('Hello {}'.format(update.message.from_user.first_name))
    return TelegramBot
class DownloadMediaBackend(PlexMediaBackend):
    """
    a robot backend for receive airplay command for download and send notification to external message channel
    """
    def __init__(self, host, port, username=None, password=None):
        super(PlexMediaBackend, self).__init__(host, port, username, password)
        self._TMP_DIR = tempfile.mkdtemp()
        self.telegrambot_ = None
        """
        Make sure the folder is world readable, since XBMC might be running as a
        different user then Airplayer.

        As pointed out at https://github.com/PascalW/Airplayer/issues#issue/9
        """
        os.chmod(self._TMP_DIR, 0755)

        self.log.debug('TEMP DIR: %s', self._TMP_DIR)
        print "tempdir", self._TMP_DIR
        self._TMP_DIR = None
    def cleanup(self):
        pass

    def stop_playing(self):
        pass

    def show_picture(self, data):
        if self._TMP_DIR == None:
            return
        utils.clear_folder(self._TMP_DIR)
        filename = 'picture%d.jpg' % int(time.time())
        path = os.path.join(self._TMP_DIR, filename)

        """
        write mode 'b' is needed for Windows compatibility, since we're writing a binary file here.
        """
        f = open(path, 'wb')
        f.write(data)
        f.close()

    def play_movie(self, url):
        self.log.debug("url is %s", url)
        self.telegrambot_.sendMessage(url)

    def notify_started(self):
        token = self.get_config('token')
        chatid = self.get_config('chatid')
        #self.telegrambot_ = get_telegram_bot()(token, chatid)
        pass
    def pause(self):
        pass

    def play(self):
        pass

    def get_player_position(self):
        pass

    def is_playing(self):
        pass

    def set_player_position(self, position):
        pass

    def set_player_position_percentage(self, percentage_position):
        pass

    def set_start_position(self, percentage_position):
        pass

