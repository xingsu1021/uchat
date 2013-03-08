#coding=utf-8
from uliweb import expose, functions

@expose('/chat')
########################################################################
class Chat(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
    
    def index(self):
        return '<h1>Hello, Uliweb</h1>'
