#!/usr/bin/python
# encoding:utf-8
__author__ = 'xyc'

class EventHook(object):
    """
    如何使用此类:
    my_event = EventHook()
    def on_my_event(a, b, **kw):
        print "****" 事件处理程序
    my_event += on_my_event
    my_event.fire(a, b)
    """

    def __init__(self):
        self._handlers = []

    def __iadd__(self, handler):
        self._handlers.append(handler)
        return self

    def __isub__(self, handler):
        self._handlers.remove(handler)
        return self

    def fire(self, **kwargs):
        for handler in self._handlers:
            handler(**kwargs)

request_success = EventHook()

request_fail = EventHook()
