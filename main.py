import cv2

# Open the camera
camera = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

# Check if the camera opened successfully
if not camera.isOpened():
    print("Could not open camera")
    exit()

print("Camera opened successfully!")
print("Press 'q' to quit.")

while True:
    # Read a frame from the camera
    success, frame = camera.read()

    if not success:
        print("Could not read frame")
        break

    # Show the camera feed
    cv2.imshow("Helmet Detection - Camera", frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the camera
camera.release()

# Close all OpenCV windows
cv2.destroyAllWindows()