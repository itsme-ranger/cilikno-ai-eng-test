# AI Engineer test Summary

Candidate: Ramadhan Gerry Akbar

## How to Run

1. Setup image/video on a specific folder
2. run `docker run -it --rm -v <path-in-container>:<path-in-host> ranger14/cilikno-aieng-test:latest --source <source-in-container> --target <target-path-in-container>`
3. If want to run with GPU machine, you can run with the same command as 2 or with GPU flag
    `docker run -it --rm --gpus all -v <path-in-container>:<path-in-host> ranger14/cilikno-aieng-test:latest --source <source-in-container> --target <target-path-in-container>`
    , although that would not improve any performance whatsoever

## Solution Explanations

1. Ultralytics offered YOLOv8 with end-to-end fashion, which covers lots of part in this task. The only part that not being covered is the post processing, which outputs image/video with bounding box on it. I choose OpenVINO inference engine since they offered a significant improvement of improvement time (approx 2 times faster than default mode). Also, OpenVINO model can run in a machine with GPU on it
2. I choose `ultralytics/ultralytics:8.2.11-python`. Sure, We can choose other but they also come with disadvantage such as bigger image size
3. Assuming there is enough time, automated testing would be better which tests on various video format, size, image format, no object, single object inside, multiple objects, etc. But for preliminary test, We can do manual test such as
   1. one video with multiple kind of objects
   2. three images:
      1. No interesting object
      2. One object
      3. mMultiple objects
   3. Run on few different machines such as one with CPU only and one with GPU
4. Although OpenVINO can be run on GPU, there are way better engines that provide better inference time and resource management, such as TensorRT