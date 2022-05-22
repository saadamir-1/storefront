from osgeo import gdal
import os
from playground.convert import shpToRaster
from playground.inference_btt_2020 import run_inference

from playground.stack import stack

def clip_landsat(nameLandsat, region):

    inputPath = '/mnt/efs/fs1/proj/storefront/'
    outputPath = '/mnt/efs/fs1/proj/storefront/clipped/'
    shp_clip = '/mnt/efs/fs1/proj/storefront/shapefiles/' + region + '_shapefile.shp'

    bands_list_numbers = ['1','2','3','4','5','6','7','8','9','10','11']
    bandList = []
    y = nameLandsat + '_B'

    for x in bands_list_numbers:
        z = y + x + '.TIF'
        bandList.append(z)

    for x in bandList:
        print(x)

    for band in bandList:
        options = gdal.WarpOptions(cutlineDSName=shp_clip,cropToCutline=True)
        outBand = gdal.Warp(srcDSOrSrcDSTab=inputPath + band,
                            destNameOrDestDS=outputPath + band,
                            options=options)
        outBand= None


# class Arguments:
#     def __init__(self):
#         self.data_path = '/home/saad/Desktop/extra/django_projects/'
#         self.rasterized_shapefiles_path = '/home/saad/Downloads/clipping/' 
#         self.model_topology = 'ENC_4_DEC_4' 
#         self.bands = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18] 
#         self.classes = ['Non-Forest', 'Forest'] 
#         self.model_path = '/home/saad/Project/Data/save_dir/model_99.pt' 
#         self.dest = '/home/saad/Downloads/clipping/'
#         self.bs = 4 
#         self.cuda = 0
#         self.device = 0

# name = 'LC08_L1TP_150036_20180608_20200831_02_T1'
# region = 'abbottabad'
# year = 2018
# args = Arguments()
# clipp_landsat(name, region)
# stack(name, year, region)
# shpToRaster(year, region)
# year_our = [year]
# region_our = [region]
# run_inference(args, year_our, region_our)