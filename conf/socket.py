#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from conf.middleware import middleware
from flask_socketio import send, emit, join_room, leave_room
from threading import Lock

class socket(object):

    def __init__(self):
        super(socket, self).__init__()

    @staticmethod
    def path(app, socketio, **args):
        
        #登陆验证用tcp验证，状态保存到redis上

        @socketio.on('message', namespace='/chat')          
        def handle_message(message):
            print('received message: ' + message)
            send("message", message)          
        
        @socketio.on('json', namespace='/chat')
        def handle_json(json):
            print('received json: ' + str(json))
            send(str(json), json=True)

        @socketio.on('test', namespace='/chat')             
        def handle_test_custom_event(arg1, arg2, json):
            print('received args: ' + arg1 + arg2 + str(json))
            emit('my response', json, namespace='/chat')   #用于自定义事件

        @socketio.on('join', namespace='/chat')
        def on_join(data):
            username = data['username']
            room = data['room']
            join_room(room)
            send(username + ' has entered the room.', room=room)

        @socketio.on('leave', namespace='/chat')
        def on_leave(data):
            username = data['username']
            room = data['room']
            leave_room(room)
            send(username + ' has left the room.', room=room)

        @socketio.on('connect', namespace='/chat')    #注意，连接和断开事件的对象是命名空间。
        def _connect():
            emit('server_response', {'data': '连接客户端成功！'})

        @socketio.on('disconnect', namespace='/chat')
        def _disconnect():
            print('Client disconnected')
        
        @socketio.on_error()        # Handles the default namespace
        def error_handler(e):
            pass

        @socketio.on_error('/chat') # handles the '/chat' namespace
        def error_handler_chat(e):
            pass

        @socketio.on_error_default  # handles all namespaces without an explicit error handler
        def default_error_handler(e):
            pass

