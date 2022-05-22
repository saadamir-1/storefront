def editTxt(x):
    my_file = open("scenes.txt", "w")
    my_file.write("landsat_ot_c2_l1|displayId\n")
    my_file.write(x)


# list_a = ['LC08_L1TP_150036_20210819_20210827_02_T1']#, 'LC08_L1TP_150036_20190713_20200827_02_T1']

# #shapeFileDownload(73.1003, 34.2549, 73.3859, 34.2504, 73.4024, 34.0640, 73.0618, 34.0709, "ApnaRegion")
# # bbox1 = findBBox(73.1003, 34.2549, 73.3859, 34.2504, 73.4024, 34.0640, 73.0618, 34.0709)
# # startYear = '2019'
# # endYear = '2021'
# # searchImage(bbox1, startYear, endYear)
# for x in list_a:
#     print("editing scenes file for" + x +"\n\n")
#     editTxt(x)
    #run_m2m(args_better_download)
    #if loop running for first time then use start year in function argument
        #stack(name, startyear, region)
    #else loop running for second time then use end year
        #stack(name, endyear, region)
# shpToRaster(year, region)
#run_inference()
#comparison()
#display()
