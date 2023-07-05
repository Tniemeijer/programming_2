from datetime import datetime


class Logger:
    def __init__(self, log_file='log.log', err_log='log.err'):
        """
        Initializes the logger.
        In self.done files that have already been processed will be stored.
        """
        self.log = log_file
        self.err = err_log
        self._add_log_start()
        self.done = []

    def add_to_log(self, itm, mode='log'):
        """
        Method that writes to log with date and timestamp added.
        
        -------

        input:
                itm (str): text that will be added to the log
                log (str): 'log' or 'err'
                                'log': append itm to process log.
                                'err': append itm to error log.
        
        output:
                writes line to log (str):  ddmmYY-HH:MM:SS: itm
        """
        match mode:
            case 'log':
                log = self.log
            case 'err':
                log = self.err
            case _:
                log = self.err

        date_time = datetime.strftime(datetime.now(),"%d/%m/%Y-%H:%M:%S")
        with open(log, mode='a', encoding='utf-8') as log:
            log.writelines(f'{date_time}: {itm}\n')
    
    def _add_log_start(self):
        """
        When initializing the logger a start text is added to indicate a new run. 
        """
        self.add_to_log("Run started")

        