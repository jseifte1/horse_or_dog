#!/bin/bash
nvcc nn.cu -L /usr/local/cuda/lib -lcudart -lcudnn -o nn
./nn dog 1
./nn dog 2
./nn horse 1
./nn horse 2
