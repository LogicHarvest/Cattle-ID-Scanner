import cv2
import numpy as np
import urllib.request
from PIL import Image

# Load the pre-trained model
model_url = "https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md#model-zoo-url"
model_path = "ssd_inception_v2_coco_2017_11_17"
model_config_path = f"{model_path}/pipeline.config"
model_weights_path = f"{model_path}/checkpoint/ckpt-0"

# Download the model files
urllib.request.urlretrieve(f"http://download.tensorflow.org/models/object_detection/{model_path}.tar.gz", f"{model_path}.tar.gz")

# Extract the downloaded files
import tarfile
with tarfile.open(f"{model_path}.tar.gz", 'r:gz') as tar:
    tar.extractall()

# Load the model
net = cv2.dnn.readNetFromTensorflow(model_weights_path + "/saved_model.pb", model_config_path)

def detect_cows(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert the image to RGB (OpenCV uses BGR by default)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Get image dimensions
    height, width, _ = image.shape
    
    # Set up the input blob
    blob = cv2.dnn.blobFromImage(rgb_image, size=(300, 300), swapRB=True)
    net.setInput(blob)
    
    # Run the forward pass
    detections = net.forward()
    
    # Loop through the detections
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        
        # If confidence is above a certain threshold (e.g., 0.5)
        if confidence > 0.5:
            class_id = int(detections[0, 0, i, 1])
            
            # Check if the detected object is a cow (class_id for cow is 44)
            if class_id == 44:
                # Scale the bounding box coordinates to the original image size
                box = detections[0, 0, i, 3:7] * np.array([width, height, width, height])
                (startX, startY, endX, endY) = box.astype("int")
                
                # Draw a bounding box around the cow
                cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
                
    # Display the image with bounding boxes
    Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)).show()

# Example usage
image_path = "path/to/your/image.jpg"
detect_cows(image_path)