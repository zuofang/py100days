'''
 输入半径计算圆的周长和面积
'''
import math

radius = float(input('please input radius:'))
perimeter = 2*math.pi*radius
area = math.pi*radius*radius
print('perimter: %.2f' % perimeter)
print('area: %.2f' % area)