from csv_parser import data_parser

original_path = '/Users/ac/Documents/2oq-c1r.csv'
reduced_to_original_image_path = '../reduced_data/reduced_to_original_image_url.csv'

# Code snippet to reduce the size of dataset by shortening imageURLString
# Reduced from around 6GB to 4.4GB 
for smallchunk in data_parser.csv_reader('/Users/ac/Documents/2oq-c1r.csv', chunksize=10**4):
    smallchunk['imageUrlStr'] = data_parser.shorten_imageURLString(smallchunk)
    data_parser.csv_writer_append(reduced_to_original_image_path, smallchunk)
