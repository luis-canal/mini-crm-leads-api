import logging
from config import API_KEY

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname) - %(messages)s"
)

logger = logging.getLogger(__name__)

