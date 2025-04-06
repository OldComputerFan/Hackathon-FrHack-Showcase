import ntplib
from datetime import datetime
from config import SIMULATE_GNSS_FAILURE

def get_gnss_time():
    if SIMULATE_GNSS_FAILURE:
        return "GNSS error: Simulated interference"
    try:
        client = ntplib.NTPClient()
        response = client.request('pool.ntp.org', version=3, timeout=1)
        return datetime.fromtimestamp(response.tx_time)
    except Exception as e:
        return f"GNSS error: {e}"
        # Fallback to error message if any error occurs