# coding=utf-8

import datetime

from django.shortcuts import render
from django.utils.timezone import now


def home(request):
    """Index page

    Args:
        request: HTTP request

    Returns:
        Index page render
    """
    today = datetime.date.today()
    return render(request, 'taskbuster/index.html',
                  {'today': today, 'now': now()})


def home_files(request, filename):
    """Render file

    Args:
        request: HTTP request
        filename (str): file name (ex. robots.txt)

    Returns:
        Given file render
    """
    return render(request, filename, {}, content_type='text/plain')
