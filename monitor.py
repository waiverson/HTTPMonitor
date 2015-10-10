#!/usr/bin/python
# encoding:utf-8
__author__ = 'xyc'

import logging
import events
from utils import ImportCLS
from urllib2 import urlopen, URLError, HTTPError

class Monitor(object):
    """
    监控url，并触发后续任务
    """

    def __init__(self, notication, handler, timeout):
        self.failed = set()
        self.timeout = timeout
        self.get_req_fire(notication)
        self.get_service_handler(handler)

    def get_req_fire(self, notication):
        for n in notication:
            cls = ImportCLS.get_cls(n)
            events.request_success += cls.recover
            events.request_fail += cls.alert

    def get_service_handler(self, handler):
        for h in handler:
            cls = ImportCLS.get_cls(h)
            events.service_handler += cls.fix

    def set_url_failed(self, url, code):
        self.failed.add((url, code))

    def get_url_failed(self, url, code):
        return (url, code) in self.failed

    def recover(self, url, code):
        self.failed.remove((url, code))
        events.request_success.fire(url=url)

    def alert(self, url, expected_code, code, service_name):
        logging.info("CHECK %s FAILED!" % url)
        logging.info("**START TO SEND ALERT**")
        events.request_fail.fire(url=url, expected_code=expected_code, code=code)
        logging.info("**START TO HANDLE EXCEPTION**")
        events.service_handler.fire(service_name=service_name)

    def check_url(self, url):
        try:
            code = urlopen(url, timeout=self.timeout).getcode()
            logging.debug("RETURNED %d" % code)
            return code
        except HTTPError, e:
            logging.error(e)
            return e.getcode()
        except URLError, e:
            logging.error(e)
        return None

    def check(self, check_urls):
        for url, expected_code, service_name in check_urls:
            logging.debug("CHECKING %s whit code %d" % (url, expected_code))
            code = self.check_url(url)
            if not code or code != expected_code:
                if not self.get_url_failed(url, expected_code):
                    self.alert(url, expected_code, code, service_name)
                    self.set_url_failed(url, expected_code)
            else:
                if self.get_url_failed(url, expected_code):
                    self.recover(url, code)
                logging.info("%s is running !", url)

