#!/usr/bin/python
# encoding:utf-8
__author__ = 'xyc'


import logging,commands
from conf import settings

class DockerHandler(object):

    HOST_IP, USER, PEM_FILE = settings.SERVICEHOST

    @classmethod
    def fix(cls, service_name):
        fix_sh = "docker restart " + service_name
        sh = "ssh -i %s %s@%s \"%s\"" % (cls.PEM_FILE, cls.USER, cls.HOST_IP, fix_sh)
        if service_name:
            status, res = commands.getstatusoutput(sh)
            logging.info("STATUS:%d, OUTPUT:%s" % (status, res))
        else:
            logging.info("SERVICE NAME IS NULL, SO NOTHING TO DO ")


