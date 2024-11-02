from datetime import datetime


class Logger:
    def __init__(self, log_file: str = "./minescript/auto_highway/auto_highway.log"):
        self.file = open(log_file, "w")

    def write_log(self, message: str) -> None:
        self.file.write(f"{datetime.now().strftime("%H:%M:%S")}:\t{message}\n")
        self.file.flush()


logger = Logger()
