import pickle
import random
import time
import traceback

import pandas as pd
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser

SLEEP_TIME_1 = 100
SLEEP_TIME_2 = 100


def adder_launch():
    accounts = []
    h = open('vars.txt', 'rb')
    while True:
        try:
            accounts.append(pickle.load(h))
        except EOFError:
            break
    h.close()
    if accounts != []:
        client = TelegramClient(accounts[0][2], accounts[0][0], accounts[0][1])
        client.connect()
    else:
        print("You don't have any accounts added to your bot")
        print('Returning to home page!')
        time.sleep(5)
        return None
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
            target_group_entity = InputPeerChannel(target_group.id, target_group.access_hash)
            break
        except ValueError:
            print("Please try again")

    members = pd.read_csv("members/members.csv")
    members = members.to_dict(orient="records")

    n = 0
    accounts_num = len(accounts)
    m = 1
    for user in members:
        n += 1
        if n % 80 == 0:
            time.sleep(60)
        try:
            print("Adding {}".format(user['user id']))
            user_to_add = InputPeerUser(user['user id'], user['access hash'])

            client(InviteToChannelRequest(target_group_entity, [user_to_add]))
            print("Waiting for 60-180 Seconds ...")
            time.sleep(random.randrange(0, 5))
        except PeerFloodError:
            print(
                "Getting Flood Error from telegram. Script is stopping now if no other accounts. Please try again after some time.")
            if m < accounts_num:
                client = TelegramClient(accounts[m][2], accounts[m][0], accounts[m][1])
                client.connect()
                print("Using another account!")
            else:
                print("Waiting {} seconds".format(SLEEP_TIME_2))
            time.sleep(SLEEP_TIME_2)
        except UserPrivacyRestrictedError:
            print("The user's privacy settings do not allow you to do this. Skipping ...")
            print("Waiting for 5 Seconds ...")
            time.sleep(random.randrange(0, 5))
        except:
            traceback.print_exc()
            print("Unexpected Error! ")
            continue
    return None
