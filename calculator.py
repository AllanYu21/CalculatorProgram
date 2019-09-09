def check_HDL(HDL_result):
	if HDL_result >= 60:
		return "Normal"
	elif 40<=HDL_result<60:
		return "Borderline low"
	else:
		return "low"	


def cholestroal_interface():
	print("Cholesterol check")
	chol_input = input("Enter your cholestroal test result: ")
	chol_data = chol_input.split("=")
	if chol_data[0] == "HDL":
		result = check_HDL(int(chol_data[1]))
		print("The result is {}".format(result))



def interface():
	print("My caluclator porgram")
	keep_running = True

	while keep_running:
		print("Option: ")
		print("1 - Cholesterol Checks")
		print("9 - Quit")

		choice = input("Enter your choice: ")
		if choice == '9':
			keep_running = False
		elif choice == '1':
			cholestroal_interface()



if __name__ == "__main__":
	interface()
