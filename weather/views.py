from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import WeatherEntitySerializer
from .models import WeatherEntity
from .repositories import WeatherRepository
from datetime import datetime

# View para gerar dados de clima
class WeatherGenerate(APIView):
    # Método para tratar requisições GET
    def get(self, request):
        # Criando uma instância do serializer com dados fornecidos
        serializer = WeatherEntitySerializer(data={
            "temperature": 28,
            "date": str(datetime.now().date())  # Obtendo a data atual
        })
        # Verificando se os dados são válidos
        if serializer.is_valid():
            # Se forem válidos, obtém os dados validados
            data = serializer.validated_data
            # Criando uma instância do repositório WeatherRepository
            repository = WeatherRepository(collectionName='weathers')
            # Inserindo os dados no repositório
            repository.insert(data)
            # Retornando os dados serializados
            return Response(serializer.data)
        # Se os dados não forem válidos, retorna os erros
        return Response(serializer.errors, status=400)
