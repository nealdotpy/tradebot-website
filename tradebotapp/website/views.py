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
	if request.method == 'GET':
		ticker = request.GET.get('ticker')
		print('*!*!*!*!*!*!*\nYou requested information for: {}\n*!*!*!*!*!*!*'.format(ticker))

		positions_matching_ticker = Position.objects.all().filter(symbol=ticker.upper())
		trades_matching_ticker = []

		for position in positions_matching_ticker:
			trades_matching_ticker.append(str(Trade.objects.all().filter(position=position)))

		#print('{}'.format(trades_matching_ticker))

	return render(request, 'home.html', {'trades': trades_matching_ticker})