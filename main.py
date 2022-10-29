import cs_bot
from cs_bot import StartupConfig
from cs_bot.adapters import sop_bot
from dotenv import load_dotenv
import os 
load_dotenv()
config = {
    "adapter":{
        "app_id": os.environ["APP_ID"],
        "app_secret": os.environ["APP_SECRET"],
        "signing_secret": os.environ["SIGNING_SECRET"]
    }
}

cs_bot.init(StartupConfig.parse_obj(config))
cs_bot.register_adapter(sop_bot.Adapter)
cs_bot.load_plugin("plugins.echo")

if __name__ == "__main__":
    cs_bot.run(host="localhost", port="8000")