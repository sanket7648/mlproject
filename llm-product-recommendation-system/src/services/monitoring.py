from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def log_request(user_id: str, endpoint: str):
    logger.info(f"User {user_id} accessed {endpoint}")

def log_response(user_id: str, endpoint: str, response_time: float):
    logger.info(f"User {user_id} received response from {endpoint} in {response_time:.2f} seconds")

def log_error(user_id: str, endpoint: str, error_message: str):
    logger.error(f"User {user_id} encountered an error at {endpoint}: {error_message}")

def log_feedback_submission(user_id: str, product_id: str, rating: int):
    logger.info(f"User {user_id} submitted feedback for product {product_id} with rating {rating}")

def log_performance_metric(metric_name: str, value: float):
    logger.info(f"Performance metric {metric_name}: {value:.2f}")