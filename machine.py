def car (manufacturer,brand,**car_make):
	cars = {}
	cars ['Производитель'] = manufacturer
	cars ['Марка авто']	   = brand
	for key,value in car_make.items():
		cars[key] = value
	return cars

# machineq = car('lada','priora',
# 			  region = 'Moskva',
# 			  dvigatel = '16 litrov')
# print(machineq)