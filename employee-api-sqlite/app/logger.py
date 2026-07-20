"""
This file configures application logging.
All log messages are stored in employee.log
"""
import logging

logging.basicConfig(
    filename="employee.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
#object of logger
logger = logging.getLogger(__name__)