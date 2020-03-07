#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import flask_login, base64, json
from service.module.User import User as muser

class middleware(object):

    def __init__(self, app):
        super(middleware, self).__init__()

        ##页面登录插件
        login_manager = flask_login.LoginManager()
        login_manager.session_protection = 'strong'
        login_manager.login_message = u"用户未登录，请先登录。"
        login_manager.init_app(app)

        @login_manager.request_loader
        def load_user_from_request(request):

            api_key = request.args.get('apiKey')
            uid     = request.args.get("uid")

            if api_key and uid:
                user = muser.get(api_key, uid)
                if user:
                    return user

            api_key = request.headers.get('auth')
            uid     = request.headers.get('uid')
            if api_key:
                try:
                    api_key = base64.b64decode(api_key)
                except TypeError:
                    pass
                try:
                    uid = base64.b64decode(uid)
                except TypeError:
                    pass
                user = muser.get(api_key, uid)
                if user:
                    return user
            return None
        @login_manager.unauthorized_handler
        def unauthorized():
            # do stuff
            ret = {}
            ret['status'] = 0
            ret['message']= '你还未获得授权，无法访问'
            return json.dumps(ret)

    