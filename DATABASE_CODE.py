
import pandas as pd

def database(image_id, object_class, accuracy):

	#listt = i_string.split(":")[1:]

	accuracy = float(accuracy)/100
	count = 1

	try:
		with open("database.csv", "r") as file:
			count = len(file.readlines()) 
			data = {"index": count, "Image_ID" : [image_id], "Object_Class" : [object_class], "Accuracy (%)": [accuracy]}
			df = pd.DataFrame.from_dict(data)

			df.to_csv("database.csv", mode='a', index=False, header=False)
			#print("HERE")
	except:
		with open("database.csv", "w") as file:
			data = {"index": count, "Image_ID" : [image_id], "Object_Class" : [object_class], "Accuracy (%)": [accuracy]}
			df = pd.DataFrame.from_dict(data)

			df.to_csv("database.csv", mode='a', index=False, header=True)

	return 0

# a = "141:dogs_bablu:dog:10000"
# error = database("dogs_bablu", "dog", "10000")