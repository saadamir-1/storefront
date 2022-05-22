from numpy import imag
import rasterio
import os
from django.conf import settings

# from storefront.settings import BASE_DIR

def stack(nameLandsat, data_path, image_name):
    
    bands_list = ['1','2','3','4','5','6','7','8','9','10','11']
    file_list = []
    y = nameLandsat + '_B'

    for x in bands_list:
        z = y + x + '.TIF'
        file_list.append(z)
    

    # file_list = ['LC08_L1TP_150036_20180608_20200831_02_T1_B1.TIF', 
    #              'LC08_L1TP_150036_20180608_20200831_02_T1_B2.TIF', 
    #              'LC08_L1TP_150036_20180608_20200831_02_T1_B3.TIF', 
    #              'LC08_L1TP_150036_20180608_20200831_02_T1_B4.TIF', 
    #              'LC08_L1TP_150036_20180608_20200831_02_T1_B5.TIF', 
    #              'LC08_L1TP_150036_20180608_20200831_02_T1_B6.TIF', 
    #              'LC08_L1TP_150036_20180608_20200831_02_T1_B7.TIF', 
    #              'LC08_L1TP_150036_20180608_20200831_02_T1_B8.TIF', 
    #              'LC08_L1TP_150036_20180608_20200831_02_T1_B9.TIF', 
    #              'LC08_L1TP_150036_20180608_20200831_02_T1_B10.TIF', 
    #              'LC08_L1TP_150036_20180608_20200831_02_T1_B11.TIF']

    # Read metadata of first file
    
    # file_name = '/playground/downloaded_image/' + file_list[0]
    # print(settings.BASE_DIR)
    # with rasterio.open(os.path.join(settings.BASE_DIR, file_name)) as src0:
    file_path = data_path + file_list[0]
    with rasterio.open(file_path) as src0:
        meta = src0.meta
    # Update meta to reflect the number of layers
    meta.update(count = len(file_list))

    # # Read each layer and write it to stack
    print(data_path)
    print('\n' + image_name)
    with rasterio.open(image_name, 'w', **meta) as dst:
        for id, layer in enumerate(file_list, start=1):
            # with rasterio.open(os.path.join(settings.BASE_DIR, layer)) as src1:
            with rasterio.open(file_path + layer) as src1:
                dst.write_band(id, src1.read(1))

# name = 'LC08_L1TP_150036_20180608_20200831_02_T1'
# region = 'multan'
# year = 2014
# stack(name, year, region)
