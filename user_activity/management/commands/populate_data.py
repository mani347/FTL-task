from django.core.management.base import BaseCommand
from user_activity.models import Users, ActivityPeriods
from datetime import datetime, timedelta


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            u1 = Users(real_name='Egon Spengler', time_format='America/Los_Angeles')
            u1.save()
            u2 = Users(real_name='Glinda Southgood', time_format='Asia/Kolkata')
            u2.save()
            now = datetime.now()
            a1u1 = ActivityPeriods(user=u1, start_time=now, end_time=now + timedelta(minutes=30))
            a2u1 = ActivityPeriods(user=u1, start_time=now + timedelta(minutes=30), end_time=now + timedelta(minutes=60))
            a3u1 = ActivityPeriods(user=u1, start_time=now + timedelta(minutes=60), end_time=now + timedelta(minutes=90))
            a1u1.save()
            a2u1.save()
            a3u1.save()

            a1u2 = ActivityPeriods(user=u2, start_time=now, end_time=now + timedelta(minutes=30))
            a2u2 = ActivityPeriods(user=u2, start_time=now + timedelta(minutes=30), end_time=now + timedelta(minutes=60))
            a3u2 = ActivityPeriods(user=u2, start_time=now + timedelta(minutes=60), end_time=now + timedelta(minutes=90))
            a1u2.save()
            a2u2.save()
            a3u2.save()
            print("Data  Populated.")
        except Exception as e:
            print("Something went wrong: " + str(e))
