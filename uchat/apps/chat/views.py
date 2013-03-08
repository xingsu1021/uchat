#coding=utf-8
from uliweb import expose, functions
import redis
import time
from etc.config import UConfig

@expose('/chat')
########################################################################
class Chat(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.pool = redis.ConnectionPool(host='172.17.0.18', port=6379, db=0)
        self.rc = redis.Redis(connection_pool=self.pool)
    
    def index(self):

        import simplejson as json
        
        #获取session
        user = request.session.get('user')
        if not user:
            return redirect(url_for('main.views.index')) 
        
        print "user===>",user
        if not self.rc.get(user):
            self.rc.set(user,
                    json.dumps({'msg': 'test',
                                'created': time.time()
                                }))
        return {}
