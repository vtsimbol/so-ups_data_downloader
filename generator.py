import os
import pandas as pd
import config
import constants
from datetime import timedelta


def generate():
    print('---- Generate .csv files ----')
    # check directory for result
    if not os.path.exists(config.result_dir):
        os.makedirs(config.result_dir)
    for region in constants.region.keys():
        print(f'Processing: {region}')
        # list for result dataset by this region
        generate_data_list = []
        consumption_data_list = []
        datetime_list = []
        # read all .csv files
        current_dt = config.start_datetime
        while current_dt <= config.stop_datetime:
            file_path = os.path.join(os.path.join(config.temp_dir, region), f'{current_dt.day:02d}-{current_dt.month:02d}-{current_dt.year}.csv')
            if os.path.exists(file_path):
                df = pd.read_csv(file_path, encoding='windows-1251', sep=';')
                for i in range(0, df.shape[0]):
                    if df['Время Мск'][i][:5].find(f'{current_dt.day:02d}-{current_dt.month:02d}') != -1:
                        datetime_list.append(df['Время Мск'][i])
                        consumption_data_list.append(df['Потребление, МВт*ч'][i])
                        generate_data_list.append(df['Генерация, МВт*ч\\'][i])
            current_dt += timedelta(days=1)
        # save to .csv
        df = pd.DataFrame({'Время Мск': datetime_list,
                           'Потребление, МВт*ч': consumption_data_list,
                           'Генерация, МВт*ч': generate_data_list})
        df.to_csv(os.path.join(config.result_dir, f'{region}__{config.start_datetime.day:02d}-'
                  f'{config.start_datetime.month:02d}-{config.start_datetime.year}__'
                  f'{config.stop_datetime.day:02d}-{config.stop_datetime.month:02d}-{config.stop_datetime.year}.csv'),
                  index=False, sep=';', encoding='utf-8')
