import os
import dotenv

dotenv.load_dotenv()

class EnvVar:
    def __init__(self):
        self.debug = os.getenv('DEBUG')
        self.secret_key = os.getenv('SECRET_KEY')
        #self.database_url = os.getenv('DATABASE_URL')
        self.address = os.getenv('ADDRESS')
        self.port = os.getenv('PORT')
            
env = EnvVar()

print(f"debug = {env.debug}\nsecret_key = {env.secret_key}\ndatabase_url = null")