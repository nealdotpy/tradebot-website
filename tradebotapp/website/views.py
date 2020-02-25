from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect

#from .forms import NewTopicForm
#from django.http import HttpResponse
from .models import Trade, Position, Portfolio

# Create your views here.
def home(request):
	trades = Trade.objects.all()
	return render(request, 'home.html', {'trades': trades})
	#print('Hello World!')

def source(request):
	return redirect('https://github.com/nealdotpy/tradebot-website') # less clicks the better :)


def dashboard(request):
	return render(request, 'dashboard.html')