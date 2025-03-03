import logging
import os
from datetime import datetime

#Step 1: Generate a unique log filename based on the current date and time
LOG_FILE = f"{datetime.now().strftime('%m-%d-%Y-%H-%M-%S')}.log"  
# Example output: "03-03-2025-14-50-30.log"

# Step 2: Define the folder where log files will be stored
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)

# os.getcwd() → Gets the current working directory (where the script is running)
# "logs" → Subdirectory where logs will be stored
# Example output: "C:\Users\Abhinav\MyProject\logs" (on Windows)

# Step 3: Create the logs directory if it doesn’t exist
if not os.path.exists(logs_path):
    os.makedirs(logs_path)

# Step 4: Create the full path for the log file
LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)
# Combines logs directory with the log filename
# Example output: "C:\Users\Abhinav\MyProject\logs\03-03-2025-14-50-30.log"

logging.basicConfig(
    filename=LOG_FILE_PATH,  # Log messages will be saved in this file
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Format of log messages
    level=logging.INFO,  # Minimum log level to be recorded
)

if __name__ == "__main__":
    logging.info("logging started")