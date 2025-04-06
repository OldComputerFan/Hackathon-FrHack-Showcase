import ntplib
from datetime import datetime
from config import SIMULATE_GALILEO_FAILURE

def get_galileo_time():
    if SIMULATE_GALILEO_FAILURE:
        return "GALILEO error: Simulated interference"
    try:
        client = ntplib.NTPClient()
        response = client.request('pool.ntp.org', version=3, timeout=1)
        return datetime.fromtimestamp(response.tx_time)
    except Exception as e:
        return f"GALILEO error: {e}"
        # Fallback to error message if any error occurs