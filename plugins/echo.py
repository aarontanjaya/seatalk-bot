import cs_bot
from cs_bot import MessageSession, logger
from cs_bot.libs.seatalk_openapi.client import SeaTalkOpenAPIClient
from cs_bot.permissions import ANYONE
import requests
import os
import json

@cs_bot.on_prefix(["marco"], permission = ANYONE)
def echo(session: MessageSession):
    logger.info(f"receive message: {session.message.content}")
    session.send(session.sender.email, "polo")

@cs_bot.on_prefix(["echo"], permission = ANYONE)
def challenge(session: MessageSession):
    logger.info(f"receive message: {session.message.content}")
    session.send(session.sender.email, session.message.content.lstrip("echo"))

@cs_bot.on_prefix(["weather"], permission = ANYONE)
def challenge(session: MessageSession):
    data = requests.get("http://api.weatherstack.com/current?access_key="+
            os.environ["WEATHER_ACCESS_KEY"]+"&query=Jakarta")
    data = data.json()
    print(data["current"]["temperature"], data["current"]["weather_descriptions"])
    temperature = str(data["current"]["temperature"])
    description = str(data["current"]["weather_descriptions"][0])
    humidity = str(data["current"]["humidity"])
    session.send(session.sender.email, 
        description+", "+
        temperature+"°C - humidity: "+
        humidity+"%"
    )

blast_loop = []
@cs_bot.on_prefix(["blast"], permission = ANYONE)
def blast_something(session: MessageSession):
    blast_loop.append(cs_bot.every(5).seconds.do(blast))
    # for email in session.message.content.lstrip("blast").split(","):
    

def blast():
    seabot = SeaTalkOpenAPIClient(os.environ["APP_ID"],
        os.environ["APP_SECRET"],
        os.environ["SIGNING_SECRET"]
    )
    emails = ["aaron.tanjaya@shopee.com", "william.ciptono@shopee.com"]
    employee_code =seabot.get_employee_code_with_email(emails)

    for val in employee_code.values():
        seabot.send_single_chat_message(val, "test schedule")

is_blast = False
@cs_bot.on_prefix(["stop"], permission = ANYONE)
def stop_blast(session: MessageSession):
    cs_bot.cancel_job(blast_loop[0])
    blast_loop.pop()
