import base64
from fileinput import filename
import osmnx as ox
from django.shortcuts import render
from django.http import HttpResponse
from playground import comparison
from playground.bounding_box import findBBox
from playground.convert import shpToRaster
from playground.edit_scene import editTxt
from playground.m2m import run_m2m
from playground.pysh import shapeFileDownload
from playground.search_landsat_image import searchImage
from playground.stack import stack
from . import inference_btt_2020
from PIL import Image
from playground.clip import clip_landsat
from playground.comparison import comparisons
# Create your views here.
# request -> response
# request handler
# action ( views is alse called action in some frameworks)
class Arguments:
    def __init__(self):
        self.data_path = '/mnt/efs/fs1/proj/storefront/'
        self.rasterized_shapefiles_path = '/mnt/efs/fs1/proj/storefront/shapefiles/' 
        self.model_topology = 'ENC_4_DEC_4' 
        self.bands = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18] 
        self.classes = ['Non-Forest', 'Forest'] 
        self.model_path = '/mnt/efs/fs1/test_data/model_99.pt' 
        self.dest = '/mnt/efs/fs1/proj/storefront/playground/inference_results/'
        self.bs = 4 
        self.cuda = 0
        self.device = 0

class Arguments_m2m:
    def __init__(self):
        self.user = 'ziayanj'
        self.passw = 'fyp.forest.123' 
        self.file = 'none'

def run_project(request, startYear, endYear, region):

    args = Arguments()
    args_downloading = Arguments_m2m() 

    if startYear == endYear:
        year_our = [startYear]
    else:
        year_our = [startYear, endYear]
    
    print("\n**************************************\n")
    print("-----------> Activity Log <-----------")
    print("\n**************************************\n")
    print("\n==> Downloading ShapeFiles")

    shapeFileDownload(73.1003, 34.2549, 73.3859, 34.2504, 73.4024, 34.0640, 73.0618, 34.0709, region)

    print("\n==> Downloading Complete")
    print("\n==> Creating bounding box")

    bbox1 = findBBox(73.1003, 34.2549, 73.3859, 34.2504, 73.4024, 34.0640, 73.0618, 34.0709)

    print("\n==> Bounding box created")
    print("\n==> Searching for Landsat8 Images")

    image_names = searchImage(bbox1, year_our)

    print("\n==> Search completed for Landsat8 Images\n")
    count = 0
    print(image_names) 
    for x in image_names:
       print("==> Editing scenes file for" + x +"\n")
       editTxt(x)
       run_m2m(args_downloading)
       if count == 0:
           stack(x, startYear, region)
           count+=count
       elif count == 1:
           stack(x, endYear, region)
    
    print("\n==> Converting Shapefile")
    shpToRaster(startYear, region)

    #Inference
    print("\n==> RUNNING INFERENCE")

    region_our = [region]
    inference_btt_2020.run_inference(args, year_our, region_our)
    print("\n==> INFERENCE COMLETE")

    if startYear != endYear:
        print("\n==> RUNNING COMPARISON")

        comparison(startYear, endYear, region)
        imagePath = '/mnt/efs/fs1/proj/storefront/playground/inference_results/' + startYear + '_' + endYear+'_' + region + '_comparison.png'
        try:
            with open(imagePath, "rb") as f:
                encoded_string = base64.b64encode(f.read())
                print(encoded_string)
                return HttpResponse(encoded_string, content_type="image/png")

        except IOError:
            red = Image.new('RGBA', (50, 50), (255,0,0,0))
            response = HttpResponse(content_type="image/png")
            red.save(response, "png")
            return response
    else:
        imagePath = '/mnt/efs/fs1/proj/storefront/playground/inference_results/' + region + '_' + startYear +'_inferred_map.png'
        try:
            with open(imagePath, "rb") as f:
                encoded_string = base64.b64encode(f.read())
                print(encoded_string)
                return HttpResponse(encoded_string, content_type="image/png")

        except IOError:
            red = Image.new('RGBA', (50, 50), (255,0,0,0))
            response = HttpResponse(content_type="image/png")
            red.save(response, "png")
            return response
# startYear = 2018
# endYear = 2019
# region = 'abbottabad'
# run_project(startYear, endYear, region)


