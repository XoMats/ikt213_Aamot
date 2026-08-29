import numpy as np
import cv2

def print_image_information():
    # Load an color image
    img = cv2.imread('files/iris-1.jpg')
    print("Height:", img.shape[0])
    print("Width:", img.shape[1])
    print("Channels:", img.shape[2])
    print("Size:", img.size)
    print("Data type:", img.dtype)


def camera():
    # Open the default camera
    cam = cv2.VideoCapture(0)

    # Get camera information
    fps = cam.get(cv2.CAP_PROP_FPS)
    frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Save the camera information
    with open("solutions/camera_outputs.txt", "w") as file:
        file.write(f"fps: {fps}\n")
        file.write(f"height: {frame_height}\n")
        file.write(f"width: {frame_width}\n")

    while True:
        ret, frame = cam.read()

        # Press 'q' to exit the loop
        if cv2.waitKey(1) == ord("q"):
            break

    # Release the camera
    cam.release()
    cv2.destroyAllWindows()




def main():
    print_image_information()
    #camera()


main()