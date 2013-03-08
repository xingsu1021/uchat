#coding=utf-8
from uliweb import expose, functions
import redis
from etc.config import UConfig

@expose('/chat')
########################################################################
class Chat(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
        rc = redis.Redis(connection_pool=pool)
    
    def index(self):

        #获取session
        if not request.session.get('user'):
            return redirect(url_for('main.views.index')) 
        return {}
