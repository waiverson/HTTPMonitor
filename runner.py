#!/usr/bin/python
# encoding:utf-8
__author__ = 'xyc'

import sys,logging,time

from monitor import Monitor
from conf import settings

DEFAULT_TIMEOUT = 20
DEFAULT_INTERVAL = 120

def main():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s  MODULE:%(module)s LineNO:%(lineno)d %(message)s",
                        stream=sys.stdout)
    timeout = getattr(settings, "TIMEOUT", DEFAULT_TIMEOUT)
    check_inv = getattr(settings, "CHECK_INTERVAL", DEFAULT_INTERVAL)
    # callback_url = getattr(settings, "CALLBACK_URL", None)

    monitor = Monitor(settings.NOTICATION, settings.HANDLER, timeout)

    try:
        while True:
            monitor.check(settings.CHECK_URL)
            time.sleep(check_inv)
    except KeyboardInterrupt:
        pass
    except Exception, e:
        logging.error(e)

if __name__ == '__main__':
    main()