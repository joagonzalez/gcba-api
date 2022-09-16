import time
from src.config.setting import config
from src.application import Application


if __name__ == '__main__':
    app = Application()
    app.run()
    
    while True:
        time.sleep(10)