import json
my_dict={}

def check_HDL(HDL_result):
	if HDL_result >= 60:
		return "Normal"
	elif 40<=HDL_result<60:
		return "Borderline low"
	else:
		return "low"	

def check_LDL(LDL_result):
	if LDL_result >= 190:
		return "Very High"
	elif 160<=LDL_result<190:
		return "High"
	elif 130<=LDL_result<160:
		return "Borderline high"
	else:
		return "Normal"

def cholestroal_interface():
	print("Cholesterol check")
	chol_input = input("Enter your cholestroal test result: ")
	chol_data = chol_input.split("=")
	if chol_data[0] == "HDL":
		result = check_HDL(int(chol_data[1]))
		print("The result is {}".format(result))
		my_dict["result"] = ("The result is {}".format(result))
	elif chol_data[0] == "LDL":
		result = check_LDL(int(chol_data[1]))
		print("The result is {}".format(result))
		my_dict["result"] = ("The result is {}".format(result))

def patient_interface():
	print("Patient Input")
	name = input("Enter patient name: ")
	age = int(input("Enter patient age: "))
	my_dict["name"] = name
	my_dict["age"] = age


def upload_JSON():
	out_file = open("patientData.json", "w")
	json.dump(my_dict, out_file)
	out_file.close()
 	
	



def interface():
	print("My caluclator porgram")
	keep_running = True

	while keep_running:
		print("")
		print("Option: ")
		print("1 - Cholesterol Checks")
		print("2 - Patient Input")
		print("3 - Upload JSON")
		print("9 - Quit")

		choice = input("Enter your choice: ")
		if choice == '9':
			keep_running = False
		elif choice == '1':
			cholestroal_interface()
		elif choice == '2':
			patient_interface()
		elif choice == '3':
			upload_JSON()



if __name__ == "__main__":
	interface()
