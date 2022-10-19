import pandas as pd
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.messages import GetDialogsRequest, AddChatUserRequest
from telethon.tl.types import InputPeerEmpty, ChannelParticipantsAdmins
from telethon.tl.types import InputPeerChannel
from telethon.tl.types import InputPeerUser

import configparser

config = configparser.ConfigParser()
config.read("telethon.config")
api_id = "26345051"
api_hash = "d1dc44cb8b9d69ca20b8d6fa5602cca4"
bot_token = "5697892007:AAEfuHnjFjpeMS4J-mw37LKGx4IR53pFcBU"
phone = "+36306854154"
# api_id = config["telethon_credentials"]["api_id"]
# api_hash = config["telethon_credentials"]["api_hash"]

client = TelegramClient("bot", api_id, api_hash).start(bot_token=bot_token)
client.connect()

group_name = "Testerino001_bot_test"
#
# if not client.is_user_authorized():
#     client.send_code_request(phone)
#     client.sign_in(phone, input("enter the code:"))



person = client.get_entity(chat)
print(person.username, person.phone)
client.send_message(person.id, message =" asd")
"""
api_id = "GIVE YOUR API ID"
api_hash = "GIVE YOUR API HASH"

client = TelegramClient('test', api_id, api_hash)
client.connect()

# Provide the name of the Telegram group.
# In below example we are scraping members from vikasjhahelloworld001 Group

target_group = client.get_entity("vikasjhahelloworld001")

print("Group ID: {}, Group Hash: {}".format(target_group.id, target_group.access_hash))

target_group_entity = InputPeerChannel(target_group.id,target_group.access_hash)


# Change the location of the file as per your need

df = pd.read_excel("C:\\crypto\\members.xls")
print(df.columns)
users = df.to_records(index=False)
print(users)

for i in range(6):
    try:
        print("Adding: {}".format(users[i]['username']))
        print("Userid: {} , user_access_hash: {}".format(users[i]['id'], users[i]['access_hash']))
        user_to_add =InputPeerUser(users[i]['id'], users[i]['access_hash'])
        print("user to add: {}".format(user_to_add))
        client(AddChatUserRequest("vikasjhahelloworld001",users[i]['username'],fwd_limit=1))
    except Exception as e:
        print(e)

"""
