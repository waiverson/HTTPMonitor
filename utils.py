#!/usr/bin/python
# encoding:utf-8

__author__ = 'xyc'

import logging,smtplib
from email.mime.text import MIMEText
from conf import settings
from importlib import import_module

class SMTPConnection(object):

    def __init__(self, host=None, port=None, username=None, password=None, use_tls=None, fail_silently=False):
        self.host = host or settings.EMAIL_HOST
        self.port = port or settings.EMAIL_PORT
        self.username = username or settings.EMAIL_HOST_USER
        self.password = password or settings.EMAIL_HOST_PASSWORD
        self.use_tsl = use_tls or settings.EMAIL_USE_TLS
        self.fail_silenty = fail_silently
        self.conection = None

    def open(self):

        if self.conection:
            return False
        try:
            self.conection = smtplib.SMTP(self.host, self.port)
            if self.use_tsl:
                self.conection.ehlo()
                self.conection.starttls()
                self.conection.ehlo()
            if self.username and self.password:
                self.conection.login(self.username, self.password)
            return True
        except:
            if not self.fail_silenty:
                raise

    def close(self):
        import socket
        try:
            try:
                self.conection.quit()
            except socket.sslerror:
                self.conection.close()
        except:
            if not self.fail_silenty:
                raise
            return
        finally:
            self.conection = None

    def send(self, recipients, from_email, subject, message):

        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = ','.join(recipients)

        try:
            self.conection.sendmail(from_email, recipients, msg.as_string())
        except Exception, e:
            logging.error(e)
            if not self.fail_silenty:
                raise
            return False
        return True

class ImportCLS(object):

    @classmethod
    def get_cls(cls, cls_dir):
        try:
            dot = cls_dir.rindex('.')
        except ValueError:
            logging.error("CANNOT PARSE CLASS NAME: %s", cls_dir)
            return None
        module, clsname = cls_dir[:dot], cls_dir[dot+1:]

        try:
            mod = import_module(module)
        except ImportError, e:
            logging.error(e)
            logging.error("CANNNOT LOAD MODULE: %s", module)
            return None

        try:
            cls = getattr(mod, clsname)
        except AttributeError:
            logging.error("CANNOT GET CLASS:%s", clsname)
        return cls

    @classmethod
    def get_cls_ins(cls, cls_dir, **kwargs):
        return cls.get_cls(cls_dir)(**kwargs)