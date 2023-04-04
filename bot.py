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