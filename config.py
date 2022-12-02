# FILL THESE VALUES ACCORDINGLY.

from RomeoBot.config.hell_config import Config

class Development(Config):
  # get these values from my.telegram.org. 
  APP_ID = 15350244    # 6 is a placeholder. Fill your 6 digit api id
  API_HASH = "28100f5f7ebbc51d16ca759c87af30dc"   # replace this with your api hash

  # create any PostgreSQL database.
  # I recommend to use elephantsql and paste that link here
  DB_URI = "postgres://romeo_user:wgvduEmB98az6GV4cK1v6XhT1lEfWJsI@dpg-ce1qq4ta4996ndu00ieg-a.oregon-postgres.render.com/romeo"

  # After cloning the repo and installing requirements...
  # Do `python string.py` and fill the on screen prompts.
  # String session will be saved in your saved message of telegram.
  # Put that string here.
  ROMEOBOT_SESSION = "1BVtsOJIBu5Ulqw7qelUe_xMMgL0OFbyny1rSJm5krlm0Rb2IWuKRLJj2-7zR6KxGddjDZUiH01P4gTqGsQK7shtZyAK3wc_HqC1HsmBIjDZvv9B33CCE9Pe5xTl31jMruQfCzUr9wSS2QcbNXC5KezxzWW_SYsd9eHWpAsjvhab3nhfP-vXLbN6pm_BsMeev3TCEtP0dfV3A_rjZd9LI1AMpL2B4t9AvXeU2YdM6GSbpCnm9c6bZ-aV9Z6LxgfQB9z9pUoW-gNzVvSq55fhlRNjhrVdXBrAciZ062yngwENG0yPn5EGBVxPoD9vWC-tBIa7a2-7OUjnNu5wZZcXeSUiuEM1TJCc="

  # Create a bot in @BotFather
  # And fill the following values with bot token and username.
  BOT_TOKEN = "5423617634:AAGilf7a2Od1S7mK9ozNIl6VkN1q9zXcAZE" #token

  # Custom Command Handler. 
  HANDLER = "."

  # Custom Command Handler for sudo users.
  SUDO_HANDLER = "."


# end of required config
# bot
