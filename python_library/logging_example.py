import logging

logging.basicConfig(
    filename="output.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",
    datefmt="%Y-%m-%d %I:%M:%S%p",
)

logging.debug("Log with debug-level severity")
logging.info("Log with info-level severity")
logging.warning("Log with warning-level severity")
logging.error("Log with error-level severity")
logging.critical("Log with error-level severity")

try:
    raise Exception("Throw exception")
except Exception as e:
    logging.error("Exception occurred", exc_info=True)
