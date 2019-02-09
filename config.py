import os
from datetime import datetime


base_dir = os.path.dirname(os.path.abspath(__file__))
temp_dir = os.path.join(base_dir, 'temp')
log_dir = os.path.join(base_dir, 'log')
start_datetime = datetime(2010, 1, 1)
stop_datetime = datetime(2018, 12, 31)
