from datetime import datetime, timedelta
from config import SIMULATE_PTP_NOISE
import random

def get_ptp_time():
    try:
        now = datetime.now()
        # if SIMULATE_PTP_NOISE:
        #     noise = timedelta(milliseconds=random.uniform(-50, 50))
        #     return now + noise
        return now
    except Exception:
        return None
        # Fallback to None if any error occurs
        # This is a placeholder for actual PTP time retrieval logic.