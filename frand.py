# отправь это видео сообщение своему другу)
# канал @modwini
from .. import loader


@loader.tds
class cat(loader.Module):
    """Подпишись на канал @modwini"""

    strings = {"name": "cat"}

    async def catcmd(self, message):
        """Скинь это своему другу)"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://telesco.pe/kruglishik/7",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return