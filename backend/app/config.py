'''
secHUB // backend // config.py
Description: Loads data from sec.env
'''
import os
from dotenv import load_dotenv

load_dotenv()

INTERNAL_API_BASE = os.getenv("INTERNAL_API_BASE")
INTERNAL_API_KEY = os.getenv("INTERNAL_API_KEY")