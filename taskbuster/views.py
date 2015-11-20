# coding=utf-8

import datetime

from django.shortcuts import render
from django.utils.timezone import now


def home(request):
    """Index page view

    :param request: HTTP request
    :return: index page render
    """
    today = datetime.date.today()
    return render(request, 'taskbuster/index.html',
                  {'today': today, 'now': now()})


def home_files(request, filename):
    """File view (robots.txt and humans.txt

    :param request: HTTP request
    :param filename: humans.txt or robots.txt
    :return: file render
    """
    return render(request, filename, {}, content_type='text/plain')
