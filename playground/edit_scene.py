def editTxt(x):
    my_file = open("scenes.txt", "w")
    my_file.write("landsat_ot_c2_l1|displayId\n")
    my_file.write(x)

list_a = ['LC08_L1TP_150036_20210819_20210827_02_T1', 'LC08_L1TP_150036_20190713_20200827_02_T1']
editTxt(list_a[0])