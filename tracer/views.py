from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from tracer.forms import DreamForm
from tracer.models import Dream, Locations, Themes

def dreamform(request):
    template = loader.get_template('dreamform.html')
    if request.method=="POST":
        form = DreamForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            Dream(
                user=request.user
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                rating = form.cleaned_data['rating']
            )
            dreamlocations = Locations(dream=Dream)
            for location in locations:
                dreamlocations.tags.add(location)
            dreamthemes = Themes(dream=dream)
            for theme in themes:
                dreamthemes.tags.add(theme)
            Dream.save()
            save_m2m()
            return HttpResponseRedirect('login')
    else:
        form = DreamForm()
        context = {'form': form}
    return HttpResponse(template.render(context , request))
