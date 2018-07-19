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
    week_count = list_user.filter(created_date__gte=datetime.now() - timedelta(days=7)).count()
    month_count = list_user.filter(created_date__gte=datetime.now() - timedelta(days=30)).count()
    year_count = list_user.filter(created_date__gte=datetime.now() - timedelta(days=365)).count()
    return render(request, 'myapp/index.html',
                  {'list_user': list_user, 'week_count': week_count, 'month_count': month_count,
                   'year_count': year_count, 'total_visits': total_visits})
