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

def search_ticker(request):
	ticker = request.GET.get('ticker')
	if request.method == 'GET':
		print('*!*!*!*!*!*!*\nYou requested information for: {}\n*!*!*!*!*!*!*'.format(ticker))

	position_matching_ticker = Position.objects.all().filter(symbol=ticker)
	trades_matching_ticker = position_matching_ticker#Trade.objects.all().filter(position=())

	print('{}'.format(trades_matching_ticker))

	return render(request, 'home.html', {'trades': trades_matching_ticker})