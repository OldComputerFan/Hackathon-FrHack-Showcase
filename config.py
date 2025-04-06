# Configuration file for time synchronization

# List of time sources in order of priority
TIME_PRIORITY = ["PTP", "GNSS", "5G", "GPS"]  # 5G is now the network source

# Simulation flags
SIMULATE_GNSS_FAILURE = False
SIMULATE_PTP_NOISE = False
SIMULATE_NETWORK_JITTER = False
SIMULATE_GPS_FAILURE = False  # For GPS simulation