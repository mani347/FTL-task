from django.db import models


class Users(models.Model):
    real_name = models.CharField(max_length=100)
    time_format = models.CharField(max_length=100)

    class Meta:
        db_table = "users"


class ActivityPeriods(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        db_table = "activity_periods"
