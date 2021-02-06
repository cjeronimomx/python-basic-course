# pip install python-dotenv
import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("LOG_PATH"))