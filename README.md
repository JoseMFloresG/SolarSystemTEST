#Recognition Video UUV SIM Documentation

<p align="center">
  <img src=https://github.com/vanttec/vanttec_uuv/blob/master/docs/LogoNegro_Azul.png width="400" height="240" align="center"/>
</p>

## Clone the UUV Sim repository ###

- Go into this link and follow the instructions: [UUV_sim Repository](https://github.com/vanttec/vanttec_uuv/tree/retos)

## Install repositories ###
**Dont do catkin_make or catkin build before install all the repositories**
```
cd /ws/src
```
- ZED ROS WRAPPER: This repository is to use the ZED Camera [Repository Link](https://github.com/stereolabs/zed-ros-wrapper)
```
catkin build j4
```

## How to use it ###

- To use the camera see the documentation of the zed-ros-wrapper repository
- Use rostopic to see the topic of the camera and change it on "darknet_ros/config/ros.yaml"
- To launch the YOLO node:
```
roslaunch darknet_ros darknet_ros.launch
```
