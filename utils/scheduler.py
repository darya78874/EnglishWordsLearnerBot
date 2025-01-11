import schedule

import time

import threading

def job():

    print("Это сообщение выдано по расписанию!")

def run_scheduler():

    schedule.every().day.at("10:00").do(job)

    while True:

        schedule.run_pending()

        time.sleep(1)

def start_scheduler():

    thread = threading.Thread(target=run_scheduler)

    thread.start()
