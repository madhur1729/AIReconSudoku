import cv2
import time

vid = cv2.VideoCapture(0)
processing_interval = 1  # seconds
last_processed_time = time.time()  

while True:
    ret, frame = vid.read()

    if not ret:
        break
    
    current_time = time.time()
    
    # Check if it's time to process the frame
    if current_time - last_processed_time >= processing_interval:
        cv2.imshow("solve", frame)
        
        last_processed_time = current_time  # Update the timer
    
    # Display the frame (optional)
    cv2.imshow('Video Frame', frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
