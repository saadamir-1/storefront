import base64
from fileinput import filename
import osmnx as ox
from django.shortcuts import render
from django.http import HttpResponse
from . import inference_btt_2020
from PIL import Image

# Create your views here.
# request -> response
# request handler
# action ( views is alse called action in some frameworks)
class Arguments:
    def __init__(self):
        self.data_path = '/home/saad/Project/Test_Data/'
        self.rasterized_shapefiles_path = '/home/saad/Project/District_Shapefiles' 
        self.model_topology = 'ENC_4_DEC_4' 
        self.bands = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18] 
        self.classes = ['Non-Forest', 'Forest'] 
        self.model_path = '/home/saad/Project/Data/save_dir/model_99.pt' 
        self.dest = '/home/saad/Project/Inference'
        self.bs = 4 
        self.cuda = 1
        self.device = 0



def inference(request, startYear, endYear, region):
    args_better = Arguments()
    if startYear == endYear:
        year_our = [startYear]
    else:
        year_our = [startYear, endYear]
    place = ox.graph_from_bbox(25.65,25.55,85.26,85.01, network_type = 'drive')
    place_projected = ox.project_graph(place)
    # ox.plot_graph(place_projected)
    ox.save_graph_shapefile(place_projected, filepath = 'playground/shapefiles')
    region_our = [region]
    inference_btt_2020.run_inference(args_better, year_our, region_our)
    imagePath = '/home/saad/Project/Inference/abbottabad_2014_inferred_map.png'
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
