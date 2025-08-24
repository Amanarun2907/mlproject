import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(),"logs", LOG_FILE)
## current working directory / logs / log file name
os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH=os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s -%(levelname)s- %(message)s",
    level=logging.INFO,
)






# if __name__=="__main__":
#     logging.info("Logging has started")




# What is Logging in Python? (Simple Definition)
# Logging in Python means recording messages about events that happen in your code. 
# These messages help you keep track of what's going on while your program runs. It is useful for debugging, troubleshooting, and understanding the flow of your program


# Example: Tracking Personal Expenses
# Imagine you want to keep track of all the money you spend each day. You decide to write down every time you buy something, noting:

# The date and time
# What you bought
# The amount spent

# Your log might look like this in a notebook or phone:
# Date	    Item	    Amount
# 24-Aug-2025	Coffee	     ₹50
# 24-Aug-2025	Bus ticket   ₹30
# 24-Aug-2025	Movie ticket ₹150

# This is a real-life "log." 
# By doing this, you can later check where your money went, spot unnecessary spending, and plan your budget—just like how a computer program uses logging to monitor its own activities and errors.