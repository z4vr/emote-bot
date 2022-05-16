import logging
import os
import asyncio

def setup_logging():
    """
    Setup logging for the emote-bot.
    """

    # general logs
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')

    # discord logs
    discord_logger = logging.getLogger('discord')
    discord_logger.setLevel(logging.INFO)
    discord_handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    logging.getLogger('discord').addHandler(discord_handler)

    # save the log to a file
    log_file = os.path.join(os.path.dirname(__file__), 'emote-bot.log')
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)-8s %(message)s',
        '%Y-%m-%d %H:%M:%S'))
    logging.getLogger('').addHandler(file_handler)


def run_bot():
    """
    Run the bot.
    """

    from client import client
    client.run()

if __name__ == '__main__':
    setup_logging()
    asyncio.run(run_bot())