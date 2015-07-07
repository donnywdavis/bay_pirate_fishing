from django.shortcuts import render


def home(request):
    """
    This is the route for the home page of the site.

    :param request: Data passed in from the browser
    :return: Render the template to the browser.
    """

    return render(request, 'index.html', {})


def about(request):
    """
    This is the route for the about page.

    :param request: Data passed in from the browser
    :return: Render the template to the browser.
    """

    return render(request, 'about.html', {})
