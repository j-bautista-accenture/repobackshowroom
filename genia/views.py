from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializer import GenIASerializer
from .models import GenIA

class GenIAViewSet(ModelViewSet):
    queryset = GenIA.objects.all()
    serializer_class = GenIASerializer

    @action(detail=False, methods=['post'])
    def consulta(self, request):
        # Recuperar los datos de la petición
        prompt = request.data.get('prompt')

        # Verificar si se han proporcionado todos los datos necesarios
        if not prompt:
            return Response({"error": "Se requiere un prompt"}, status=status.HTTP_400_BAD_REQUEST)

        # Aquí puedes agregar la lógica para procesar la imagen y el modelo seleccionado
        # Por ejemplo, puedes usar la biblioteca keras para procesar la imagen con el modelo seleccionado

        # Devuelve una respuesta exitosa
        return Response({"message": "Respuesta del prompt"}, status=status.HTTP_200_OK)