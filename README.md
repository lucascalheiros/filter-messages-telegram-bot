# filter-messages-telegram-bot

This is a simple filter message bot, it works together with a dummy telegram account which is used to subscribe to channels, bots, etc. 
The messages received by this dummy account are checked with a defined regex and showed to the user, if matched.


## Usage

`pip install -r requirements.txt`

Please copy the `config.template.py`, rename it to `config.py`, and follow the instructions specified inside the file.

`cp config.template.py config.py`

After that use `python run.py` to start, you will be prompted to verify the telegram dummy account.

Start the bot that you have created using bot father, and type /filter REGEX to filter the messages of the verified account.
