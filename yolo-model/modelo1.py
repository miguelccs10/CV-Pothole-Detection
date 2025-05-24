from ultralytics import YOLO

model = YOLO('model/yolo_em_casa_portugues.pt')

results = model(source='videos/20250509_163434.mp4', show= False, conf=0.4, save= True)