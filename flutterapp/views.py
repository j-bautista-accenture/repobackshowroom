from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializer import CompVisionFSerializer
from .models import CompVisionF
from .utils import modelos_keras, save_image

class CompVisionFViewSet(ModelViewSet):
    queryset = CompVisionF.objects.all()
    serializer_class = CompVisionFSerializer

    @action(detail=False, methods=['post'])
    def process_image(self, request):
        # Recuperar los datos de la petición
        img_name = request.data.get('imageName')
        image = request.data.get('image')
        model_selected = request.data.get('modelSelected')

        # Verificar si se han proporcionado todos los datos necesarios
        if not image or not model_selected or not img_name:
            return Response({"error": "Se requiere una imagen y un modelo seleccionado"}, status=status.HTTP_400_BAD_REQUEST)
        
        #guardamos la imagen en la ruta raiz
        save_image(img_name, image)

        #aplicamos el modelo de keras a la imagen
        class_name, confidence_score = modelos_keras(img_name, model_selected)

        # Devuelve una respuesta exitosa
        return Response({
            "class_name": class_name,
            "confidence_score": confidence_score,
            }, status=status.HTTP_200_OK)