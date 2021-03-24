from __future__ import absolute_import, unicode_literals
import logging

from os import getenv
from datetime import datetime
from django.conf import settings
from meupcgamer.celery import app

logger = logging.getLogger("celery")

@app.task
def get_ordersB2B():
    logger.info("-"*25)
    logger.info("Initiated Task - " + func_name())
    EcommGateway.get_ordersB2B()
    logger.info("Ended Task - " + func_name())
    logger.info("-"*25)


def func_name():
    import traceback
    return traceback.extract_stack(None, 2)[0][2]