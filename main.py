from ultralytics import YOLO
import argparse
import cv2

parser = argparse.ArgumentParser()

parser.add_argument(
    "--name", action="store"
)  # Equivalent to parser.add_argument("--name")
parser.add_argument("--source, -s")
parser.add_argument("--target, -t")

args = parser.parse_args()

# Load the exported OpenVINO model
ov_model = YOLO('yolov8m_openvino_model/')

# Run inference
results = ov_model(args.source)
boxes = result[0].boxes.cpu().numpy()
img = cv2.imread(args.source)
cv2.imwrite(target, img)