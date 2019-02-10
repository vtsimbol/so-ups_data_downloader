import os
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from datetime import timedelta
import config
import constants
import logger


def download():
    print('---- Download data from so-ups.ru ----')
    # check directory for result
    if not os.path.exists(config.temp_dir):
        os.makedirs(config.temp_dir)
    for region in constants.region.keys():
        print(f'Processing: {region}')
        region_path = os.path.join(config.temp_dir, region)
        # exist and clear directory for region data
        if not os.path.exists(region_path):
            os.makedirs(region_path)
        # download data by current region
        current_dt = config.start_datetime
        while current_dt <= config.stop_datetime:
            if not os.path.exists(os.path.join(region_path, f'{current_dt.day:02d}-{current_dt.month:02d}-{current_dt.year}.csv')):
                url = f'http://so-ups.ru/index.php?id=ees_gen_consump_plan&no_cache=1&tx_ms1cdu_pi1[kpo]={region}' \
                    f'&tx_ms1cdu_pi1[dt]={current_dt.day:02d}.{current_dt.month:02d}.' \
                    f'{current_dt.year}&tx_ms1cdu_pi1[format]=csv'
                try:
                    stream = urlopen(url)
                    with open(os.path.join(region_path, f'{current_dt.day:02d}-{current_dt.month:02d}-{current_dt.year}.csv'), 'wb') as file:
                        file.write(stream.read())
                except HTTPError:
                    logger.log_write(f'{region}\\{current_dt.day:02d}.{current_dt.month:02d}.{current_dt.year} - HTTPError')
                except URLError:
                    logger.log_write(f'{region}\\{current_dt.day:02d}.{current_dt.month:02d}.{current_dt.year} - URLError')
                except:
                    logger.log_write(f'{region}\\{current_dt.day:02d}.{current_dt.month:02d}.{current_dt.year} - Other Error')
            current_dt += timedelta(days=1)