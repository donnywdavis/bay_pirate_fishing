import datetime
from django.shortcuts import render
from schedule.models import Event


def home(request):
    """
    This is the route for the home page of the site.

    :param request: Data passed in from the browser
    :return: Render the template to the browser.
    """

    events = Event.objects.filter(end_date__gte=datetime.date.today())[:3]
    context = {
        'events': events
    }

    return render(request, 'index.html', context)


def about(request):
    """
    This is the route for the about page.

    :param request: Data passed in from the browser
    :return: Render the template to the browser.
    """

    return render(request, 'about.html', {})
