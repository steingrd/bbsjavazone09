#!/usr/bin/env python

from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect

from models import Player
from forms import RegisterPlayerForm, RegisterResultForm

def register_player(request):
    if request.method == 'POST':
        try:
            player = Player.objects.get(email=request.POST['email'])
            return HttpResponseRedirect('/darts/your_score/?email='+player.email) # TODO reverse()
        except Player.DoesNotExist:
            pass
        
        form = RegisterPlayerForm(request.POST)
        if form.is_valid():
            player = form.save()
            return HttpResponseRedirect('/darts/throw_darts/?email='+player.email) # TODO reverse()
            
    else:
        form = RegisterPlayerForm()
        
    context = { 'form': form }
    return render_to_response('darts/register_player.html', context)


def register_result(request):
    player = get_object_or_404(Player, email=request.GET['email'])
    
    if request.method == 'POST':
        form = RegisterResultForm(request.POST)
        if form.is_valid():
            form.save(player=player)
            return HttpResponseRedirect('/darts/your_score/?email='+player.email) # TODO reverse()
            
    else:
        form = RegisterResultForm()
        
    context = { 'form': form, 'player': player }
    return render_to_response('darts/register_result.html', context)
    
    
def your_score(request):
    player = get_object_or_404(Player, email=request.GET['email'])
    context = { 'player': player }
    return render_to_response('darts/your_score.html', context)