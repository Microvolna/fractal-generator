import matplotlib.pyplot as plt
from loguru import logger
import os
import cv2
import time

IMG_SIZE = (2000, 2000)
FOLDER = "images"

OUTPUT = 'fractal.png'

data = []
labels = []

def create_data():
    logger.info(f'Размер изображения - {IMG_SIZE[0]}x{IMG_SIZE[1]}')
    logger.info(f'Папка с датасетом - {FOLDER}')

    data_dir = os.path.abspath(os.getcwd())
    path = os.path.join(data_dir, FOLDER)

    for image in os.listdir(path):
        temp_path = os.path.join(path, image)
 
        img_array = cv2.imread(os.path.join(path, image))
        new_array = cv2.resize(img_array, IMG_SIZE)
        label = temp_path.split(os.path.sep)[-2]
        labels.append(label)
        data.append(new_array)

create_data()
plt.imsave(OUTPUT, data[2])
logger.info(f'Успешно сохранено в файл {OUTPUT}')
time.sleep(5)