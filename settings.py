#!/usr/bin/python
# encoding:utf-8
__author__ = 'xyc'

CHECK_URL = (('http://user.xxx.com', 200, "xxx"),
             ('http://admin.xxx.com', 200, "xxx"),
             ('http://www.xxx.com', 200, "xxx"),
             ('http://xxx', 200, "xxx"),
             ('http://xxx', 200, "xxx"),
             ('http://xxx', 200, "xxx"),
             ('http://xxx', 200, "xxx"))

SERVICEHOST = ('10.10.10.10', 'root', 'xxx.pem')

TIMEOUT = 10

CHECK_INTERVAL = 10

RETRY_COUNT = 3

NOTICATION = ('notication.ConsoleNotication', 'notication.MailNotication')
HANDLER = ('handler.DockerHandler',)

# CALLBACK_URL = ()

# WEBUI = ''

EMAIL_HOST = 'smtp.xxx.com'
EMAIL_PORT = '25'
EMAIL_HOST_USER = 'xx@xxx.com'
DEFAULT_FROM_EMAIL = 'xx@xxx.com'
EMAIL_HOST_PASSWORD = 'xxx@123'
EMAIL_USE_TLS = False

RECIPIENTS = ['xx.xx@xxx.com']
