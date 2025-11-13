import os
import logging
from datetime import datetime
from typing import Optional, Dict, Any

def setup_logger(name: str, log_file: Optional[str] = None) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger

def validate_amount(amount: float) -> bool:
    return isinstance(amount, (int, float)) and amount > 0

def format_timestamp(timestamp: datetime) -> str:
    return timestamp.strftime('%Y-%m-%d %H:%M:%S')

def load_env_variable(key: str, default: Optional[str] = None) -> str:
    value = os.getenv(key, default)
    if value is None:
        raise ValueError(f"Environment variable '{key}' is not set and no default provided.")
    return value

def parse_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
    required_fields = ['amount', 'currency', 'timestamp']
    for field in required_fields:
        if field not in payload:
            raise ValueError(f"Missing required field '{field}' in payload.")
    
    if not validate_amount(payload['amount']):
        raise ValueError("Invalid amount in payload.")
    
    return {
        'amount': payload['amount'],
        'currency': payload['currency'],
        'timestamp': format_timestamp(payload['timestamp'])
    }