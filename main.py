# import libs
import os
import requests
import random
# import things from libs
from donationalerts import Alert
from requests import get
from discord_webhook import DiscordWebhook, DiscordEmbed
from markupsafe import Markup
from dotenv import load_dotenv

# configure settings, maybe ill change it later to .env lib
load_dotenv()
da_alert_widget_token = os.environ.get('da_alert_widget_token')
webhook_da = os.environ.get('webhook')
webhook = DiscordWebhook(webhook_da)
print(f"Remote Donationalerts widget is set to: {da_alert_widget_token}")
print(F"Webhook is set to {webhook_da}")
print("Donationalerts script startup successfully!")

# main part where we get and send this messages to discord
alert = Alert(da_alert_widget_token)
@alert.event()
def new_donation(event):
	embed = DiscordEmbed(title='_**New donation!**_', description=f'**{event.username}** donated **{event.amount} {event.currency}** with message: **{event.message}**', color='03b2f8')
	embed.add_embed_field(name='Date Time', value=f'{event.header}')
	embed.set_footer(text='https://www.donationalerts.com/r/hewwo_kitty69', icon_url=f'https://a.okayu.me/3')
	webhook.add_embed(embed)
	response = webhook.execute()
	print(event.header)