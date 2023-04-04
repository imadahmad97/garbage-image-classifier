# Garbage Bin Sorter - Overview
Garbage bin sorter is a image classification model for images of waste. It sorts the images into one of:

 1. Trash
 2. Compost
 3. Recycling

We have implemented this model in a variety of ways, including a web application and even a trash sorting robot! 

# Table of Contents
- [Model](#model)
- [Trash Sorting Robot (TSR)](#trash-sorting-robot-tsr)
- [Mobile Web Application](#mobile-web-application)


# Model
The image classification model is a convolutional neural network built with Keras. It consists of an input layer, 9 convolutional 2D layers, 4 Max Pooling 2D layers, 1 flatten layer, and 3 Dense layers. The model was trained on data from [Kaggle](https://www.kaggle.com/datasets/mostafaabla/garbage-classification?select=garbage_classification). 

# [Trash Sorting Robot (TSR)](https://www.youtube.com/watch?v=s5CwtBsv_bo)
Upon building the model, I decided to put it into application in the form of a Trash Sorting Robot (TSR). A video of the robot in action can be seen [here](https://www.youtube.com/watch?v=s5CwtBsv_bo).

The robot was built on a Raspberry Pi 3 single board computer. I controlled the trash lids with servo motors, two of which were powered by their own 9V batteries, and one that was powered by the Raspberry Pi itself. The Raspberry Pi was also connected to a camera module to scan the trash. Below is a schematic diagram of the robot:

<a href="https://ibb.co/60QK9bj"><img src="https://i.ibb.co/nMpXdfx/Raspberry-Pi-Diagram-2.png" alt="Raspberry-Pi-Diagram-2" border="0"></a>

Taking a look at the robot from the front view, we can see the (tiny) camera module connected to the Pi. Note that in future iterations, a stronger camera with it's own power supply will produce better results:

<a href="https://ibb.co/jGMP7Pz"><img src="https://i.ibb.co/mtqVQV0/IMG-0672.jpg" alt="IMG-0672" border="0"></a>

Looking the the back of the trash bins, we can see the servo motor taped to the back. This motor is connected to a circular disk that has a string tied to it. This string is taped to the lid at the top, so that when the motor spins the lid is pulled:

<a href="https://ibb.co/fd7bzSG"><img src="https://i.ibb.co/YBG6FWT/Picture1.png" alt="Picture1" border="0"></a>

Finally, I decided to show a top-down view. This shows all the wiring and connections. You can see the two batteries as well, next to the Pi:

<a href="https://ibb.co/FHg27w6"><img src="https://i.ibb.co/fD4f0pM/Screenshot-2023-03-31-at-4-35-50-AM.png" alt="Screenshot-2023-03-31-at-4-35-50-AM" border="0"></a>

# [Mobile Web Application](https://gargabe-classifier-jxq632gueq-uc.a.run.app/)
The application was built on a Dash framework. Then, we built a Docker container with all the app dependencies. Finally, the docker was deployed to Google Cloud Run. 
