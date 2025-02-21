# main.py

import sys
import os

# modules folder ko Python path me add karein
sys.path.append(os.path.join(os.path.dirname(__file__), "modules"))

# Ab modules ko import karein
from bot import bot_function
from felli import felli_function
from wel import welcome_message
from tagall import tag_all

# Sare functions ko call karein
print(bot_function())
print(felli_function())
print(welcome_message())
print(tag_all())
