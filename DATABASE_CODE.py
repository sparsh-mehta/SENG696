
import pandas as pd

def database(i_string):

	listt = i_string.split(":")[1:] 
 
	count = 1

	try:
		with open("database.csv", "r") as file:
			count = len(file.readlines()) 
			data = {"index": count, "img_id" : [listt[0]], "object_class" : [listt[1]], "accuracy": [listt[2]]}
			df = pd.DataFrame.from_dict(data)

			df.to_csv("database.csv", mode='a', index=False, header=False)
			#print("HERE")
	except:
		with open("database.csv", "w") as file:
			data = {"index": count, "img_id" : [listt[0]], "object_class" : [listt[1]], "accuracy": [listt[2]]}
			df = pd.DataFrame.from_dict(data)

			df.to_csv("database.csv", mode='a', index=False, header=True)

	return 0

a = "141:dogs_bablu:dog:09785"
# error = database(a)
