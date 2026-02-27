import warnings
from sympy.printing.pretty.pretty_symbology import line_width
warnings.filterwarnings('ignore')
from ultralytics import YOLO
if __name__ == '__main__':
    model = YOLO('runs/train/XX/weights/best.pt') 
    model.val(data='dataset/data.yaml',
              split='test',
              imgsz=640,
              batch=16,
              # iou=0.6,
              # rect=False,
              # show_conf=False, 
              line_width=1, 
              project='runs/val',
              name='LR_yolo_results',
              plots=True,
              )