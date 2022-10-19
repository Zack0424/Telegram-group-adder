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


def main():


    client = TelegramClient(phone, api_id, api_hash)
    client.connect()

    chats = []
    last_date = None
    chunk_size = 200
    groups = []

    result = client(GetDialogsRequest(
        offset_date=last_date,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=chunk_size,
        hash=0
    ))
    chats.extend(result.chats)
    j = 0

    for chat in chats:
        try:
            if chat.megagroup == True:
                groups.append(chat)
        except:
            continue

    for i in groups:
        print(j,i.title)
        j+=1
    group_to_add = int(input("Enter the id of group:"))
    target_group = groups[group_to_add]

    target_entity = InputPeerChannel(target_group.id, target_group.access_hash)

    mode = int(input('1/2'))
    #
    if mode == 1:
        user_to_add = InviteToChannelRequest(5641414094 ,-111539806409344814)


def own_id():
    client = TelegramClient(phone, api_id, api_hash)
    client.connect()
    me = client.get_entity("me")
    print(me.id, me.access_hash)
#     5641414094 -111539806409344814

main()
