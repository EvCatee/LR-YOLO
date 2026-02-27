import warnings, os
warnings.filterwarnings('ignore')
from ultralytics import YOLO
if __name__ == '__main__':
    model = YOLO('yolo11')
    model.load('yolo11n.pt') 
    model.train(data='dataset/data.yaml',
                cache=False,
                imgsz=640,
                epochs=300,
                batch=16,
                close_mosaic=10,
                workers=4, 
                device='0'
                project='runs/train',
                name='LR_yolo_experiment',
                )