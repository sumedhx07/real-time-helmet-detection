from ultralytics import YOLO

# Load a pretrained YOLO model
model = YOLO("yolo11n.pt")

# Run YOLO on an image
results = model("https://ultralytics.com/images/bus.jpg")

# Display the result
results[0].show()