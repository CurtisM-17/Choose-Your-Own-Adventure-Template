constants = [] # Empty list of constants

def user_choice(choice_map: dict, *other_variables):
	map_items = choice_map.items() # Reference the choice map dictionary

	# Create the string that will display the choices to the user
	message_string = ""
	for display, choice_info in map_items:
		if message_string:
			message_string += ", "
		message_string += display + ' ("' + choice_info[0] + '")'

	# Get the user's input and make sure it's one of the choices
	def get_choice():
		choice = input(message_string + ": ")
		selected_successfully = False

		for _, choice_info in map_items:
			if choice_info[0].lower() == choice.lower():
				print("-"*45) # Separates the line so the user can easily see
				choice_info[1](*constants, *other_variables)
				selected_successfully = True
				break

		if not selected_successfully:
			print("Invalid input. Please choose one of the options.")
			get_choice()

	get_choice()

# Define constants that are automatically passed through each choice
def add_constants(*new_constants):
	for const in new_constants:
		constants.append(const)