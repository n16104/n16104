import  time


class timer(object):
    def_init_(self, verbose=false):
       self.verbose = verbose


    def_enter_(self):
       self.start_time = time.time()
       return self


    def_exit_(self, exc_type,exc_val,exc_tb):
       self.end = time.time()
       self.secs = self.end_time - self.start_time
       self.millis = self.secs * 1000
       if self.verbose:
           print('elapsed time: {0:f} ms'.format(self.mills))