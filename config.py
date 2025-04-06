# Configuration file for time synchronization

# List of time sources in order of priority
TIME_PRIORITY = ["GNSS", "PTP", "5G"]  # 5G is now the network source

# Simulation flags
SIMULATE_GNSS_FAILURE = False
SIMULATE_PTP_NOISE = False
SIMULATE_NETWORK_JITTER = False
