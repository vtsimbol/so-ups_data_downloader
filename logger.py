import os
import config


def initialization():
    print('---- Log initialization ----')
    if not os.path.exists(config.log_dir):
        os.makedirs(config.log_dir)
    with open(os.path.join(config.log_dir, 'log.txt'), 'w') as file:
        file.write(f'start\n')


def log_write(data):
    if not os.path.exists(config.log_dir):
        os.makedirs(config.log_dir)
    if not os.path.exists(os.path.join(config.log_dir, 'log.txt')):
        with open(os.path.join(config.log_dir, 'log.txt'), 'w') as file:
            file.write(f'{data}\n')
    else:
        with open(os.path.join(config.log_dir, 'log.txt'), 'a') as file:
            file.write(f'{data}\n')
