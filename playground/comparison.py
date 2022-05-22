from matplotlib.image import imread
from PIL import Image
import numpy as np

def comparison(year_one, year_two, region):
    first = imread('/mnt/efs/fs1/proj/storefront/playground/inference_results/' + region + '_' + year_one +'_inferred_map.png')
    second = imread('/mnt/efs/fs1/proj/storefront/playground/inference_results/' + region + '_' + year_two +'_inferred_map.png')

    a, b, c = first.shape
    result = np.zeros(first.shape)

    for i in range(a):
        for j in range(b):
            result[i, j, 3] = 1.

            if first[i, j, 1] == second[i, j, 1]:
                if first[i, j, 0] == second[i, j, 0]:
                    result[i, j, 1] = second[i, j, 1]
                else:
                    result[i, j, 0] = second[i, j, 0]

            else:
                if second[i, j, 1] == 0:
                    result[i, j, 0] = 1
                else:
                    result[i, j, 0] = 1
                    result[i, j, 1] = 1
                
    
    res_img = Image.fromarray((result * 255).astype(np.uint8))
    res_img.save('/mnt/efs/fs1/proj/storefront/playground/inference_results/' + year_one + '_' + year_two + '_' + region + '_comparison.png')
