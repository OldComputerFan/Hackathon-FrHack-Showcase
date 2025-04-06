import ntplib
from datetime import datetime, timedelta
from config import SIMULATE_GPS_FAILURE

def get_gps_time():
    if SIMULATE_GPS_FAILURE:
        return None  # Return None instead of string
    try:
        client = ntplib.NTPClient()
        response = client.request('pool.ntp.org', version=3, timeout=1)
        return datetime.fromtimestamp(response.tx_time) - timedelta(seconds=19)
    except Exception:
        return None  # Also return None on exception

