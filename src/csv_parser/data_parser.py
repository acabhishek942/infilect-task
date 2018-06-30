#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on June 30, 2018
@author: acabhishek942
This script has methods to read data from a csv file to pandas dataframe in
in small chunks of size 10
"""
import pandas as pd
import numpy as np

import os

def onlyOriginalImageURL(imageURLString):
    """
    Return only original image url
    """
    if isinstance(imageURLString, str):
        return imageURLString.split(';')[0]
    return ""

# for training_data in  pd.read_csv(path, chunksize=10):
#     print(training_data.index)
#     break;

def csv_reader(path, chunksize=10**4):
    """
    Returns the mentioned number of rows from csv file.

    param path: Path of the csv file
    param chunksize: number of records to process at a time.
            Default value : 10**4
    """
    for chunk in pd.read_csv(path, chunksize=chunksize):
        yield chunk

def shorten_imageURLString(chunk):
    """
    param chunk: pandas dataframe
    """
    return chunk['imageUrlStr'].apply(onlyOriginalImageURL)


def csv_writer_append(path, chunk):
    """
    param path: Path of the csv file
    param chunk: pandas dataframe
    """
    if not os.path.isfile(path):
        chunk.to_csv(path, index=False)
    else:
        chunk.to_csv(path, mode='a', index=False, header=False)
