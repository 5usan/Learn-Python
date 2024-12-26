import re

#Regex
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d*)\]"
result = re.search(regex, log)
result1 = re.search(regex, "A completely different string that also has numbers [3452335] in the sentence.")
print(result[1])
print(result1[1])


# Regex expression

# .(dot) matches every characters

# To search from the start of any strings we use: ^ before that string. Example:
#       ^fruit
#       it prints: fruit, fruits, fruiters, fruit's, etc.

# To search from the end of any strings we use: $ after that string. Example:
#       cats$
#       it prints: hercats, himcats, thiscats, etc.

print(re.search(r"p.ng", "penguin"))
print(re.search(r"p.ng", "clapping"))
print(re.search(r"p.ng", "spong"))

#For case insensitive
print(re.search(r"p.ng", "PENGuin", re.IGNORECASE))

#To match only certain characters
print(re.search(r"[Pp]ython", "Python"))
print(re.search(r"[Pp]ython$", "Hello_python"))
print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go")) #This prints None as regex does not match since there is space( ) before way
print(re.search(r"^hi[a-zA-Z0-9]", "history"))

#To match either one expression or another
print(re.search(r"cats|dogs", "I love cats."))
print(re.search(r"cats|dogs", "I love dogs."))
print(re.search(r"cats|dogs", "I love both cats and dogs.")) #Returns the first item that matched
print(re.findall(r"cats|dogs", "I love both cats and dogs.")) #Returns every items that matched

#Repeated characters
print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programmin")) #Matches upto last n in "programmin"
print(re.search(r"Py[a-z]*n", "Python Programmin")) #Matches Python
print(re.search(r"Py[a-z]*n", "Pyn"))

#Optional Characters
print(re.search(r"p?each", "each"))
print(re.search(r"p?each", "peach"))

#Match a actual dot(.) in strings
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "welcome.com"))

#Match letter, numbers and underscore(_) easily => \w is used
print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_anoth0er_example"))

# \d => matching digits 
# \s => matching whitespace characters as space, tab, or new line
# \b => word boundaries

# For refrences www.reges101.com


#Mixing all these regex patterns
print(re.search(r'^A.*a$', "Argentina"))
print(re.search(r'^A.*a$', "America"))
print(re.search(r'^A.*a$', "American")) #None

#Valid variable names in python
print(re.search(r"^[a-zA-Z_]\w*$", "hello123"))
print(re.search(r"^[a-zA-Z_]\w*$", "_hello123"))
print(re.search(r"^[a-zA-Z_]\w*$", "1hello123"))
print(re.search(r"^[a-zA-Z_]\w*$", "h_ello123"))
print(re.search(r"^[a-zA-Z_]\w*$", "h_el!lo123"))

#Check web addresses
def check_web_address(text):
  pattern = r"^[A-Za-z][A-Za-z_-]*[\.[A-Za-z]*]*$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True

#Check time regular expression that follows: the hour is between 1 and 12, with no leading zero, followed by a colon, then minutes between 00 and 59, then an optional space, and then AM or PM, in upper or lower case.
def check_time(text):
  pattern = r"^[1]?[0-9]:[0-5][0-9][ ]?[AaPp][Mm]$"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False
print(check_time("6:02 am")) # True
print(check_time("6:02km")) # False

#Checks the text for the presence of 2 or more characters or digits surrounded by parentheses, with at least the first character in uppercase (if it's a letter), returning True if the condition is met, or False otherwise.
def contains_acronym(text):
  pattern = r"^.*\([A-Za-z0-9]*\).*$"
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True

def rearrange_name(name): 
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result == None:
        return False
    return "{} {}".format(result[2], result[1])

print(rearrange_name("Shrestha, Susan"))
print(rearrange_name("Shrestha?, Susan"))

#Repeatation Qualifiers
print(re.search(r"[A-Za-z]{5}", "a ghost"))
print(re.findall(r"[A-Za-z]{5}", "a scary ghost appeared")) #Matches all words that are greater or equal to 5 and prints only 5 characters
print(re.findall(r"\b[A-Za-z]{5}\b", "a scary ghost appeared")) #\b is used to match word with exact 5 characters
print(re.findall(r"\w{5,10}", "I really like straberries")) #Matches all words that are between the length of 5 to 10
print(re.findall(r"\w{5,}", "I really like straberries")) #Matches all words that are greater or equal to 5 and prints all characters associate to that word.
print(re.findall(r"s\w{,20}", "I really like straberries")) #Matches all words that are less than 20 characters and starts with s

#other methods of re module
print(re.split(r"[.?!]", "One sentence. Another one? And the last one!")) #Splits the word without matching character
print(re.split(r"([.?!])", "One sentence. Another one? And the last one!")) #Splits the word with matching character
print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com")) #Replace the characters with matching characters
print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada"))

def transform_record(record):
  new_record = re.sub(r"(\d{3})-(\d{3}-?\d{4})", r"+1-\1-\2", record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer

def multi_vowel_words(text):
  pattern = r"\w*[aeiouAEIOU]{3,}\w*"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []

def transform_comments(line_of_code):
  result = re.sub(r'#{1,}\s', '// ', line_of_code)
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"

def convert_phone_number(phone):
  result = re.sub(r"(\b\d{3}\b)-(\b\d{3}\b-\b\d{4}\b)", r"(\1) \2", phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300



