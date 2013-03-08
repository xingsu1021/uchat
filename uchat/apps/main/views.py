#coding=utf-8
from uliweb import expose, functions

@expose('/')
def index():
    print "===>",request.session.get('user')
    #获取session
    if request.session.get('user'):
        return redirect(url_for('chat.views.Chat.index')) 
    return {}


@expose('/login')
def login():
    username = request.POST.get('username')
    print "username===>",username
    #保存session
    request.session['user'] = username
    return redirect(url_for('chat.views.Chat.index'))