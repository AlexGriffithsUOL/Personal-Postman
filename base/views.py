from django.shortcuts import render
from django.views import View
from api.models import api_call

# Create your views here.
class index(View):
    def get(self, request):
        calls = api_call.objects.all()
        return render(request, "base/index.html", { 'api_calls' : calls })
