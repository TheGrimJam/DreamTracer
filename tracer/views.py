from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import loader
from tracer.forms import DreamForm
from tracer.models import Dream

def dreamform(request):
    template = loader.get_template('tracer/dreamform.html')
    if request.method=="POST":
        form = DreamForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            user=request.user
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            rating = form.cleaned_data['rating']
            date = form.cleaned_data['date']
            location = form.cleaned_data['location']
            theme_tags = form.cleaned_data['theme']
            dream_instance = Dream(
                user=user,
                title=title,
                description=description,
                date=date,
                rating=rating,
                location=location,
            )
            dream_instance.save()
            for theme_tag in theme_tags:
                dream_instance.theme.add(theme_tag)
            return HttpResponseRedirect(reverse('auth_login'))
    else:
        form = DreamForm()
        context = {'form': form}
    return HttpResponse(template.render(context , request))

def userdreams(request):
    template = loader.get_template('tracer/userdreams.html')
    dreams_query = Dream.objects.filter(user=request.user).order_by('-date')
    context = {'dreams_query': dreams_query}
    return HttpResponse(template.render(context , request))
