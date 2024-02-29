import logging
import os
from datetime import datetime

# Define log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define log directory
log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")

# Ensure log directory exists
os.makedirs(log_path, exist_ok=True)

# Define log file path
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    filename=LOG_FILEPATH,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
                    )

if __name__ == '__main__':
    logging.info("Testing logging functionality.")
