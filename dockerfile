FROM ultralytics/ultralytics:8.2.11-python

WORKDIR /analytic

RUN yolo export model=yolov8m.pt format=openvino

COPY . .

# Run inference with the exported model
ENTRYPOINT [ "main.py"]