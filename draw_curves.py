import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

plt.rcParams['figure.figsize'] = [6,4]

def smoothen(Y):
	window_len = 15
	extra_points = window_len / 2
	kernel = np.ones(window_len, dtype=float) / window_len
	extended_Y = np.concatenate((extra_points * [Y[0]], Y, extra_points * [Y[-1]]))
	return np.convolve(extended_Y, kernel, 'same')[extra_points:-extra_points]

def draw(points, title, file, points1 = None):
	X = [x for x, y in points]
	Y = [y for x, y in points]
	new_X = np.linspace(0, 85, 100)

	itp = interp1d(X, Y, kind='linear')
	plt.plot(new_X, smoothen(itp(new_X)), color='#27408b', label='men')

	if points1:
		X1 = [x for x, y in points1]
		Y1 = [y for x, y in points1]

		itp = interp1d(X1, Y1, kind='linear')
		plt.plot(new_X, smoothen(itp(new_X)), color='#4876ff', label='women')


	ax = plt.gca()
	ax.set_xticks([0, 13, 18, 25, 35, 45, 55, 65, 75, 85])
	ax.set_yticks([0, 1.0])
	ax.legend(loc='best')

	plt.title(title, y=1.08)
	plt.xlim((0, 85))
	plt.xlabel('Age')
	plt.ylabel('Probability')
	plt.tight_layout()
	plt.savefig(file + '.pdf')
	plt.savefig(file + '.png')
	plt.close()
	# plt.show()


low = 0.1
high = 0.9

points = [(0, 0.6), (18, low), (25, low), (40, low), (65, 0.3), (75, high), (85, high)]
draw(points, 'Expected Probability to be in a Dublin Procedure by Age\nLabor Market Integration', 'fig1')

points = [(0, 0.6), (10, 0.5), (14, low), (30, low), (45, 0.6), (65, high), (85, high)]
draw(points, 'Expected Probability to be in a Dublin Procedure by Age\nPhysical Fitness', 'fig2')

points = [(0, low), (13, low), (18, 0.3), (25, high), (35, high), (65, 0.35), (85, low)]
points1 = [(0, low), (13, low), (18, 0.3), (25, high - 0.2), (35, high - 0.2), (65, 0.35), (85, low)]
draw(points, 'Expected Probability to be in a Dublin Procedure by Age\nCriminality', 'fig3', points1)
