from django.shortcuts import render
import os

# Create your views here.
def app(request):
    """
    Main view to render the Vue.js app.
    """
    context = {
        'environment': os.environ.get('NODE_ENV'),
        'email': 'some_email@aol.com',
        'api_key': 'some key from os.environ or django.conf.settings',
        # etc...
    }
    return render(request=request, template_name='vue.html', context=context)
