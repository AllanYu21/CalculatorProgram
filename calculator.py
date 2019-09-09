def interface():
	print("My caluclator porgram")
	keep_running = True

	while keep_running:
		print("Option: ")
		print("9 - Quit")
		choice = input("Enter your choice: ")
		if choice == '9':
			keep_running = False



if __name__ == "__main__":
	interface()
