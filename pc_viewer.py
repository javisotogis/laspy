import laspy as lp
import numpy as np


input_path = "C:\Javi\Movidas\laspy\PNOA_1.las"

with lp.open(input_path) as fh:
    print('Points from Header:', fh.header.point_count)
    las = fh.read()
    print(las)
    print('Points from data:', len(las.points))
    ground_pts = las.classification == 2
    bins, counts = np.unique(las.return_number[ground_pts], return_counts=True)
    print('Ground Point Return Number distribution:')
    for r,c in zip(bins,counts):
        print('{}:{}'.format(r, c))

point_cloud = lp.read(input_path)
print(point_cloud)

points = np.vstack((point_cloud.x, point_cloud.y, point_cloud.z)).transpose()
colors = np.vstack((point_cloud.red, point_cloud.green, point_cloud.blue)).transpose()

print(points)
print(colors)