from EsproFelli.__init__ import app

# EsproFelli/main.py

# Absolute Import ka use karein

from EsproFelli.modules.felli import felli_function
from EsproFelli.modules.wel import welcome_message
from EsproFelli.modules.tagall import tag_all

# Functions ko call karein
app = app()
bot = app()
print(felli_function())
print(welcome_message())
print(tag_all())
