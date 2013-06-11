# -*- coding: utf-8 -*-
'''
Created on 

@author: 
'''
from wtforms import Form, Field, TextField, TextAreaField, SelectField, validators
from wtforms.widgets import TextInput
from application.models import *

class ListTextField(Field):
    widget = TextInput()

    def _value(self):
        if self.data:
            return u', '.join(self.data)
        else:
            return u''

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = [x.strip() for x in valuelist[0].split(',')]
        else:
            self.data = []

