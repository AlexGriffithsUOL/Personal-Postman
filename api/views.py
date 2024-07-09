from django.shortcuts import render
from django.views import View
from .models import api_call
from django.shortcuts import get_object_or_404

# Create your views here.
class api_details(View):
    def __init__(self):
        self.name = 'API Details'
        self.template = 'api/details.html'

    def get(self, request, api_call_id):
        call = get_object_or_404(api_call, pk=api_call_id)
        return render(request, self.template, { 'api_call': call })