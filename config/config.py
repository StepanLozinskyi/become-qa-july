import os

class Config:
    base_url = os.environ.get("BASE_URL", 'https://api.github.com')