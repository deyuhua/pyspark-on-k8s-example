#!/usr/bin/env python

from pyspark import SparkContext, SparkConf
import time

if __name__ == '__main__':
    conf = SparkConf().setAppName("calculate_pyspark_example")
    with SparkContext(conf=conf) as sc:
        time.sleep(10)
