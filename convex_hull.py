###convex hull algorithm for a set of 2D points
from scipy.spatial import ConvexHull
import numpy as np
import matplotlib.pyplot as plt


def convex_hull(points):
	points = sorted(set(points))
	def cross(o, a, b):
		return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

	lower = []
	for p in points:
		while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <=0:
			lower.pop()
		lower.append(p)

	upper = []
	for p in reversed(points):
		while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
			upper.pop()
		upper.append(p)

	return lower[:-1] + upper[:-1]

points = [(i//10, i%10) for i in range(100)]
hull = convex_hull(points);
#points = np.random.rand(10, 2)
#hull = ConvexHull(points)

plt.plot(hull)
#plt.plot(points[:, 0], points[:,1], 'o')
#for simplex in hull.simplices:
#	plt.plot(points[simplex,0], points[simplex,1], 'r-')

plt.show()