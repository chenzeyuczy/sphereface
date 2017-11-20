#!/bin/bash
# Usage:
# ./code/sphereface_train.sh GPU
#
# Example:
# ./code/sphereface_train.sh 0,1,2,3

CAFFE_PATH=./tools/caffe-sphereface/build/tools/caffe
SOLVER_PATH=./train/sphereface_solver.prototxt
GPU_ID=0
LOG_PATH=./result/sphereface_train_ms10w.log
#SNAPSHOT=./result/sphereface_model_ms10w_iter_27000.solverstate
#-snapshot ${SNAPSHOT}

${CAFFE_PATH} train -solver ${SOLVER_PATH} -gpu ${GPU_ID} 2>&1 | tee ${LOG_PATH}
