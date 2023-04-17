# #this class is used to save logs in a file, i.e., autoamtion.log

from datetime import datetime

class Logger:
    def __init__(self, log_file_path):
        self.log_file_path = log_file_path

    def write_log(self, log_message):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.log_file_path, 'a') as log_file:
            log_file.write(f'{current_time} - {log_message}\n')
