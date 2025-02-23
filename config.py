import os
class Config:
    API_ID=24509589
    API_HASH="717cf21d94c4934bcbe1eaa1ad86ae75"
    BOT_TOKEN="7734465358:AAGMuYNK4DSMq8i7W5HofNa6WHr6xtbgRIU"
    SUDO = list(int(i) for i in os.environ.get("SUDO", "6693611573").split(" "))
    START_IMG="https://telegra.ph/file/52fefb8bd51289a83a49b.jpg"
    BOT_ID=8084144216
    MONGO_URL = "mongodb+srv://rogip74246:fCM4fkn8jWv9zizJ@ritikraj.mylvo.mongodb.net/?retryWrites=true&w=majority&appName=ritikraj"
    BOT_USERNAME="ZuliaiBot"
    BOT_NAME="ZuliaiBot"
