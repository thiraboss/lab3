def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}
	
def students():
	Student = [
	{'id': '59011597', 'firstname': 'Chatchanok', 'lastname': 'Wongsamang'},
	{'id': '59011598', 'firstname': 'Jiramate', 'lastname': 'Leingprom'},
	{'id': '59011599', 'firstname': 'Jirayu', 'lastname': 'Promsongwong'},
	{'id': '59011600', 'firstname': 'Kitpol', 'lastname': 'Tansakul'},
	{'id': '59011601', 'firstname': 'Nattamon', 'lastname': 'Sridam'},
	{'id': '59011602', 'firstname': 'Peeranat', 'lastname': 'Limpitaporn'},
	{'id': '59011604', 'firstname': 'Phison', 'lastname': 'Khankang'},
	{'id': '59011605', 'firstname': 'Thirawat', 'lastname': 'Rungrojchaiyaporn'}
	]
	return Student
	
allStudent = students()
def students_get(index):
    for i in allStudent:
        if index == i['id']:
            print('yeah')
            return i
            break
