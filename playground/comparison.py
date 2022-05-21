from matplotlib.image import imread
from PIL import Image

def comparison(year_one, year_two, region):
    img = imread('path_to_all_files' + 'first_second_region.png')
    img2 = imread('path_to_all_files' + 'first_second_region.png')

    a, b, c = img.shape
    result = np.zeros(first.shape)

    for i in range(a):
        for j in range(b):
            result[i, j, 3] = 1.

            if first[i, j, 0] == second[i, j, 0] and first[i, j, 1] == second[i, j, 1]:
                pass

            elif first[i, j, 0] == second[i, j, 0] and first[i, j, 1] != second[i, j, 1]:
                result[i, j, 0] = second[i, j, 1]

            elif first[i, j, 0] != second[i, j, 0] and first[i, j, 1] == second[i, j, 1]:
                result[i, j, 0] = second[i, j, 0]

            elif first[i, j, 0] != second[i, j, 0] and first[i, j, 1] != second[i, j, 1]:
                result[i, j, 0] = second[i, j, 0]
                result[i, j, 1] = second[i, j, 1]
                
    
    res_img = Image.fromarray((result * 255).astype(np.uint8))
    res_img.save('path_to_results_folder' + "first_second_region_comparison.png")