# from doctest import master
from apscheduler.schedulers.background import BackgroundScheduler
from .views import Schedule

def start():
  scheduler = BackgroundScheduler()
  base1 = Schedule()
  scheduler.add_job(base1.get_queryset, "interval", minutes=1)
  scheduler.start()