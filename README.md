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



<iframe width="560" height="315" src="https://www.youtube.com/embed/s5CwtBsv_bo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

# [Mobile Web Application](https://gargabe-classifier-jxq632gueq-uc.a.run.app/)
