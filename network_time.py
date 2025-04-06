from datetime import datetime, timedelta
import random
from config import SIMULATE_NETWORK_JITTER

def get_network_time():
    try:
        base_time = datetime.utcnow()
        jitter = random.uniform(-2.0, 2.0)
        if SIMULATE_NETWORK_JITTER:
            jitter += random.uniform(-50.0, 50.0)  # Extreme jitter
        return base_time + timedelta(milliseconds=jitter)
    except Exception:
        return datetime.utcnow()
        # Fallback to current UTC time if any error occurs
        # This is a placeholder for actual network time retrieval logic.