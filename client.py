from config import BOT_TOKEN
from swibots import Client

client = Client(
    BOT_TOKEN
)
client._upload_mode = "STORAGE"