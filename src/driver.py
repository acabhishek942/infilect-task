from data_preprocessing import data_parser

import json

original_path = '/Users/ac/Documents/2oq-c1r.csv'
reduced_to_original_image_path = '../reduced_data/reduced_to_original_image_url.csv'
duplicate_image_url_json_path = '../reduced_data/duplicate_image_url.json'
reduced_image_url_json_path = '../reduced_data/reduced_duplicate_image_url.json'
reduced_drop_duplicate_rows_path = '../reduced_data/reduced_drop_duplicate_rows.csv'

"""
Code snippet to reduce the size of dataset by shortening imageURLString
Reduced from around 6GB to 4.4GB
"""
# for smallchunk in data_parser.csv_reader(original_path, chunksize=10**4):
#     smallchunk['imageUrlStr'] = data_parser.shorten_imageURLString(smallchunk)
#     data_parser.csv_writer_append(reduced_to_original_image_path, smallchunk)

# marking products having same imageURLString as copies of one another
"""
Generate a dictionary like {imageURLString: [list of all repeating indexes]}
"""
duplicate_image_url_dict = {}
for smallchunk in data_parser.csv_reader(reduced_drop_duplicate_rows_path, columns_to_read=['imageUrlStr'], chunksize=10**4):
    for index, row in smallchunk.iterrows():
        if isinstance(row['imageUrlStr'], str):
            if row['imageUrlStr'] in duplicate_image_url_dict:
                duplicate_image_url_dict[row['imageUrlStr']].append(index)
            else:
                duplicate_image_url_dict[row['imageUrlStr']] = [index]
for key in duplicate_image_url_dict:
    print duplicate_image_url_dict[key]
#
# with open(duplicate_image_url_json_path, 'w') as fp:
#     json.dump(duplicate_image_url_dict, fp)

"""
Remove all entries from duplicate_image_url_json_path that does not repeat
"""
# with open(duplicate_image_url_json_path) as fp:
#     duplicate_image_url_dict = json.load(fp)
#
# imageUrlStr_to_delete = []
# for image_url_string in duplicate_image_url_dict:
#     if len(duplicate_image_url_dict[image_url_string]) == 1:
#         imageUrlStr_to_delete.append(image_url_string)
#
# for image_url in imageUrlStr_to_delete:
#     del duplicate_image_url_dict[image_url]
#
# with open(reduced_image_url_json_path, 'w') as fp:
#     json.dump(duplicate_image_url_dict, fp)

"""
Drop rows from dataset that have same image url and write to new csv file.
Took about 10 mins to execute and reduced dataset size to 1.3GB
"""
# with open(reduced_image_url_json_path) as fp:
#     reduced_image_url_dict = json.load(fp)
#
# loop_counter = 0
# for smallchunk in data_parser.csv_reader(reduced_to_original_image_path, chunksize=10**4):
#     smallchunk_backup = smallchunk
#     indexes_to_drop = []
#     for index, row in smallchunk.iterrows():
#         if row['imageUrlStr'] in reduced_image_url_dict:
#             indexes_to_drop_temp = reduced_image_url_dict[row['imageUrlStr']][1:]
#             for potential_drop_index in indexes_to_drop_temp:
#                 if potential_drop_index in range(loop_counter*(10**4), 9999 + loop_counter*(10**4)):
#                     indexes_to_drop.append(potential_drop_index - (loop_counter*(10**4)))
#     smallchunk_backup.drop(smallchunk_backup.index[list(set(indexes_to_drop))], inplace=True)
#     data_parser.csv_writer_append(reduced_drop_duplicate_rows_path, smallchunk_backup)
#     loop_counter += 1
