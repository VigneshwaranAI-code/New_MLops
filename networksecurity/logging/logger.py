import logging 
import datetime
import os




logs_path = os.path.join(os.getcwd(), "logs") 
os.makedirs(logs_path, exist_ok=True)

log_file = f"{datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.log"
log_file_path = os.path.join(logs_path, log_file)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler()
    ]
)
