import logging

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from jobs.models import Jobs

from jobs.scraper import RemoteOKAPIClient, IndeedAPIClient

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'A command to work with RemoteOK API and its data.'

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.client = RemoteOKAPIClient()
        self.indeedclient = IndeedAPIClient()

    
    def pullremoteokjobs(self):
        logging.info(
            'Pulling data from RemoteOk API and storing to database...'
        )
        for data in self.client.getjobs():
            if 'id' not in data:
                continue
            job, _ = Jobs.objects.get_or_create(id=data['id'])
            job.id = data.get('id','')
            job.slug = data.get('slug','')
            job.epoch = data.get('epoch','')
            job.date = data.get('date','')
            job.company = data.get('company','')
            job.position = data.get('position','')
            job.description = data.get('description','')
            job.url = data.get('url','')
            job.save()
        logging.info('Jobs successfully pulled from RemoteOk and stored')


    def pullindeedjobs(self):
        logging.info(
            'Pulling data from Indeed and storing to database...'
        )
        for data in self.indeedclient.getjobs():
            if 'id' not in data:
                continue
            job, _ = Jobs.objects.get_or_create(id=data['id'])
            job.id = data.get('id','')
            job.slug = data.get('slug','')
            job.epoch = data.get('epoch','')
            job.date = data.get('date','')
            job.company = data.get('company','')
            job.position = data.get('position','')
            job.description = data.get('description','')
            job.url = data.get('url','')
            job.save()
        logging.info('Jobs successfully pulled from Indeed and stored')


