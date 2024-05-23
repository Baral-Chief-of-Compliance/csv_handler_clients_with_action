from csvHandler import csvHandler
import os
from dotenv import load_dotenv


load_dotenv()


ch = csvHandler(os.getenv('IN_FILE_PATH'))


#использование методов экземпляра класса csvHandler
ch.save_processed_data(ch.analyze_client_behavior(), os.getenv('OUT_FILE_PATH'))

