def welcome_message():
  print( " Welcome to the Mad Libs Game\n\nGet ready for a hilarious and creative adventure with words! Mad Libs is a word game where you fill in the blanks with various types of words to create a funny and often absurd story.\n\nHere's how it works:\n\n1. You'll be prompted to enter different types of words such as nouns, verbs, adjectives, etc.\n2. Once you've provided all the words, we'll use them to fill in the blanks in a pre-written story.\n3. The result? A unique and wacky tale that you helped create!\n\nTo get started, simply follow the prompts and type in the requested words. If you're not sure what type of word to enter, we'll give you a clue. Have fun and let your imagination run wild!\n\nNow, let's embark on a word-filled journey!")

def read_template(file_path):
  with open(file_path, 'r') as file:
    content = file.read()
    print(content)
    return content

import re

def parse_template(content):
  # pattern = r'\{([^\{\}]+)\}'
  pattern = r"{([\w ',.-]+)}"
  matches = tuple(re.findall(pattern, content))
  actual_stripped = re.sub(pattern, '{}', content)
  actual_parts = matches
  return actual_stripped, actual_parts
  

user_input = input("Please enter 2 adjectives and then a noun: " )
print(tuple(user_input))

def merge(actual_stripped, user_input):
  return actual_stripped.format(*user_input)

