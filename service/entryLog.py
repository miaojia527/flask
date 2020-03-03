#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lib.service import service
from service.orm.EntryLog import EntryLog
import sys,chardet
import json
from lib.func import ComplexEncoder, func
import time
from sqlalchemy import func

class entryLog(service):
    """docstring for entryLog"""
    def __init__(self, session):
        super(entryLog, self).__init__()
        self.session = session
        
    def get(self, id):
        
        session = self.session
        #清除默认缓存
        # #session.commit()
        result = session.query(EntryLog).filter_by(id = id).first()
        
        return result.to_dict()
    
    def create(self, entryId, uid):
        
        session = self.session
        
        addtime = time.strftime("%Y-%m-%d %H:%M:%S")
        entry = EntryLog( entryId=entryId, uid=uid, addtime=addtime)
        session.add(entry)
        session.commit()
        result = 1
        return (result == 1) and 'success' or "failure"