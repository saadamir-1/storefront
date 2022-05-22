import shapefile

def shapeFileDownload(coord1a, coord1b, coord2a, coord2b, coord3a, coord3b, coord4a, coord4b, region):

    with shapefile.Writer("./shapefiles/" + region + "_shapefile") as w:
        w.field('field1', 'C')
        w.poly([[
            [coord1a, coord1b], [coord2a, coord2b], [coord3a, coord3b],  # colorado
            [coord4a, coord4b]]])
            # w.poly([[ [lon, lat] 
            # coada are all longitudes while cordb are all latitudes
            # [73.1003, 34.2549], [73.3859, 34.2504], [73.4024, 34.0640],  # colorado
            # [73.0618, 34.0709]]])
        w.record('polygon1')

    with open("./shapefiles/" + region + "_shapefile.prj", "w") as projection:
        epsg = 'GEOGCS["WGS 84",'
        epsg += 'DATUM["WGS_1984",'
        epsg += 'SPHEROID["WGS 84",6378137,298.257223563]]'
        epsg += ',PRIMEM["Greenwich",0],'
        epsg += 'UNIT["degree",0.0174532925199433]]'
        print(epsg, file=projection)

    # dividedRects = [(7598325.0, 731579.0, 7698325.0, 631579.0), (7598325.0, 631579.0, 7698325.0, 611641.0), (7698325.0, 731579.0, 7728636.0, 631579.0), (7698325.0, 631579.0, 7728636.0, 611641.0)]
    # anus = [7598325.0, 731579.0, 7698325.0, 631579.0]
    # anus = [[5.588144,51.993435], [5.727906, 51.993435], [5.727906, 51.944356], [5.588144, 51.944356]]

  # w.point(one[0], one[1])
  # w.record('point1')

  # w.point(one[2], one[1])
  # w.record('point2')

  # w.point(one[2], one[3])
  # w.record('point3')

  # w.point(one[0], one[3])
  # w.record('point4')

  

  # w.point(anus[0][0], anus[0][1])
  # w.record('point1')
  
  # w.point(anus[1][0], anus[1][1])
  # w.record('point2')

  # w.point(anus[2][0], anus[2][1])
  # w.record('point3')

  # w.point(anus[3][0], anus[3][1])
  # w.record('point4')





  # w.poly([[
  #       [-109.05, 37.0], [-102.05, 37.0], [-102.05, 41.0],  # colorado
  #       [-109.05, 41.0], [-111.05, 41.0], [-111.05, 42.0],  # utah
  #       [-114.05, 42.0], [-114.05, 37.0], [-109.05, 37.0]]])

        


  # for i in range(0, len(dividedRects)):
  #   print(i)
  #   topLeft = [dividedRects[i][0],dividedRects[i][1]]
  #   topRight = [dividedRects[i][2], dividedRects[i][1]]
  #   bottomRight = [dividedRects[i][2], dividedRects[i][3]]
  #   bottomLeft = [dividedRects[i][0], dividedRects[i][3]]

  #   w.point(dividedRects[i][0], dividedRects[i][1])
  #   w.record('point1')

  #   w.point(dividedRects[i][2], dividedRects[i][1])
  #   w.record('point2')

  #   w.point(dividedRects[i][2], dividedRects[i][3])
  #   w.record('point3')

  #   w.point(dividedRects[i][0], dividedRects[i][3])
  #   w.record('point4')

  # for i in range(0, len(dividedRects)):

  #   w.field("ID", "C", "40")
  #   w.field("Events", "C", "40")
  #   topLeft = [dividedRects[i][0],dividedRects[i][1]]
  #   topRight = [dividedRects[i][2], dividedRects[i][1]]
  #   bottomRight = [dividedRects[i][2], dividedRects[i][3]]
  #   bottomLeft = [dividedRects[i][0], dividedRects[i][3]]
  #   w.poly([[topLeft,topRight,bottomRight,bottomLeft]])
  #   w.record(str(i), str(0))

# create the PRJ file
    

# shapeFileDownload(73.1003, 34.2549, 73.3859, 34.2504, 73.4024, 34.0640, 73.0618, 34.0709, "multan")

