import cs_bot
from cs_bot import MessageSession, logger
from cs_bot.libs.seatalk_openapi.client import SeaTalkOpenAPIClient
from cs_bot.permissions import ANYONE

@cs_bot.on_prefix(["marco"], permission = ANYONE)
def echo(session: MessageSession):
    logger.info(f"receive message: {session.message.content}")
    session.send(session.sender.email, "polo")

@cs_bot.on_prefix(["echo"], permission = ANYONE)
def challenge(session: MessageSession):
    logger.info(f"receive message: {session.message.content}")
    session.send(session.sender.email, session.message.content.lstrip("echo"))