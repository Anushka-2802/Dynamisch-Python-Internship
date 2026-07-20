import logging

logging.basicConfig(filename="employee.txt",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

#logger object
logger = logging.getLogger(__name__)