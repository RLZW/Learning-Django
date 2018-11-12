"""Platzigram Views"""

# Django
from django.http import HttpResponse
from django.http import JsonResponse

# Utilities
from datetime import datetime
import json

# Debugging
import pdb

DEBUG_MODE = False

# EXAMPLE OF REQUEST IN SORT VIEW sort URL   ?numbers=10,4,50,32


def hello_word(request):
    """Returns a greeting"""
    print(f'El esquema con el que se pidio fue {request.scheme}')
    now = datetime.now().strftime('%b %dth, %Y -%H:%M hrs')
    string = f'Oh, hi!, Current server time is {str(now)}'

    _isDebug
    return HttpResponse(string)


def _isDebug():
    global DEBUG_MODE
    if DEBUG_MODE:
        pdb.set_trace()


def sort(request):
    """Return a JSON Response with sorted integers"""

    print(f'El esquema con el que se pidio fue {request.scheme}')
    numbers = request.GET['numbers']
    sortedNumbers = sorted([int(i) for i in numbers.split(',')])

    data = {
        'Status': 'ok',
        'numbers': numbers,
        'sorted': sortedNumbers,
        'message': 'Integers sorted succesfully.'}

    response = JsonResponse(data, json_dumps_params={'indent': 2})

    _isDebug
    return response


def say_hi(request, name, age):
    """Checks age"""
    if age < 12:
        message = f'Sorry {name}, you are not allowed here'
    else:
        message = f'Hey {name} welcome to the proyect'

    _isDebug
    return HttpResponse(message)
