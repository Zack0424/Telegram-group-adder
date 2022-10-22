from telethon import TelegramClient
from telethon.tl.functions.contacts import ResolveUsernameRequest

# # from telethon.tl.functions.channels import GetFullChannelRequest
# #
# # client = TelegramClient("asd",26345051,"d1dc44cb8b9d69ca20b8d6fa5602cca4").start(bot_token="5697892007:AAEfuHnjFjpeMS4J-mw37LKGx4IR53pFcBU")
# # async def message_sender():
# #     await client.send_message("ZackEE1005", "Hi")
# #
# # with client:
# #     client.loop.run_until_complete(message_sender())
#
#
# from telethon import TelegramClient
# from telethon.tl.functions.channels import GetParticipantsRequest
# from telethon.tl.functions.channels import GetFullChannelRequest
# from telethon.tl.types import ChannelParticipantsSearch
#
#
#
api_id = "26345051"
api_hash = "d1dc44cb8b9d69ca20b8d6fa5602cca4"
bot_token = "5697892007:AAEfuHnjFjpeMS4J-mw37LKGx4IR53pFcBU"
phone_number = "+36306854154"
# ################################################
# channel_username = 'Testerbot011'
# ################################################
#

#
# # ---------------------------------------
# offset = 0
# limit = 200
# my_filter = ChannelParticipantsSearch('')
# all_participants = []
# while_condition = True
# # ---------------------------------------
# channel = client(GetFullChannelRequest(channel_username))
# while while_condition:
#     participants = client(GetParticipantsRequest(channel=channel_username, filter=my_filter, offset=offset, limit=limit, hash=0))
#     all_participants.extend(participants.users)
#     offset += len(participants.users)
#     if len(participants.users) < limit:
#          while_condition = False
try:

    client = TelegramClient('message_sender', api_id, api_hash)

    assert client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone_number)
        me = client.sign_in(phone_number, input('Enter code: '))

    channel = await client(ResolveUsernameRequest('channel_name'))
    async for _user in client.iter_participants(entity=channel):
        print(_user)

except Exception as e:
    print(e)
