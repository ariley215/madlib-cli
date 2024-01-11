def welcome_message():
  print( " Welcome to the Mad Libs Game\n\nGet ready for a hilarious and creative adventure with words! Mad Libs is a word game where you fill in the blanks with various types of words to create a funny and often absurd story.\n\nHere's how it works:\n\n1. You'll be prompted to enter different types of words such as nouns, verbs, adjectives, etc.\n2. Once you've provided all the words, we'll use them to fill in the blanks in a pre-written story.\n3. The result? A unique and wacky tale that you helped create!\n\nTo get started, simply follow the prompts and type in the requested words. If you're not sure what type of word to enter, we'll give you a clue. Have fun and let your imagination run wild!\n\nNow, let's embark on a word-filled journey!")

def read_template(file_path):
  with open('assets/dark_and_stormy_night_template.txt', 'r') as file:
    content = file.read()
    print(content)
    return content


def parse_template(content):
  actual_stripped =
  actual_parts = ()
  while '{' in content and '}' in content:
    start_index = content.find('{')
    end_ind
  print("parse file")


def merge():
  print("merge")