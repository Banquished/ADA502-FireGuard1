from django.apps import AppConfig


class FrcmappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'frcmApp'

    def ready(self):
        print("Starting Scheduler ...")
        from .data_scheduler import data_updater
        data_updater.start()
