'''
判断是否是闰年
'''

year = int(input('please input year:'))
is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
print(is_leap)