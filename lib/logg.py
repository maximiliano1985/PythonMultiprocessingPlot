#!/usr/bin/env python
from multiprocessing import Process
import sys
import logger


args_logger = {'sampling_time_ms': 5, 'plotting_time_ms': 100}
logger.Logger(args_logger)
    
    