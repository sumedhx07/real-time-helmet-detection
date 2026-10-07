import cv2
from ultralytics import YOLO

# Load the pretrained YOLO model
model = YOLO("yolo11n.pt")

# Open the camera
camera = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

if not camera.isOpened():
    print("Could not open camera")
    exit()

print("YOLO camera detection started.")
print("Press 'q' to quit.")

while True:
    # Read a frame
    success, frame = camera.read()

    if not success:
        print("Could not read frame")
        break

    # Run YOLO on the frame
    results = model(frame, verbose=False)

    # Draw detections on the frame
    annotated_frame = results[0].plot()

    # Display the result
    cv2.imshow("YOLO Camera Detection", annotated_frame)

    # Quit when q is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Clean up
camera.release()
cv2.destroyAllWindows()

print("Camera stopped.")