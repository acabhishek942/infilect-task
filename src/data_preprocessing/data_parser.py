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

def csv_reader(path, chunksize=10**4, columns_to_read=None, mark_duplicates=True):
    """
    Returns the mentioned number of rows from csv file.

    param path: Path of the csv file
    param chunksize: number of records to process at a time.
            Default value : 10**4
    param columns_to_read: specify the columns to read.
            Default value: None(signifies all columns to be read)
    param mark_duplicates: mark duplicates in the dataframe
    """
    for chunk in pd.read_csv(path, usecols=columns_to_read, mangle_dupe_cols=mark_duplicates, chunksize=chunksize):
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

duplicate_image_url_dict = {} #needs-attention Need to see how to store this variable
def make_duplicate_image_url_dict(chunk, column_name, chunksize=10**4):
    for index, row in chunk.iterrows():
        if isinstance(row['imageUrlStr'], str):
            if row['imageUrlStr'] in duplicate_image_url_dict:
                duplicate_image_url_dict[row['imageUrlStr']].append(index)
            else:
                duplicate_image_url_dict[row['imageUrlStr']] = [index]
