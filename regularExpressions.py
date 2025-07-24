
import re

txt = "123 4567 89"
print(re.findall(r"\d{3}", txt))  
# r= raw-string, ""= inside a string, \d = check digit inside the string, {}= length of the digit 
# → ['123', '456']

txt = "1 12 123 1234"
print(re.findall(r"\d{2,}", txt))
# r = raw-string, \d = check digit inside the string, {2,} = length of the digit 2 or more  
# → ['12', '123', '1234']

txt = "a ab abc abcd abcde"
print(re.findall(r"\w{2,4}", txt))  
# r = raw-string, \w = check word character, {2,4} = length of the word character 2 to 4
# → ['ab', 'abc', 'abcd', 'abcd']


txt = "Ich habe einen Hund und eine Katze."
print(re.findall(r"Hund|Katze", txt))  
# r = raw-string, | = or, Hund|Katze = check for either 'Hund' or 'Katze'
# → ['Hund', 'Katze']

txt = "7hallo*"
print(re.findall(r"\d|[a-zA-Z]", txt))  
# r = raw-string, \d = check digit, | = or, [a-zA-Z] = check for letters (both lowercase and uppercase)
# → ['7', 'h', 'a', 'l', 'l', 'o']


txt = "abababab"
print(re.findall(r"(ab){3}", txt)) 
# r = raw-string, (ab) = check for 'ab', {3} = check for 3 occurrences of 'ab'
# → ['ab']

txt = "Name: Martin, Alter: 54"
match = re.search(r"Name: (\w+), Alter: (\d+)", txt)
# r = raw-string, \w+ = check for word characters (name), \d+ = check for digits (age)
# the parentheses capture the matched groups
# → match object with groups for name and age
if match:
    print(match.group(1))  # → Martin
    print(match.group(2))  # → 54

txt = "abc123xyz"
print(re.findall(r"[a-z]", txt))
# r = raw-string, [a-z] = check for lowercase letters  
# → ['a', 'b', 'c', 'x', 'y', 'z']

txt = "abc123"
print(re.findall(r"[0-9]", txt))  
# r = raw-string, [0-9] = check for digits
# → ['1', '2', '3']

txt = "Preis: 100€"
print(re.findall(r"\d+", txt))  
# r = raw-string, \d+ = check for one or more digits
# → ['100']

txt = "a.b"
print(re.findall(r"a\.b", txt))  
# r = raw-string, a\.b = check for 'a.b' (the dot is escaped with \) . = matches any character
# → ['a.b']

txt = "abc 123 a-c"
print(re.findall(r"a.c", txt))  

# → ['abc', 'a-c']

txt = "Start hier, dann weiter"
print(re.findall(r"^Start", txt))  
# r = raw-string, ^Start = check if the string starts with 'Start'
# → ['Start']

txt = "Alles gut am Ende"
print(re.findall(r"Ende$", txt))  
# r = raw-string, Ende$ = check if the string ends with 'Ende'
# → ['Ende']

txt = "Helloooo"
print(re.findall(r"o*", txt))  
# r = raw-string, o* = check for zero or more occurrences of 'o' *= matches zero or more times
# → ['', '', '', 'oooo', '', '']

txt = "Helloooo"
print(re.findall(r"o+", txt))  
# r = raw-string, o+ = check for one or more occurrences of 'o' + = matches one or more times
# → ['oooo']

txt = "Email: test@mail.de und info@firma.org"
print(re.findall(r"\S+@\S+\.\w+", txt))  
# r = raw-string, \S+ = check for one or more non-whitespace characters, @ = at symbol, \.\w+ = dot followed by word characters
# → ['test@mail.de', 'info@firma.org']

txt = "Hallo Martin, willkommen!"
match = re.search(r"Martin", txt)
# r = raw-string, Martin = check for the exact string 'Martin'
# If found, it returns a match object; if not, it returns None
if match:
    print(match.group())  # → Martin

txt = "Apfel, Banane; Orange / Zitrone"
print(re.split(r"[,;/]\s*", txt))  
# r = raw-string, [,;/] = split by comma, semicolon, or slash, \s* = optional whitespace after the delimiter
# → ['Apfel', 'Banane', 'Orange', 'Zitrone']

txt = "Meine Nummer ist 0176-1234567"
print(re.sub(r"\d{3,}", "XXX", txt))  
# r = raw-string, \d{3,} = check for three or more digits, "XXX" = replace with 'XXX'
# → Meine Nummer ist 0176-XXX


