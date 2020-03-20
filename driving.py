country = input('which country: ')
age = input('enter your age: ')
age = int(age)
if country == 'China':
	if age >= 18:
		print('you can take a driving test.')
	else:
		print('you can not take a driving test.')