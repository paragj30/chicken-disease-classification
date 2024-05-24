import sys
import logging
import os
from datetime import datetime

logging_str = "[%(asctime)s: line_number-%(lineno)d: %(levelname)s: %(module)s: %(message)s]" 
log_dir = "logs"
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_filepath = os.path.join(os.getcwd(),log_dir, LOG_FILE)
os.makedirs(log_dir, exist_ok=True)



logging.basicConfig(
    level = logging.INFO,
    format = logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnClassifierProjectLogger")
