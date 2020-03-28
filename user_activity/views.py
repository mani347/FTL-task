from django.http import JsonResponse
from user_activity.models import ActivityPeriods, Users


def view(request):
    final_data = dict()
    try:
        users = Users.objects.all()
        final_data['ok'] = True
        final_data['members'] = []
        for user in users:
            data = dict()
            id = user.pk
            real_name = user.real_name
            tz = user.time_format
            data['id'] = id
            data['real_name'] = real_name
            data['tz'] = tz
            data['activity_periods'] = []
            activity_periods = ActivityPeriods.objects.filter(user=user)
            for activity_period in activity_periods:
                d = dict()
                start_time = activity_period.start_time
                end_time = activity_period.end_time
                start_time = start_time.strftime("%b %d %Y %I:%M%P")
                end_time = end_time.strftime("%b %d %Y %I:%M%P")
                d['start_time'] = start_time
                d['end_time'] = end_time
                data['activity_periods'].append(d)
            final_data['members'].append(data)
    except Exception as e:
        print("something went wrong: " + str(e))
        final_data['ok'] = False
    return JsonResponse(final_data)
