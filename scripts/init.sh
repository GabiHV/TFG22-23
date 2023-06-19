#!/bin/bash

pip install pandas==1.5.3
source /etc/bash.bashrc && jupyter notebook --notebook-dir=/tf --ip 0.0.0.0 --no-browser --allow-root