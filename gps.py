import ntplib
from datetime import datetime, timedelta
from config import SIMULATE_GPS_FAILURE

def get_gps_time():
    if SIMULATE_GPS_FAILURE:
        return "GPS error: Simulated interference"
    try:
        client = ntplib.NTPClient()
        response = client.request('pool.ntp.org', version=3, timeout=1)
        return datetime.fromtimestamp(response.tx_time) - timedelta(seconds=19)
    except Exception as e:
        return f"GPS error: {e}"
        # Fallback to error message if any error occurs
