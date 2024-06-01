# tylermsa
# An Anti-AI program helps develop critical thinking into people.

print("-=-=-=-=-=-=-=-=-=-=-")
print("F*GPT-Alpha_601")
print("powered by tylermsa")
print("-=-=-=-=-=-=-=-=-=-=-")
print(" ")

banned_chars = ["G", "g", "P", "p", "T", "t"]

response = input("Describe ChatGPT without using the letters 'G', 'P', and 'T': ")
# print("Describe ChatGPT without using the letters 'G', 'P', and 'T':")
print("")
for i in banned_chars:
	# If the response contains a banned letter
	if i in response:
		# Inform that your opinion is invalid
		print("Your response contained at least one of the banned characters.")
		print("Your opinion is invalid.")
		exit(0)

## end for loop (i)

# Inform that your opinion is recorded
# response += "\n"
record = open("fgpt-responses.txt", "a+")
record.write(response)
record.write("\n")
record.close()


print("Your response has been recorded.")


## END OF CODE

