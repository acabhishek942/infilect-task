from data_preprocessing import data_parser

import json

original_path = '/Users/ac/Documents/2oq-c1r.csv'
reduced_to_original_image_path = '../reduced_data/reduced_to_original_image_url.csv'
duplicate_image_url_json_path = '../reduced_data/duplicate_image_url.json'

# Code snippet to reduce the size of dataset by shortening imageURLString
# Reduced from around 6GB to 4.4GB
# for smallchunk in data_parser.csv_reader(original_path, chunksize=10**4):
#     smallchunk['imageUrlStr'] = data_parser.shorten_imageURLString(smallchunk)
#     data_parser.csv_writer_append(reduced_to_original_image_path, smallchunk)

# marking products having same imageURLString as copies of one another
"""
Generate a dictionary like {imageURLString: [list of all repeating indexes]}
"""
# duplicate_image_url_dict = {}
# for smallchunk in data_parser.csv_reader(reduced_to_original_image_path, columns_to_read=['imageUrlStr'], chunksize=10**4):
#     for index, row in smallchunk.iterrows():
#         if isinstance(row['imageUrlStr'], str):
#             if row['imageUrlStr'] in duplicate_image_url_dict:
#                 duplicate_image_url_dict[row['imageUrlStr']].append(index)
#             else:
#                 duplicate_image_url_dict[row['imageUrlStr']] = [index]
#
# with open(duplicate_image_url_json_path, 'w') as fp:
#     json.dump(duplicate_image_url_dict, fp)
