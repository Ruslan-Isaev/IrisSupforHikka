version = (2, 2, 8)

# meta developer: @RUIS_VlP

import random
from datetime import timedelta

from telethon import functions
from telethon.tl.types import Message

from .. import loader, utils


@loader.tds
class IrisSupMod(loader.Module):
    """Саппорт для лс"""

    strings = {
        "name": "irissup",
    }

    def __init__(self):
        self.name = self.strings["name"]

    async def client_ready(self, client, db):
        self.client = client
        self.db = db
        self.myid = (await client.get_me()).id
        self.iris = 5443619563

    async def message_q(
        self,
        text: str,
        user_id: int,
        mark_read: bool = False,
        delete: bool = False,
    ):
        """Отправляет сообщение и возращает ответ"""
        async with self.client.conversation(user_id) as conv:
            msg = await conv.send_message(text)
            response = await conv.get_response()
            if mark_read:
                await conv.mark_read()

            if delete:
                await msg.delete()
                await response.delete()

            return response

    @loader.command()
    async def команды(self, message):
        """Команды Iris Support Bot"""
        ihelp = (
            "Команды Iris Support Bot: https://teletype.in/@iris_cm/isb_commands"
        )
        await utils.answer(message, ihelp)
        
    @loader.command()
    async def сап(self, message):
        """передает введенную команду в Iris Support Bot"""
        bot = "@IrisSupportBot"
        if len(message.text) < 6:
        	await utils.answer(message, "Где текст?")
        	return
        text = f".{message.text[4:]}"
        givs = await self.message_q(
            text,
            bot,
            mark_read=True,
            delete=True,
        )
        await utils.answer(message, givs.text)
        
       
        
        