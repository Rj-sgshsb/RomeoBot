# FILL THESE VALUES ACCORDINGLY.

from RomeoBot.config.hell_config import Config

class Development(Config):
  # get these values from my.telegram.org. 
  APP_ID = 18551764    # 6 is a placeholder. Fill your 6 digit api id
  API_HASH = "991a66d509729ab73929bb42b514dce5"   # replace this with your api hash

  # create any PostgreSQL database.
  # I recommend to use elephantsql and paste that link here
  DB_URI = "postgres://romeo_user:wgvduEmB98az6GV4cK1v6XhT1lEfWJsI@dpg-ce1qq4ta4996ndu00ieg-a.oregon-postgres.render.com/romeo"

  # After cloning the repo and installing requirements...
  # Do `python string.py` and fill the on screen prompts.
  # String session will be saved in your saved message of telegram.
  # Put that string here.
  ROMEOBOT_SESSION = "1BVtsOHgBuw3rsvwrB3uzoV1MjG69mDdKegyazeoir7VoJ2Cvq_ZFAAovnGYlmwk1bs6XhdWiUGo_g9qY-UdefA9wknZw89uRA766yqklIN_ZcAc5ns2nx37ZYGF1tC3pSIwUL3xvkhAOrbkFc3HPqza1MmroiLgBf5PKTF2cESJZpGeDYq4xsJQG_XNv3VToGtjZlzh81AwTSuNoU7L378pi9d_wz7ttAZVqm2WzkBhlS3YWFGgmDKeZMsf_nhWWkSoy3e5R-qbV8QCEWO4Y9vFfRtwvV_Cb975lANn0skLlQNT_twRUjO9aEJ4XmJKuOwZ4Hd-X6C653wV8cTJDQky8YM9btXY="

  # Create a bot in @BotFather
  # And fill the following values with bot token and username.
  BOT_TOKEN = "5604091752:AAEbdcctzFVW_eET0jWCbA8IYl7OEoOnHos" #token

  # Custom Command Handler. 
  HANDLER = "."

  # Custom Command Handler for sudo users.
  SUDO_HANDLER = "."


# end of required config
# bot
