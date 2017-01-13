from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from tracer.forms import DreamForm
from tracer.models import Dream

def dreamform(request):
    template = loader.get_template('dreamform.html')
    if request.method=="POST":
        form = DreamForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            user=request.user
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            rating = form.cleaned_data['rating']
            location = form.cleaned_data['location']
            theme = form.data['theme']
            Dream.objects.create(
                user=user,
                title=title,
                description=description,
                rating=rating,
                location=location,
                theme=theme
            )
            return HttpResponseRedirect('login')
    else:
        form = DreamForm()
        context = {'form': form}
    return HttpResponse(template.render(context , request))
