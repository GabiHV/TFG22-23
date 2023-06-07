#!/bin/bash

#Instalar contenedor de Docker
sudo docker run --gpus all -it --rm -v ./:/tf -p 8888:8888 tensorflow/tensorflow:latest-gpu-jupyter