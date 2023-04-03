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
    ├── README.md

## Setup and Installation

If not already, install [Telegram](https://telegram.org/)

### API Access Token

To create a Telegram bot, a Telegram API access token is needed.

To retrieve a token, open Telegram and search for @botfather. Start a conversation
with [BotFather](https://t.me/botfather) by pressing the start button or sending '''/start'''.

Send the command '''/newbot''' to BotFather and respond to the prompts to first name
your bot and then give it a username. Following this BotFather will respond with an
HTTP API Token to access the Telegram API. Do not share your API access token as
anyone can use it to control or manage your bot.

In

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install os, telebot.

```bash
pip install os
pip install telebot
```

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing

Pull requests are welcome. For major changes

## Author

David Folger