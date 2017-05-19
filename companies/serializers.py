from rest_framework import serializers
from .models import Stock


class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        # to include some fields = ('ticker', 'volume')
        # to include all attributes from model use this -->
        fields = '__all__'


