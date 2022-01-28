from celery import shared_task
from celery.utils.log import get_task_logger
from django.contrib.auth.models import User
import time

logger = get_task_logger(__name__)

@shared_task
def getAllUsers():
    users = User.objects.all()
    logger.info("Getting all users")
    time.sleep(50)
    print("Helloooo!")
    return {"status": True}