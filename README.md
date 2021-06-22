# Choose your own adventure template
## Made for Majed K.

Each script represents a branch. Your very first one should be called something like **Start** or something similar to that. This would be the file you start executing from. Everything will run from this central terminal.

Each file will follow a particular structure:

```py
# It would probably be good practice to include a comment at the top detailing the choice that lead to the module.

from UserChoice import user_choice # This line should look the exact same in every module.
import (first choice module)
import (second choice module)

def branch(): # Should be named branch for consistency
	print("Message that the user will read. You can do anything you want here.")

	user_choice({ # Reference the user_choice module
		"Open the door": ["open", First_First.branch],
		"Do the barrel roll": ["roll", First_Second.branch]
	})
```

The most important part to understand is the argument you pass into user_choice. I don't know if you're familiar with this, but it's a dictionary representing a custom key and value pair. In our case, the key is the action name, and the value is a list containing two pieces of information:


* The first piece of information is the text the user will input for the action. This is not case sensitive.
* The second item in the list represents the choice module. If you keep it consistent, each module's function should be called branch. This way you can just add module.branch as the list item. Do not forget the .branch part or it will throw an error.

Make sure user_choice() argument is surrounded by curly brackets {} in order to indicate a dictionary.

As for file naming, I realized that there is probably no way to keep it clean and easy, so just name it however you feel is appropriate and import it properly, unless you can think of something that I didn't.

Also note that you can add as many options as you please as long as you add it in the user_choice argument dictionary and import the module for it.

**That's all! just keep this format and you'll be fine. You shouldn't have to touch the user_choice module which contains the only if statement required for this project. You can change what you want and make it as complex as you want, just keep it consistent and clean.**