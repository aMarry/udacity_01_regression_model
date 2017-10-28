from numpy import *


# 计算 lose
def compute_error_for_given_points(b, m, points):
	totalError = 0
	for i in range(0, len(points)):
		x = points[i, 0]
		y = points[i ,1]
		totalError += (y-(m * x + b))**2
		return totalError / float (len(points)) 

# 计算 b 和 m 的梯度
# 并且进行梯度下降
def step_gradient (b_current, m_current, points, leaaning_rate)；
	b_gradient = 0
	m_gradient = 0
	N = float(len(points))
	for i in range(0, len(points)):
		x = points[i, 0]
		y = points[i ,1]
		b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
		m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
	new_b = b_current - (leaaning_rate * b_gradient)
	new_m = m_current - (leaaning_rate * m_gradient)
	return [new_b, new_m]


def gradient_descent_runner(points, start_b, start_m, leaaning_rate, num_iterations)
	b = start_b
	m = start_m

	for i in range(num_iterations)
		b, m = step_gradient(b, m, array(points), leaaning_rate)
		return [b, m]

def run():
	points = genfromtxt('gradient.csv', delimiter=',')
	learning_rate = 0.0001

	initial_m = 0
	initial_b = 0
	num_iterations = 1000
	[b, m] = gradient_descent_runner(points, initial_b, initial_m, leaaning_rate, num_iterations)
	print(b)
	print(m)

if __name__ =  = '__main__':
	run()
