import json
import socketio
import os
import requests
import discord
import datetime

from requests import get
from discord_webhook import DiscordWebhook, DiscordEmbed
from markupsafe import Markup
from dotenv import load_dotenv

load_dotenv()
donation = os.environ.get('token') #You donation alert token
webhook_da = os.environ.get('webhook')
webhook = DiscordWebhook(webhook_da)
print(f"Remote DA destination set to: {donation}")
print(F"Webhook is set to {webhook_da}")
print("Donationalerts script startup successfully!")

sio = socketio.Client()

@sio.on('connect')
def on_connect():
	sio.emit('add-user', {"token": donation, "type": "alert_widget"})

@sio.on('donation')
def on_message(data):
	y = json.loads(data)

	embed = DiscordEmbed(title='_**New donation!**_', description=f"**{y['username']}** donated **{y['amount']} {y['currency']}** with message: **{y['message']}**", color='03b2f8')
	embed.set_footer(text='https://www.donationalerts.com/r/hewwo_kitty69', icon_url=f'https://a.okayu.me/3')
	webhook.add_embed(embed)
	response = webhook.execute()

sio.connect('wss://socket.donationalerts.ru:443',transports='websocket')
