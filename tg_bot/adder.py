import pandas as pd
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.messages import GetDialogsRequest, AddChatUserRequest
from telethon.tl.types import InputPeerEmpty, ChannelParticipantsAdmins
from telethon.tl.types import InputPeerChannel
from telethon.tl.types import InputPeerUser
import pandas
import configparser, pickle
import time


config = configparser.ConfigParser()
config.read("telethon.config")
api_id = "26345051"
api_hash = "d1dc44cb8b9d69ca20b8d6fa5602cca4"
bot_token = "5697892007:AAEfuHnjFjpeMS4J-mw37LKGx4IR53pFcBU"
phone = "+36306854154"


def main_launch():


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


    for chat in chats:
        try:
            if chat.megagroup == True:
                groups.append(chat)
        except:
            continue
    j = 0
    for i in groups:
        print(j,i.title)
        j+=1
    group_to_add = int(input("Enter the id of group:"))
    target_group = groups[group_to_add]

    target_entity = InputPeerChannel(target_group.id, target_group.access_hash)

    mode = int(input('1:ID/2:Name'))
    #
    if mode == 1:
        user_to_add = InputPeerUser(5706562927 ,-3400718621332902635)
    elif mode == 2:
        user_to_add = client.get_input_entity("NikEE1005")

    client(InviteToChannelRequest(target_group, [user_to_add]))

def own_id():
    client = TelegramClient(phone, api_id, api_hash)
    client.connect()
    person = client.get_entity("NikEE1005")
    print(person.id, person.access_hash)
#
#



def adder_launch():
    accounts = []
    h = open('vars.txt', 'rb')
    while True:
        try:
            accounts.append(pickle.load(h))
        except EOFError:
            break
    h.close()
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

    for chat in chats:
        try:
            if chat.megagroup == True:
                groups.append(chat)
        except:
            continue
    j = 0
    for i in groups:
        print(j, i.title)
        j += 1
    while True:

        try:
            group_to_add = int(input("Enter the 'id' of the group you want to add members to:"))
            target_group = groups[group_to_add]
            break
        except ValueError:
            print("Please try again")



    members = pandas.read_csv("members/members.csv", )
    members = members.to_dict(orient="records")

    for i in members:
        user_to_add = InputPeerUser(i["user id"] ,i["access hash"])

        client(InviteToChannelRequest(target_group, [user_to_add]))
        print("One person is done, waiting 60 seconds to continue")
        time.sleep(60)




adder_launch()