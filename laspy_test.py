import laspy as lp
import numpy as np

## open file
input_path = "C:\Javi\Movidas\laspy\PNOA_1.las"
point_cloud = lp.read(input_path)  # read file
pointsZ = np.vstack((point_cloud.z)).transpose()  # convert Z values into np array
print('\nAltitud maxima:', np.max(pointsZ))  # print some metrics
print('\nAlitud media:', np.mean(pointsZ))
print('\nAltitud minima:', np.min(pointsZ))

histo = (np.histogram(pointsZ, bins=[4, 200, 400, 600, 800, 963]))  ## find out Z distribution

print('\nHistograma: ', histo)

with lp.open(input_path) as fh:
    #print('Numero de puntos en la cabecera:', fh.header.point_count)
    las = fh.read()
    print('Points from data:', len(las.points))  ## read number of points from file




with lp.open(input_path) as fh:
    las = fh.read()
    ground_pts = las.classification == 2
    bins, counts = np.unique(las.return_number[ground_pts], return_counts=True)
    #print('Ground Point Return Number distribution:')
    for r,c in zip(bins,counts):
        print('{}:{}'.format(r, c))  ## find out ground point distribution


#print(point_cloud)

#points = np.vstack((point_cloud.x, point_cloud.y, point_cloud.z)).transpose()
colors = np.vstack((point_cloud.red, point_cloud.green, point_cloud.blue)).transpose()
print(colors)  ## create numpy array with RGB

