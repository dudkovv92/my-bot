import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
 )
filename="app.log",
level=logging.INFO,
format="%(asctime)s - %(levelname)s - %(message)s"

logging.info("Всё работает")
logging.warning("Что-то подозрительное")
logging.error("Ошибка!")