from ultralytics import YOLO

# Load the pretrained YOLO model
model = YOLO("yolo11n.pt")

# Train it on our helmet dataset
model.train(
    data="helmet_dataset/data.yaml",
    epochs=10,
    imgsz=640,
    batch=8
)