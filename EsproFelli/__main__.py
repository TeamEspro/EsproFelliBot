from EsproFelli.__init__ import app

# EsproFelli/main.py

# Absolute Import ka use karein

from modules.felli import felli_function
from modules.wel import welcome_message
from modules.tagall import tag_all

# Functions ko call karein
app = app()
print(felli_function())
print(welcome_message())
print(tag_all())
