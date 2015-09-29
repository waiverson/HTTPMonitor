#!/usr/bin/python
# encoding:utf-8
__author__ = 'xyc'

CHECK_URL = (('http://user.52desk2.com', 200),
             ('http://admin.51desk.com', 200),
             ('http://www.51desk.com', 200),
             ('http://52.74.107.193:16001', 200),
             ('http://52.74.107.193:16002', 200),
             ('http://52.74.107.193:16003', 200),
             ('http://52.74.107.193:16004', 200),
             ('http://52.74.107.193:16005', 200))

TIMEOUT = 5

CHECK_INTERVAL = 120

NOTICATION = ('notication.ConsoleNotication', 'notication.MailNotication')
HANDLER = ('FX_Monitor.handler',)

# CALLBACK_URL = ()

# WEBUI = ''

EMAIL_HOST = 'smtp.mxhichina.com'
EMAIL_PORT = '25'
EMAIL_HOST_USER = 'poster@51desk.com'
DEFAULT_FROM_EMAIL = 'poster@51desk.com'
EMAIL_HOST_PASSWORD = 'Abc123456'
EMAIL_USE_TLS = False

RECIPIENTS = ['tom.xiong@51desk.com']
