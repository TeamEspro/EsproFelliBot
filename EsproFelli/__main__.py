from EsproFelli.__init__ import app

# EsproFelli/main.py

# Absolute Import ka use karein

from EsproFelli.modules.felli import felli_function
from EsproFelli.modules.wel import welcome_message


# Functions ko call karein
app = app()

print(felli_function())
print(welcome_message())
