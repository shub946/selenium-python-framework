import logging
class logclass:
    def getthelogs(self):
        logger =logging.getLogger()
        filehandler = logging.FileHandler("Logs\\logfile.log",mode="w")
        formatter =logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s', datefmt='%d%m%y %I:%M:%S %p')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger