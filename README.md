# Machine Learning Engineer Test: Computer Vision and Object Detection

## Objective
This test aims to assess your skills in computer vision and object detection, with a specific focus on detecting room walls and identifying rooms in architectural blueprints or pre-construction plans.

This test evaluates your practical skills in applying advanced computer vision techniques to a specialized domain and your ability to integrate machine learning models into a simple API server for real-world applications.

Choose one of the visual tasks, one of the text extraction tasks, and the API Server task. We encourage you to submit your tests even if you can’t complete all tasks.

Good luck!


## Full test description
[Senior Machine Learning Engineer.pdf](https://github.com/user-attachments/files/16702909/Senior.Machine.Learning.Engineer.pdf)


## PS
Share your project with the following GitHub users:
- vhaine-tb
- gabrielreis-tb

## Example cURL
```
curl -X POST -F "image=@extracted_page_xyz.png" "http://localhost:3000/run-inference?type=wall"
curl -X POST -F "image=@extracted_page_xyz.png" "http://localhost:3000/run-inference?type=room"
curl -X POST -F "image=@extracted_page_xyz.png" "http://localhost:3000/run-inference?type=page_info"
curl -X POST -F "image=@extracted_page_xyz.png" "http://localhost:3000/run-inference?type=tables"
```
