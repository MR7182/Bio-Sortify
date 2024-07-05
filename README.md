# Bio Sortify: AI for greener tomorrow

## Overview
Bio Sortify is a machine learning model trained to classify waste as either biodegradable or non-biodegradable. The model boasts an impressive accuracy of **98.8%**. This project was developed for Philly Codefest 2024, where the theme was "AI for Common Good". 

## Web Interface
A user-friendly website was built using **HTML**, **CSS**, and **JavaScript**to interact with the model. The website supports both image classification and real-time classification. We used **FastAPI** to connect the model to the website, ensuring a seamless and efficient interaction between the user interface and the machine learning model.

## Model Training
The model was trained on a dataset of **250,000 images** sourced from Kaggle. We used **AWS Sagemaker** for training, leveraging transfer learning on **ImageNet V2**, where we got a test accuracy of **98.8%**. Initially, we attempted to train the model using a Convolutional Neural Network (CNN), but the training process was lengthy and the accuracy was only 86.54%. Therefore, we decided to use AWS Sagemaker, which also happened to be a sponsor for Philly Codefest.

## Team
Bio Sortify was brought to life by a team of six hardworking and enthusiastic individuals:
- Meghna Rajbhandari
- Saksham Rajbhandari
- Krithi Hari
- Evan Toomey
- Vruj Patel
- Uditi Shah

## Model Prediction Screenshot
Since the model is not currently hosted and we are using FastAPI, below is a screenshot demonstrating the model's prediction:

<a href="https://ibb.co/5jqNW08"><img src="https://i.ibb.co/t2y7MGs/Screenshot-2024-07-04-195925.png" alt="Screenshot-2024-07-04-195925" border="0"></a>

## Real Time Prediction Video

[![Watch the video](https://github.com/MR7182/Bio-Sortify/blob/main/thumbnail.png)](https://github.com/MR7182/Bio-Sortify/blob/main/video.mp4)


## Acknowledgements
We would like to express our gratitude to Philly Codefest 2024 for providing us with the opportunity to work on this project. We would also like to thank AWS Sagemaker for their support.

## Future Work
Our team is committed to continuous improvement and innovation. We are currently exploring the use of YOLOv8 for faster prediction results. By leveraging the speed and efficiency of YOLOv8, we aim to enhance the real-time classification capabilities of Bio Sortify, making it even more responsive and user-friendly.

In addition, we are also working on expanding the categories of waste that our model can identify. This will allow us to provide more detailed and accurate information to our users, further promoting responsible waste management practices.

Lastly, we are planning to host our model, which will allow us to reach a wider audience and make a greater impact towards a greener tomorrow.
