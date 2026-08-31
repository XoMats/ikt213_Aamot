import numpy as np
import cv2
    

def padding(image, border_width):
    reflect = cv2.copyMakeBorder(image,border_width,border_width,border_width,border_width, cv2.BORDER_REFLECT)
    return reflect

def crop(image, x_0, x_1,  y_0, y_1):
    cropped_image = image[y_0:y_1, x_0:x_1]
    return cropped_image

def resize(image, width, height):
    resized = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)
    return resized

def copy(image, emptyPictureArray):
    width = image.shape[1]
    height = image.shape[0]
    channels = image.shape[2]

    for y in range(height):
        for x in range(width):
            for c in range(channels):
                emptyPictureArray[y, x, c] = image[y, x, c]
    return emptyPictureArray

def grayscale(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray

def hsv(image):
    hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    return hsvImage

def hue_shifted(image, emptyPictureArray, hue):
    width = image.shape[1]
    height = image.shape[0]
    channels = image.shape[2]

    for y in range(height):
        for x in range(width):
            for c in range(channels):
                emptyPictureArray[y, x, c] = (int(image[y, x, c]) + hue) % 256

    return emptyPictureArray

def smoothing(image):
    smooth = cv2.GaussianBlur(image, (15, 15), sigmaX=0, borderType=cv2.BORDER_DEFAULT)
    return smooth

def rotation(image, rotation_angle):
    if rotation_angle == 90:
        rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        return rotated
    if rotation_angle == 180:
        rotated = cv2.rotate(image, cv2.ROTATE_180)
        return rotated
    else:
        print("Not a valid number")
        return








def main():
    # Load image
    image = cv2.imread('files/iris-1.png')
    if image is None:
        print("Could not find file")
        return

    # task 1
    border_width = 100
    result_task1 = padding(image, border_width)

    output_task1 = 'solution/task1.png'
    cv2.imwrite(output_task1, result_task1)
    print(f"Saved padded image to: {output_task1}")
    
    cv2.imshow('Padded Image', result_task1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # task 2
    frame_width = image.shape[1]
    frame_height = image.shape[0]
    #print(frame_height, frame_width)
    
    x_0, x_1, y_0, y_1 = 200, frame_width - 130, 200, frame_height - 130
    result_task2 = crop(image, x_0, x_1, y_0, y_1)

    output_task2 = 'solution/task2.png'
    cv2.imwrite(output_task2, result_task2)
    print(f"Saved padded image to: {output_task2}")

    cv2.imshow('Cropped Image', result_task2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # task 3
    width, height = 200, 200
    result_task3 = resize(image, width, height)

    output_task3 = 'solution/task3.png'
    cv2.imwrite(output_task3, result_task3)
    print(f"Saved padded image to: {output_task3}")

    cv2.imshow('Resized Image', result_task3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # task 4
    height, width, channels = image.shape
    emptyPictureArray = np.zeros((height, width, 3), dtype=np.uint8)
    result_task4 = copy(image, emptyPictureArray)
    
    output_task4 = 'solution/task4.png'
    cv2.imwrite(output_task4, result_task4)
    print(f"Saved copied image to: {output_task4}")

    cv2.imshow('Copied Image', result_task4)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # task 5
    result_task5 = grayscale(image)
    output_task5 = 'solution/task5.png'
    cv2.imwrite(output_task5, result_task5)
    print(f"Saved padded image to: {output_task5}")

    cv2.imshow('Grayscaled Image', result_task5)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # task 6
    result_task6 = hsv(image)
    output_task6 = 'solution/task6.png'
    cv2.imwrite(output_task6, result_task6)
    print(f"Saved hsv image to: {output_task6}")

    cv2.imshow('Hsv Image', result_task6)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # task 7
    hue = 50
    emptyPictureArray = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)

    result_task7 = hue_shifted(image, emptyPictureArray, hue)
    output_task7 = 'solution/task7.png'
    cv2.imwrite(output_task7, result_task7)
    print(f"Saved hue image to: {output_task7}")

    cv2.imshow('Hue Image', result_task7)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # task 8
    result_task8 = smoothing(image)
    output_task8 = 'solution/task8.png'
    cv2.imwrite(output_task8, result_task8)
    print(f"Saved smooth image to: {output_task8}")

    cv2.imshow('Smooth Image', result_task8)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # task 9
    rotation_angle = 180

    result_task9 = rotation(image, rotation_angle)
    output_task9 = 'solution/task9.png'
    cv2.imwrite(output_task9, result_task9)
    print(f"Saved rotated image to: {output_task9}")

    cv2.imshow('Rotated Image', result_task9)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()