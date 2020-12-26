# -*- coding: utf-8 -*-
''' task
'''
from ..model.task import _Task
from .. import db


class TaskService():

    def getSetting(self, num=1):
        task = _Task.query.filter_by(id=num).first()
        if not task:
            task = _Task()
            db.session.add(task)
            db.session.commit()
        return task

    def updateTaskStatus(self, status, num=1):
        task = self.getSetting(num)
        if task.status != status:
            task.status = status
            db.session.commit()

taskService = TaskService()