from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import os


def save_image(img_name, image):
    
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Obtener la ruta a la carpeta static/images
    static_images_dir = os.path.join(root_path, 'static/', 'images')

    # Crear el directorio si no existe
    if not os.path.exists(static_images_dir):
        os.makedirs(static_images_dir)

    # Crear la ruta de destino para guardar la imagen
    destination_path = os.path.join(static_images_dir, img_name)

    # Guardar la imagen en la carpeta static/images
    with open(destination_path, 'wb') as destination:
        destination.write(image.read())


def modelos_keras(img_name, model_selected):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)
    
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    static_path = os.path.join(root_path, 'static')

    # Load the model
    model = load_model(static_path+"/models/"+model_selected+"/keras_Model.h5", compile=False)

    # Load the labels
    class_names = open(static_path+"/models/"+model_selected+"/labels.txt", "r").readlines()

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open(static_path+"/images/"+img_name).convert("RGB")

    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", int(confidence_score*100))
    
    return class_name[2:], confidence_score
