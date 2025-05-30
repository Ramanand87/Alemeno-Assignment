from django.core.management.base import BaseCommand
from apis.tasks import ingest_data,reset_sequences

class Command(BaseCommand):
    help = 'Run Excel ingestion directly without Celery'

    def handle(self, *args, **kwargs):
        ingest_data()
        reset_sequences()
