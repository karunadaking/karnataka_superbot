# ============================================================
# Group Manager Bot
# Author: karnatakabots (https://t.me/karnatakabots) 
# Support: https://t.me/karnatakabots
# Channel: https://t.me/karnatakabots
# YouTube: https://youtube.com/@karnatakabots
# License: Open-source (keep credits, no resale)
# ============================================================

from .start import register_handlers
from .group_commands import register_group_commands

def register_all_handlers(app):
    register_handlers(app)
    register_group_commands(app)
    print("✅ Group commands registered!")

