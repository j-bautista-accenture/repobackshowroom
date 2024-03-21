from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializer import CompVisionUSerializer
from .models import CompVisionU

class CompVisionUViewSet(ModelViewSet):
    queryset = CompVisionU.objects.all()
    serializer_class = CompVisionUSerializer

    @action(detail=False, methods=['post'])
    def process_image(self, request):
        # Serializar los datos del cuerpo de la solicitud
        serializer = CompVisionUSerializer(data=request.data)

        # Verificar si los datos son válidos
        if serializer.is_valid():
            # Guardar los datos procesados en la base de datos o realizar otras operaciones necesarias
            processed_data = serializer.validated_data
            # Aquí puedes acceder a processed_data['images'] para obtener la lista de imágenes procesadas
            # Realiza las operaciones necesarias con las imágenes
            
            # Devolver una respuesta exitosa
            return Response({"message": "Imágenes procesadas exitosamente"}, status=status.HTTP_200_OK)
        else:
            # Si los datos no son válidos, devolver los errores de validación
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)