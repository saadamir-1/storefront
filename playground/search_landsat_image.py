import json
from landsatxplore.api import API
from bounding_box import findBBox

def searchImage(boundingBox, sYear, eYear):
# Initialize a new API instance and get an access key
    api = API('ziayanj', 'fyp.forest.123')

# Search for Landsat TM sceneslandsat_8_c1
    scenes = api.search(
        dataset='landsat_ot_c2_l1',
        bbox=(boundingBox[0], boundingBox[1],boundingBox[2],boundingBox[3]),#73.0618, 34.0640, 73.4024, 34.2549),
        start_date=sYear +'-06-01',
        end_date=eYear +'-08-30',
        max_cloud_cover=20
        #latitude=50.85,
        #longitude=-4.35,
    )   

    if sYear == eYear:
        list_arr = [scenes[0]['display_id']]
    else:
        list_arr = [scenes[0]['display_id'], scenes[len(scenes)-1]['display_id']]

    print(list_arr)

    api.logout()

    return list_arr

    # print(f"{len(scenes)} scenes found.")
    # Process the result
    # for scene in scenes:
    #     print(scene['acquisition_date'].strftime('%Y-%m-%d'))
    #     print(scene['entity_id'])
    #     print(scene['display_id'])
    #     print()

    # Write scene footprints to disk
        # fname = f"{scene['landsat_product_id']}.geojson"
        # with open(fname, "w") as f:
        #     json.dump(scene['spatial_coverage'].__geo_interface__, f)

    

bbox1 = findBBox(73.1003, 34.2549, 73.3859, 34.2504, 73.4024, 34.0640, 73.0618, 34.0709)
startYear = '2019'
endYear = '2021'
searchImage(bbox1, startYear, endYear)


# from landsatxplore.earthexplorer import EarthExplorer

# ee = EarthExplorer('ziayanj', 'fyp.forest.123')

# ee.download('LT52040241995266FUI02', output_dir='./data')

# ee.logout()


# from usgs import api

# # Set the EarthExplorer catalog
# node = 'EE'

# # Set the Hyperion and Landsat 8 dataset
# landsat8_dataset = 'LANDSAT_8'

# # Set the scene ids
# landsat8_scene_id = 'LT52040241995266FUI02'

# # Submit requests to USGS servers
# api.metadata(landsat8_dataset, node, [landsat8_scene_id])
