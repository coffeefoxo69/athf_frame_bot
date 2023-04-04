# TeleFrame Bot

TeleFrame Bot is a Telegram Bot Template for automated, scheduled posting of
individual frames/images from a .mp4 source or multiple .mp4 sources contained
within a directory.

This readme will function as a guide to utilizing the source code
of this bot to create and manage other bots that serve the same or similar purposes.

Users of this code should be expected to know how to navigate Telegram and know Python.

## Directory Structure
    .
    ├── .env                   # Environmental variables
    ├── bot.py                 # Python
    ├── data                   # stores current episode frames
    ├── source_media           # stores source media
    └── README.md

## Setup and Installation with a Linux Environment

If not already, install the following:

[Telegram](https://telegram.org/)
[Python](https://www.python.org/)

### API Access Token

To create a Telegram bot, a Telegram API access token is needed.

To retrieve a token, open Telegram and search for @botfather. Start a conversation
with [BotFather](https://t.me/botfather) by pressing the start button or sending '/start'.

<insert screenshot of image on telegram>

Send the command '/newbot' to BotFather and respond to the prompts to first name
your bot and then give it a username. Following this BotFather will respond with an
HTTP API Token to access the Telegram API. Do not share your API access token as
anyone can use it to control or manage your bot.

In the directory open up the .env file and paste your API access token into the BOT_TOKEN
assignment.

```bash
export BOT_TOKEN=<your-api-access-token>
```

Then run in

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install os,
time, pyTelegramBotAPI, datetime, pytz, and opencv-python.

```bash
pip install os
pip install time
pip install pyTelegramBotAPI
pip install datetime
pip install pytz
pip install opencv-python
```

### Telegram Channel/Chat

For the bot to work as intended, it needs a Telegram Channel or Chat with write access.

To create a bot, hit the icon in the upper right corner of Telegram and select either
New Group or New Channel

<insert screenshot of image on telegram>

### Chat_Id Retrieval

TBA

### Container/Docker Setup

## Usage

Navigate to the root directory while in a Linux environment and type
```bash
python3 bot.py
```


## Contributing

Pull requests are welcome. For major changes

## Author

David Folger

## Appendix

### bot.py code

```python
import os
import time
from datetime import datetime
from pytz import timezone
import telebot
import cv2

BOT_TOKEN = '6295719644:AAEX8iTVyDV5IZF0pQB7SXvX9wJuT4CruGY'
TZ = timezone('EST')
BOT_DESCRIPTION = "This is a bot"

episode_number = 1;
season_number = 1;
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "I am Alive!")

def generate_episode_frames(episode_number, season_number):
        frame_counter = 0;
        frame_number = 0;
        season = 'athf_season_' + str(season_number)
        episode = 'ep' + str(episode_number)
        current_file = './source_media/' + str(season) + '/' + str(episode) + '.mp4'
        cam = cv2.VideoCapture(current_file)

        try:
             if not os.path.exists('data'):
                  os.makedirs('data')
        except OSError:
             print('Error: Creating directory of data')
        while True:
            ret, frame = cam.read()
            frame_counter += 1;

            if ret:
                if (frame_counter % 100 == 0):
                    name = './data/frame' + str(frame_number) + '.jpg'
                    print('Creating...' + name)
                    cv2.imwrite(name, frame)
                    frame_number += 1;
            else:
                 break
        cam.release()
        cv2.destroyAllWindows()
        return frame_number


next_frame = 0

while True:
    if next_frame == 0:
        total_frames = generate_episode_frames(episode_number, season_number)
        framepath = './data/frame' + str(next_frame) + '.jpg'
        bot.send_photo(chat_id=-1001652896787, photo=open(framepath, 'rb'))
        episode_number += 1
        next_frame += 1

    if (datetime.now(TZ).minute == 0):
        framepath = './data/frame' + str(next_frame) + '.jpg'
        bot.send_photo(chat_id=-1001652896787, photo=open(framepath, 'rb'))
        next_frame += 1
        time.sleep(60)
        break
    else:
        print(datetime.now(TZ).minute) #debugging
        time.sleep(10) #debugging
```