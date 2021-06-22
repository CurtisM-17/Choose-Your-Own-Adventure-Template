def user_choice(choice_map):
	map_items = choice_map.items()

	message_string = ""
	for display, choice_info in map_items:
		if message_string:
			message_string += ", "
		message_string += display + ' ("' + choice_info[0] + '")'

	def get_choice():
		choice = input(message_string + ": ")
		selected_successfully = False

		for _, choice_info in map_items:
			if choice_info[0].lower() == choice.lower():
				print("-"*45) # Separates the line so the user can easily see
				choice_info[1]()
				selected_successfully = True
				break

		if not selected_successfully:
			print("Invalid input. Please choose one of the options.")
			get_choice()

	get_choice()

	#choice = input(choice_map)