from apscheduler.schedulers.blocking import BlockingScheduler
import app


schedule = BlockingScheduler()


@schedule.scheduled_job('interval', minute='3')
def populate_database():
    app.populate_database()


schedule.start()
