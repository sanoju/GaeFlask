# -*- coding: utf-8 -*-
import logging

#logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger().setLevel(logging.INFO)

from flask import Flask
import settings

app = Flask(__name__)
app.config.from_object('application.settings')

import views