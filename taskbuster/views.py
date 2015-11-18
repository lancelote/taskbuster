# coding=utf-8

from django.shortcuts import render


def home(request):
    """Index page

    Args:
        request: HTTP request

    Returns:
        Index page render
    """
    return render(request, 'taskbuster/index.html', {})


def home_files(request, filename):
    """Render file

    Args:
        request: HTTP request
        filename (str): file name (ex. robots.txt)

    Returns:
        Given file render
    """
    return render(request, filename, {}, content_type='text/plain')
