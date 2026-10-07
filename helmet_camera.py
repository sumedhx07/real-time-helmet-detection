import cv2
from ultralytics import YOLO

# Load our trained helmet model
model = YOLO("runs/detect/train/weights/best.pt")

# Open camera
camera = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

if not camera.isOpened():
    print("Could not open camera")
    exit()

print("Helmet tracking started.")
print("Press 'q' to quit.")

while True:
    success, frame = camera.read()

    if not success:
        print("Could not read frame")
        break

    # Run YOLO tracking
    results = model.track(
        frame,
        persist=True,
        verbose=False
    )

    result = results[0]

    # Draw detections and tracking IDs
    annotated_frame = result.plot()

    # Display
    cv2.imshow("Helmet Tracking", annotated_frame)

    # Quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()

print("Helmet tracking stopped.")