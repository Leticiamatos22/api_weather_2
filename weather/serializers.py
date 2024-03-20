from rest_framework import serializers
from .models import WeatherEntity

# Definição do Serializer para a entidade WeatherEntity
class WeatherEntitySerializer(serializers.Serializer):
    # Definindo os campos do Serializer
    temperature = serializers.IntegerField()
    date = serializers.CharField()
    city = serializers.CharField(required=False)  # O campo city é opcional
    atmosphericPressure = serializers.CharField(required=False)  # O campo atmosphericPressure é opcional
    humidity = serializers.CharField(required=False)  # O campo humidity é opcional
    weather = serializers.CharField(required=False)  # O campo weather é opcional

    # Método para criar uma nova instância de WeatherEntity a partir de dados validados
    def create(self, validated_data):
        return WeatherEntity(**validated_data)

    # Método para atualizar uma instância existente de WeatherEntity com novos dados
    def update(self, instance, validated_data):
        # Atualizando os campos da instância com os dados validados, se fornecidos
        instance.temperature = validated_data.get('temperature', instance.temperature)
        instance.date = validated_data.get('date', instance.date)
        instance.city = validated_data.get('city', instance.city)
        instance.atmosphericPressure = validated_data.get('atmosphericPressure', instance.atmosphericPressure)
        instance.humidity = validated_data.get('humidity', instance.humidity)
        instance.weather = validated_data.get('weather', instance.weather)
        return instance
