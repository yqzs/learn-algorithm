voter = dict()
def check_voter(name):
	if voter.get(name):
		print("kick them out")
	else:
		voter[name] = True
		print("let them vote")
		
check_voter("Tom")
check_voter("Nick")
check_voter("Tom")