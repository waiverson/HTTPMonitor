#!/usr/bin/python
# encoding:utf-8
__author__ = 'xyc'

CHECK_URL = (('http://user.51desk.com', 200, "userportal"),
             ('http://admin.51desk.com', 200, "adminportal"),
             ('http://www.51desk.com', 200, ""),
             ('http://52.74.107.193:16001', 200, "mobileserver"),
             ('http://52.74.107.193:16002', 200, "jobserver"),
             ('http://52.74.107.193:16003', 200, "connector"),
             ('http://52.74.107.193:16004/WEBAPI/acs/data/analysis/satisfaction', 200, "acs"))

SERVICEHOST = ('52.74.107.193', 'root', '51deskserver.pem')

TIMEOUT = 5

CHECK_INTERVAL = 10

NOTICATION = ('notication.ConsoleNotication', 'notication.MailNotication')
HANDLER = ('handler.DockerHandler',)

# CALLBACK_URL = ()

# WEBUI = ''

EMAIL_HOST = 'smtp.mxhichina.com'
EMAIL_PORT = '25'
EMAIL_HOST_USER = 'poster@51desk.com'
DEFAULT_FROM_EMAIL = 'poster@51desk.com'
EMAIL_HOST_PASSWORD = 'faxiang@123'
EMAIL_USE_TLS = False

RECIPIENTS = ['tom.xiong@51desk.com']
