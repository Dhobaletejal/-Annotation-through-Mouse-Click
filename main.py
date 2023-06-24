import cv2

# Load the image
image = cv2.imread("Task_1.jpg")

# Create a window to display the image
cv2.namedWindow("Image")
cv2.imshow("Image", image)

# Mouse event callback function
def mouse_callback(event, x, y, flags, param):
    global tl_pt, br_pt

    if event == cv2.EVENT_LBUTTONDOWN:
        tl_pt = (x, y)  # Record top left point
    elif event == cv2.EVENT_LBUTTONUP:
        br_pt = (x, y)  # Record bottom right point

        # Draw a rectangle on the image
        cv2.rectangle(image, tl_pt, br_pt, (0, 255, 0), 2)
        cv2.putText(image, f"TL: {tl_pt}", (tl_pt[0], tl_pt[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.putText(image, f"BR: {br_pt}", (br_pt[0], br_pt[1] + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Crop the image
        cropped_image = image[tl_pt[1]:br_pt[1], tl_pt[0]:br_pt[0]]

        # Save the cropped image
        cv2.imwrite("Task_1_cropped.jpg", cropped_image)

        # Save the insights image
        cv2.imwrite("Task_1_insights.jpg", image)

        # Display the insights image
        cv2.imshow("Insights", image)

# Set the mouse callback function for the image window
cv2.setMouseCallback("Image", mouse_callback)

# Wait for the user to close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
