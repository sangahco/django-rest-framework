from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.debug import sensitive_variables, sensitive_post_parameters
from django.db.models import Q

@login_required
def index(request):
    return render(request, 'index.html')

def sampleJson(request):
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    return JsonResponse(data)