from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Position(models.Model):
	symbol = models.CharField(max_length=4)
	qty = models.IntegerField()
	price = models.FloatField()

	def __str__(self):
		return '{} share(s) of ${} for ${}'.format(self.qty, self.symbol, self.price)

class Portfolio(models.Model):
	date = models.DateTimeField()
	equity = models.FloatField()
	cash = models.FloatField()

class Trade(models.Model):
	
	class OrderType(models.TextChoices):
		MARKET = 'MRKT', _('Market')
		LIMIT = 'LMT', _('Limit')
		STOP = 'STOP', _('Stop')
		STOPLOSS = 'STLS', _('Stop Loss')

	class TradeSide(models.TextChoices):
		BUY = 'BUY'
		SELL = 'SELL'

	class TimeInForce(models.TextChoices):
		DAY = 'DAY'
		DAYEXT = 'DAYX', _('Day+Extended Hours')
		GTC = 'GTC', _('Good Til Canceled')
		FOK = 'FOK', _('Fill or Kill')
		IOC = 'IOC', _('Immediate or Cancel')
		OPG = 'OPG', _('At-the-Open')
		CLS = 'CLS', _('At-the-Close')

	date_executed = models.DateTimeField()
	order_type = models.CharField(max_length=4, choices=OrderType.choices)
	side = models.CharField(max_length=4, choices=TradeSide.choices)
	time_in_force = models.CharField(max_length=4, choices=TimeInForce.choices)
	position = models.ForeignKey(Position, on_delete=models.DO_NOTHING)

	def __str__(self):
		return '[{}] {} : {} share(s) of ${} for ${}'.format(
			str(self.date_executed)[:19]+' UTC', self.side, self.position.qty, self.position.symbol, self.position.price)


