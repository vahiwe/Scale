from jobs.commands.remoteok import Command
from celery import shared_task
command = Command()

@shared_task
def pullremoteokjobs():
    return command.pullremoteokjobs()

@shared_task
def pullindeedjobs():
    return command.pullindeedjobs()
