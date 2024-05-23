from apscheduler.schedulers.background import BackgroundScheduler
from frcmApp import views

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(views.dataScheduling, trigger='interval', hour=24,id="data_001",replace_existing=True)
    scheduler.start()
