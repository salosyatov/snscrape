import pytest
from snscrape.modules.telegram import Channel, TelegramChannelScraper


def test_parse_channel_html():
    with open('channel-page.html', 'r', encoding='utf8') as file:
        lines = file.readlines()
        text = '\n'.join(lines)
    channel_name = '1'
    channel = TelegramChannelScraper(channel_name)._parse_channel_info(text)

    assert isinstance(channel, Channel)
    assert channel.username == "alyatrend"
    assert channel.title == "Аля про AliExpress"
    assert len(channel.description) > 100
    assert channel.members == 217094
    assert channel.is_public == True


def test_parse_group_html():
    with open('group-page.html', 'r', encoding='utf8') as file:
        lines = file.readlines()
        text = '\n'.join(lines)
    channel_name = '1'
    channel = TelegramChannelScraper(channel_name)._parse_channel_info(text)

    assert isinstance(channel, Channel)
    assert channel.username == "besplatnowb"
    assert channel.title == "Кешбек за отзыв | кэшбэк за выкуп | Скидки"
    assert len(channel.description) > 100
    assert channel.members == 56054
    assert channel.is_public == False


def test_parse_deleted_html():
    with open('deleted-page.html', 'r', encoding='utf8') as file:
        lines = file.readlines()
        text = '\n'.join(lines)
    channel_name = '1'
    channel = TelegramChannelScraper(channel_name)._parse_channel_info(text)

    assert channel is None
