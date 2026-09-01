import numpy as np
import cv2

def sobel_edge_detection(image):
    blurred_img = cv2.GaussianBlur(image, (3, 3), sigmaX=0)
    sobelx = cv2.Sobel(src=blurred_img, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=1) # Sobel Edge Detection on the X axis
    sobely = cv2.Sobel(src=blurred_img, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=1) # Sobel Edge Detection on the Y axis
    sobelxy = cv2.magnitude(sobelx, sobely)
    return sobelxy

def canny_edge_detection(image, threshold_1, threshold_2):
    blurred_img = cv2.GaussianBlur(image, (3, 3), sigmaX=0)
    edges = cv2.Canny(blurred_img, threshold_1, threshold_2)
    return edges

def template_match(image, template):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # make it gray
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY) # make it gray
    w, h = template_gray.shape[::-1]

    res = cv2.matchTemplate(image_gray,template_gray,cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    return image

def resize(image, scale_factor: int, up_or_down: str):
    rows, cols, _channels = map(int, image.shape)

    if up_or_down == "up":
        image = cv2.pyrUp(image, dstsize=(scale_factor * cols, scale_factor * rows))
        print('** Zoom In: Image x scale factor variable')
    elif up_or_down == "down":
        image = cv2.pyrDown(image, dstsize=(cols // scale_factor, rows // scale_factor))
        print('** Zoom Out: Image / scale factor variable')
    else:
        raise ValueError("Not a valid string. Must be 'up' or 'down'")
    return image




def main():
    # Load image
    image = cv2.imread('files/lambo.png')
    if image is None:
        print("Could not find file")
        return

    # Task 1
    result_task1 = sobel_edge_detection(image)
    output_task1 = 'solution/task1.png'
    cv2.imwrite(output_task1, result_task1)
    print(f"Saved sobel image to: {output_task1}")

    cv2.imshow('Sobel Image', result_task1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Task 2
    threshold_1 = 50
    threshold_2 = 50

    result_task2 = canny_edge_detection(image, threshold_1, threshold_2)
    output_task2 = 'solution/task2.png'
    cv2.imwrite(output_task2, result_task2)
    print(f"Saved canny image to: {output_task2}")

    cv2.imshow('Canny Image', result_task2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Task 3
    image = cv2.imread('files/shapes-1.png')
    template = cv2.imread('files/shapes_template.jpg')
    if image is None or template is None:
        print("Could not find all files")
        return
    
    result_task3 = template_match(image, template)
    output_task3 = 'solution/task3.png'
    cv2.imwrite(output_task3, result_task3)
    print(f"Saved template matching image to: {output_task3}")

    cv2.imshow('Template Image', result_task3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Task 4
    scale_factor = 2

    image = cv2.imread('files/lambo.png')
    if image is None:
        print("Could not find file")
        return

    result_task4_up = resize(image, scale_factor, "up")
    result_task4_down = resize(image, scale_factor, "down")
    output_task4_up = 'solution/task4_up.png'
    output_task4_down = 'solution/task4_down.png'
    cv2.imwrite(output_task4_up, result_task4_up)
    cv2.imwrite(output_task4_down, result_task4_down)
    print(f"Saved Resized images to: {output_task4_up} and {output_task4_down}")

    cv2.imshow('Resized Image up', result_task4_up)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imshow('Resized Image down', result_task4_down)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



main()