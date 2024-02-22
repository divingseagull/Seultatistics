from typing import AsyncIterator

import discord


def message_to_dict(message: discord.Message) -> dict:
    """
    :param message: history to convert
    :return: a list of messages data
    """
    # noinspection PyTypeChecker
    message_data = {
        "tts": message.tts,
        "author": message.author.id,
        "content": message.content,
        "channel": message.channel.id,
        "mention_everyone": message.mention_everyone,
        "mentions": [member.id for member in message.mentions],
        "channel_mentions": [channel.id for channel in message.channel_mentions],
        "role_mentions": [role.id for role in message.role_mentions],
        "id": message.id,
        "attachments": [attachment.id for attachment in message.attachments],
        "pinned": message.pinned,
        "reactions": [reaction.emoji.id if type(reaction) is not str
                      else reaction.emoji.id
                      for reaction in message.reactions],
        "stickers": [sticker.id for sticker in message.stickers],
        "guild": message.guild.id
    }
    return message_data


async def dict_to_message():
    raise NotImplementedError
