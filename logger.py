import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname) - %(messages)s"
)

logger = logging.getLogger(__name__)