def run_project_map(request, startYear, endYear, region, a1, a2, b1, b2, c1, c2, d1, d2):

    args = Arguments()
    args_downloading = Arguments_m2m() 

    if startYear == endYear:
        year_our = [startYear]
    else:
        year_our = [startYear, endYear]
    
    # print("\n**************************************\n")
    # print("-----------> Activity Log <-----------")
    # print("\n**************************************\n")
    # print("\n==> Downloading ShapeFiles")

    # shapeFileDownload(a1, a2, b1, b2, c1, c2, d1, d2, region) # /mnt/efs/fs1/proj/storefront/shapefiles

    # print("\n==> Downloading Complete")
    # print("\n==> Creating bounding box")

    # bbox1 = findBBox(a1, a2, b1, b2, c1, c2, d1, d2)

    # print("\n==> Bounding box created")
    # print("\n==> Searching for Landsat8 Images")

    # image_names = searchImage(bbox1, year_our)

    # print("\n==> Search completed for Landsat8 Images\n")
    # count = 0
    # print(image_names) 
    # for x in image_names:
    #    print("==> Editing scenes file for" + x +"\n")
    #    editTxt(x)
    #    run_m2m(args_downloading) #/mnt/efs/fs1/proj/storefront/shapefiles
    #    if count == 0:
    #        data_path = "/mnt/efs/fs1/proj/storefront/downloaded_image/"
    #        image_name = 'landsat8_' + str(startYear) + '_region_' + region + '.tif'
    #        print("\n==> Starting Stack original file")
    #        stack(x, data_path, image_name)
    #        print("\n==> Stack completed")
    #        print("\n==> clipping landsat")
    #        clip_landsat(x, region)
    #        print("\n==> clipping landsat complete")
    #        data_path = '/mnt/efs/fs1/proj/storefront/clipped/'
    #        image_name = 'clipped_landsat8_' + str(startYear) + '_region_' + region + '.tif'
    #        print("\n==> stacking clipped landsat")
    #        stack(x, data_path, image_name)
    #        print("\n==> clipped landsat stacked")
    #        count=1
    #    elif count == 1:
    #        data_path = "/mnt/efs/fs1/proj/storefront/downloaded_image/"
    #        image_name = 'landsat8_' + str(endYear) + '_region_' + region + '.tif'
    #        print("\n==> Starting Stack original file")
    #        stack(x, data_path, image_name)
    #        print("\n==> Stack completed")
    #        print("\n==> clipping landsat")
    #        clip_landsat(x, region)
    #        print("\n==> clipping landsat complete")
    #        data_path = '/mnt/efs/fs1/proj/storefront/clipped/'
    #        image_name = 'clipped_landsat8_' + str(endYear) + '_region_' + region + '.tif'
    #        print("\n==> stacking clipped landsat")
    #        stack(x, data_path, image_name)
    #        print("\n==> clipped landsat stacked")
    
    # print("\n==> Converting Shapefile")
    # shpToRaster(startYear, region)

    # #Inference
    # print("\n==> RUNNING INFERENCE")

    # region_our = [region]
    # inference_btt_2020.run_inference(args, year_our, region_our)
    # print("\n==> INFERENCE COMLETE")

    if startYear != endYear:
        print("\n==> RUNNING COMPARISON")

        comparisons(startYear, endYear, region)
        imagePath = '/mnt/efs/fs1/proj/storefront/playground/inference_results/' + startYear + '_' + endYear+'_' + region + '_comparison.png'
        try:
            with open(imagePath, "rb") as f:
                encoded_string = base64.b64encode(f.read())
                print(encoded_string)
                return HttpResponse(encoded_string, content_type="image/png")

        except IOError:
            red = Image.new('RGBA', (50, 50), (255,0,0,0))
            response = HttpResponse(content_type="image/png")
            red.save(response, "png")
            return response
    else:
        imagePath = '/mnt/efs/fs1/proj/storefront/playground/inference_results/' + region + '_' + startYear +'_inferred_map.png'
        try:
            with open(imagePath, "rb") as f:
                encoded_string = base64.b64encode(f.read())
                print(encoded_string)
                return HttpResponse(encoded_string, content_type="image/png")

        except IOError:
            red = Image.new('RGBA', (50, 50), (255,0,0,0))
            response = HttpResponse(content_type="image/png")
            red.save(response, "png")
            return response
