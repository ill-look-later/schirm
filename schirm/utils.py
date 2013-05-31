import Queue
import logging
import threading

logger = logging.getLogger(__name__)

def put_nowait_sleep(queue, data):
    """Given a limited queue and an object, try to put object on the queue.

    If the queue is Full, wait an increasing fraction of a second
    until trying again. Return when the data has been put on the queue.
    """
    times = 0
    wait_f = lambda x: 0.01 * (2 ** x) if x < 9 else 1.28
    while True:
        try:
            queue.put_nowait(data)
            return
        except Queue.Full:
            time.sleep(wait_f(times))
            times += 1

def get_xselection(self):
    try:
        return subprocess.check_output(['xsel', '-o'])
    except OSError, e:
        if e.errno == 2:
            logger.info("Install xsel to use the 'paste x selection' feature")
            return ""
        else:
            raise e

def create_thread(target, name=None, daemon=True):
    t = threading.Thread(target=target, name=name)
    if daemon:
        t.setDaemon(True)
    t.start()
    return t
