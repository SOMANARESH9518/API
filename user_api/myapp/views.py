from django.shortcuts import render
from django.http import HttpResponse
from .models import APIUser
from datetime import datetime, timedelta
from user_api import settings


# Create your views here.
def index(request):
    settings.NBR_VISITS += settings.NBR_VISITS
    total_visits = settings.NBR_VISITS
    list_user = APIUser.objects.all()
    day_count = list_user.filter(created_date__gte=datetime.now() - timedelta(hours=24)).count()
    week_count = list_user.filter(created_date__gte=datetime.now() - timedelta(days=7)).count()
    month_count = list_user.filter(created_date__gte=datetime.now() - timedelta(days=30)).count()
    return render(request, 'myapp/index.html',
                  {'list_user': list_user, 'week_count': week_count, 'month_count': month_count,
                   'day_count': day_count, 'total_visits': total_visits})


def searchResults(request):
    username = request.GET.get('username')
    email = request.GET.get('email')
    created_date = request.GET.get('created_date')
    list_user = APIUser.objects.all()
    if username:
        list_user = list_user.filter(username__icontains=username)
    if email:
        list_user = list_user.filter(email__icontains=email)
    if created_date:
        list1 = created_date.split('-')
        # datetime format -- year,month,day
        created_date = datetime(int(list1[0]), int(list1[1]), int(list1[2]))
        list_user = list_user.filter(created_date__lte=created_date + timedelta(days=1),
                                     created_date__gte=created_date - timedelta(days=1))

    return render(request, 'myapp/search_result.html',
                  {'list_user': list_user, 'username': username, 'email':email, 'created_date': created_date})
