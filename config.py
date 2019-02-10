import os
from datetime import datetime


base_dir = os.path.dirname(os.path.abspath(__file__))
temp_dir = os.path.join(base_dir, 'temp')
result_dir = os.path.join(base_dir, 'result')
log_dir = os.path.join(base_dir, 'log')
start_datetime = datetime(2008, 1, 1)
stop_datetime = datetime(2018, 12, 31)
