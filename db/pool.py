import os
import dotenv
from psycopg2.pool import SimpleConnectionPool
from root import root
from urllib import parse

env_path = os.path.join(root, '.env')
dotenv.load_dotenv(env_path)
env = os.getenv

database_url = env('DATABASE_URL')
parse.uses_netloc.append('postgres')
url = parse.urlparse(database_url)
pool = SimpleConnectionPool(1,
                            20,
                            user=url.username,
                            password=url.password,
                            host=url.hostname,
                            port=url.port)
