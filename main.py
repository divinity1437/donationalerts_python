# import libs 
import requests
# import things from libs
from donationalerts import Alert
from requests import get
from discord_webhook import DiscordWebhook, DiscordEmbed
from markupsafe import Markup

# configure settings, maybe ill change it later to .env lib
da_alert_widget_token = '7h7DyglahN670YkMj1Oj'
webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1018598316889608232/86gfueOkDrP-k72a3DV7ZDQnWKX5zxN2pggZ-tnjctwv5_WbtbqybnKojQtaX73DKEry')

print("Donationalerts script startup successfully!")

# main part where we get and send this messages to discord
alert = Alert(da_alert_widget_token)
@alert.event()
def new_donation(event): 
	embed = DiscordEmbed(title='_**New donation!**_', description=f'**{ event.username }** donated **{ event.amount } { event.currency }** with message: **{ event.message }**', color='03b2f8')
	embed.set_footer(text='https://www.donationalerts.com/r/hewwo_kitty69', icon_url='https://a.okayu.me/3')
	webhook.add_embed(embed)
	response = webhook.execute()