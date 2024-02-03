# Real-Time Traffic Vehicle Detection using YOLOv8 (with Custom Dataset)

## Overview

This project aims to create a real-time traffic detection system using YOLOv8, a powerful object detection algorithm. The system is trained with a custom dataset, integrates OpenCV for live camera feed, and is deployed on a webpage for easy accessibility.

## Output
![image0](https://github.com/Kamal934/RealTime-Traffic-vehicle-detection/assets/110932441/765cb2c2-ecaf-4971-9602-fcbde03998c1)

### Key Features

1. **Real-Time Detection:** Utilizing the YOLOv8 architecture, the system can detect and track vehicles in real-time, making it suitable for traffic monitoring and safety applications.

2. **Custom Dataset Training:** The YOLOv8 model is trained on a custom dataset, allowing for adaptability to specific traffic conditions, diverse environments, and various vehicle types.

3. **Live Camera Feed with OpenCV:** The system integrates OpenCV to capture and process live video streams from a webcam, providing real-time input for the traffic detection model.

4. **Webpage Deployment:** The trained model is deployed on a webpage, offering a user-friendly interface for accessing real-time traffic detection results.

### Dataset Acquisition

The convenient ways to obtain the custom dataset for training:
- **Download from Kaggle:** Obtain the dataset from Kaggle by visiting [Kaggle Dataset Link]((https://www.kaggle.com/datasets/saumyapatel/traffic-vehicles-object-detection)).

### Training Process

1. **Google Colab Setup:** Open the notebook `train_yolov8_google_colab.ipynb` in Google Colab to set up the training environment.

2. **Dataset Upload:** Upload the custom dataset to Google Colab, following the guidelines in the notebook.

3. **Training:** Execute the notebook cells to initiate the YOLOv8 training process. Customize hyperparameters and configurations as needed.

### Live Camera Feed

1. **OpenCV Integration:** Use OpenCV to capture live video from a webcam. Modify the script according to your camera setup.

2. **Real-Time Inference:** Feed the live frames into the trained YOLOv8 model for real-time traffic detection.

### Webpage Deployment

1. **Web Interface:** Deploy the model on a webpage using HTML, CSS, and JavaScript to create an interactive and user-friendly interface.

2. **Real-Time Display:** Showcase the live camera feed and YOLOv8 detection results on the webpage for users to monitor traffic in real-time.


## Prerequisites

-Before you begin, ensure you have met the following requirements:

    Python 3.7 or higher.
    NVIDIA GPU (recommended for faster inference and training).
    CUDA and cuDNN (if using GPU).
    Git (for cloning the repository).
    Google Colab Account

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/RealTime-Traffic-Vehicle-Detection.git
   cd RealTime-Traffic-Vehicle-Detection

2. Dependencies:

   ```bash
   pip install -r requirements.txt



Feel free to explore, contribute, and enhance the capabilities of the real-time traffic vehicle detection system!
