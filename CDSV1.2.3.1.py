import tkinter as tk #this is our gui
import re #this is RegEx, our text tool. It's a common library for many languages
import itertools #using this is the quick fix to a single iteration problem I had
import random #only needed for some unspecified and funky actions
from tkinter.filedialog import askopenfilename,asksaveasfile
import unicodedata #this is for working with diacritics


#the following GUI setup is horrible and bad and reflects the many times I changed the interface. 

#At some point I should maybe make the window resize to fit your monitor nicely, and all of the frames with it.
#basic functionality first

window = tk.Tk()
window.title("Cryptolang Automaton")
title = tk.Label(text="Cryptolang Automaton")
master_frame = tk.Frame(relief=tk.RAISED, borderwidth=5)
frame_a = tk.Frame(master=master_frame,relief=tk.RAISED, borderwidth=5)
frame_b = tk.Frame(master=frame_a,relief=tk.RIDGE, borderwidth=5, width = 100, height =2)
frame_c = tk.Frame(master=frame_a,relief=tk.RIDGE, borderwidth=5, width = 100, height = 10)
frame_d = tk.Frame(master=frame_a,relief=tk.RIDGE, borderwidth=5, width = 100, height = 10)
frame_status = tk.Frame(master=frame_a,relief=tk.RIDGE, borderwidth=5, width = 100, height = 20)
frame_e = tk.Frame(master=master_frame,relief=tk.RIDGE, borderwidth=5, width = 20, height = 10)
frame_button = tk.Frame(relief=tk.RIDGE)
frame_radios = tk.Frame(frame_a, relief=tk.RIDGE)
frame_r1=tk.Frame(frame_radios, relief=tk.RIDGE)
frame_r2=tk.Frame(frame_radios, relief=tk.RIDGE)

rulesinput = tk.Text(master = frame_b, width = 100, height =2)
plaininput = tk.Text(master=frame_c,width = 100, height =10)
output = tk.Text(master=frame_d,width = 100, height =10)
output.tag_configure("alternate", foreground="blue")
status = tk.Text(master=frame_status,width = 100, height =15)
status.tag_configure("warning", foreground="red")
status.tag_configure("alternate", foreground="blue")
utitle = tk.Label(master=frame_e,text="All valid Symbols [X]")
universebox = tk.Text(master=frame_e,width = 20, height =4)
ctitle = tk.Label(master=frame_e,text="Consonants [C]")
consonants = tk.Text(master=frame_e,width = 20, height =2)
vtitle = tk.Label(master=frame_e,text="Vowels [V]")
vowels = tk.Text(master=frame_e,width = 20, height =2)
cdtitle = tk.Label(master=frame_e,text="Consonant Digraphs [Ch]")
consonantdigraph = tk.Text(master=frame_e,width = 20, height =2)
svtitle = tk.Label(master=frame_e,text="Semivowels [Y]")
semivowel = tk.Text(master=frame_e,width = 20, height =2)
vdtitle = tk.Label(master=frame_e,text="Vowel Digraphs [Vh]")
voweldigraph = tk.Text(master=frame_e,width = 20, height =2)
sotitle = tk.Label(master=frame_e,text="Sonorants [N]")
sonor = tk.Text(master=frame_e,width = 20, height =2)
fltitle = tk.Label(master=frame_e,text="Non-Sonorants [Cn]")
nonsonorants = tk.Text(master=frame_e,width = 20, height =2)
vctitle = tk.Label(master=frame_e,text="Complexes [Cm]")
complexes = tk.Text(master=frame_e,width = 20, height =2)
u1title = tk.Label(master=frame_e,text="User-defined group [Ua]")
u1 = tk.Text(master=frame_e,width = 20, height =2)
u2title = tk.Label(master=frame_e,text="User-defined group [Ub]")
u2 = tk.Text(master=frame_e,width = 20, height =2)
u3title = tk.Label(master=frame_e,text="User-defined group [Uc]")
u3 = tk.Text(master=frame_e,width = 20, height =2)
droptitle = tk.Label(master=frame_e,text="Dropped Characters")
drop = tk.Text(master=frame_e,width = 20, height =2)

trackchanges = tk.IntVar()
trackchanges.set(1)
r1 = tk.Radiobutton(master=frame_r1, text="Use capitals to indicate changed text", variable=trackchanges, value=1)
r2 = tk.Radiobutton(frame_r1, text="Use colours to indicate changed text", variable=trackchanges, value=2)
r3 = tk.Radiobutton(frame_r1, text="Do not indicate changes", variable=trackchanges, value=3)

diacritics = tk.IntVar()
diacritics.set(1)
d1 = tk.Radiobutton(frame_r2, text="Treat diacritics as separate characters", variable=diacritics, value=1)
d2 = tk.Radiobutton(frame_r2, text="Erase all diacritic marks", variable=diacritics, value=2)
d3 = tk.Radiobutton(frame_r2, text="Transfer diacritics to new characters", variable=diacritics, value=3)

translate = tk.Button(text="Translate", master = frame_button)
savefile = tk.Button(text="Save Config File",master = frame_button)
loadfile = tk.Button(text="Load Config File",master = frame_button)
generate = tk.Button(text="Generate", master = frame_button)


#everything's been defined, now I need to use pack & grid commands to lay it all out

title.pack()
r1.pack(anchor=tk.W)
r2.pack(anchor=tk.W)
r3.pack(anchor=tk.W)
d1.pack(anchor=tk.W)
d2.pack(anchor=tk.W)
d3.pack(anchor=tk.W)
frame_r1.grid(row=0, column=0, padx=5)
frame_r2.grid(row=0, column=1, padx=5)
frame_radios.pack()
rulesinput.pack()
plaininput.pack()
output.pack()
status.pack()
translate.grid(row=0, column=0, padx=5)
savefile.grid(row=0, column=1, padx=5)
loadfile.grid(row=0, column=2, padx=5)
generate.grid(row=0, column=3, padx=5)
frame_button.pack()
utitle.pack()
universebox.pack()
ctitle.pack()
consonants.pack()
vtitle.pack()
vowels.pack()
cdtitle.pack()
consonantdigraph.pack()
svtitle.pack()
semivowel.pack()
vdtitle.pack()
voweldigraph.pack()
sotitle.pack()
sonor.pack()
fltitle.pack()
nonsonorants.pack()
vctitle.pack()
complexes.pack()
u1title.pack()
u1.pack()
u2title.pack()
u2.pack()
u3title.pack()
u3.pack()
droptitle.pack()
drop.pack()
frame_a.grid(row=0, column=0, pady=5)
frame_b.pack()
frame_c.pack()
frame_d.pack()
frame_status.pack()
frame_e.grid(row=0,  column=1,  padx=5)
master_frame.pack()

#can't help but feel there's a more efficient way to do all of the above. Ah well, only have to do it once.



#pre-fill all the user-fields
rulesinput.insert(tk.END, "ExAmPlE_RU, LE#_S(WIT{HNE}SeT)D_BLO[C]\\KS\\")
plaininput.insert(tk.END, "put plaintext here")
output.insert(tk.END, "output will show here")
consonants.insert(tk.END, "BCDFGHJKLMNPQRSTVWXYZ")
vowels.insert(tk.END, "AEIOU")
universebox.insert(tk.END, "AEIOUBCDFGHJKLMNPQRSTVWXYZ'.?!@$%&")
consonantdigraph.insert(tk.END, "<Ch><Sh><Th>")
voweldigraph.insert(tk.END, "<oo><ie><ei><ee><ao>")
semivowel.insert(tk.END, "Y")
sonor.insert(tk.END, "HLMNRW")
nonsonorants.insert(tk.END, "BCDFGJKPQSTVXZ")
complexes.insert(tk.END, "CJQX")
drop.insert(tk.END, "`")
#the above is all just setting up the GUI; most of which is taken directly from a tutorial on tkinter
#The important thing is: I now have a window that I can call "window_mainloop()" on, which will create a while loop
#that listens for events, (such as keypresses, clicking on buttons, etc.), and performs actions until the window is closed
#I will be structuring this around a single function that triggers when a button is pressed. The minimizes the number of things someone
#needs to learn if they're trying to modify the code

#initialize user-defined variables
consonantlist = consonants.get("1.0",tk.END).strip("\n") #text boxes alwats insert a /n at the end, it's really annoying
vowellist = vowels.get("1.0", tk.END).strip("\n")
cdigraphs = consonantdigraph.get("1.0", tk.END).strip("\n")
vdigraphs = voweldigraph.get("1.0", tk.END).strip("\n")
svowels = semivowel.get("1.0", tk.END).strip("\n")
sonors = sonor.get("1.0", tk.END).strip("\n")
nonsonorant = nonsonorants.get("1.0", tk.END).strip("\n")
complexs = complexes.get("1.0", tk.END).strip("\n")
user1 = u1.get("1.0", tk.END).strip("\n")
user2 = u2.get("1.0", tk.END).strip("\n")
user3 = u3.get("1.0", tk.END).strip("\n")
universe = universebox.get("1.0", tk.END).strip("\n") #this is what we will use anytime we're looking for any valid character
dropped = drop.get("1.0", tk.END).strip("\n")

#initialize the priorty queue so that it's a global variable
statusqueue = []


def printstatusqueue(intermediary):
	status.delete("1.0", tk.END)
	intermediary.sort(key=lambda thing: thing[0])
	for it in intermediary:	
		z = None
		if len(it) > 2:
			x,y,z = it
		else:
			x,y = it	
		status.insert(tk.END,y,z)
		
	


def updatefields(): #we'll use this anytime we need to update all of the user-defined fields
	global consonantlist
	global vowellist 
	global cdigraphs
	global vdigraphs 
	global svowels 
	global sonors 
	global nonsonorant 
	global complexs
	global user1 
	global user2 
	global user3 
	global universe 
	global drop
	consonantlist = consonants.get("1.0",tk.END).strip("\n") #text boxes alwats insert a /n at the end, it's really annoying
	vowellist = vowels.get("1.0", tk.END).strip("\n")
	cdigraphs = consonantdigraph.get("1.0", tk.END).strip("\n")
	vdigraphs = voweldigraph.get("1.0", tk.END).strip("\n")
	svowels = semivowel.get("1.0", tk.END).strip("\n")
	sonors = sonor.get("1.0", tk.END).strip("\n")
	nonsonorant = nonsonorants.get("1.0", tk.END).strip("\n")
	complexs = complexes.get("1.0", tk.END).strip("\n")
	user1 = u1.get("1.0", tk.END).strip("\n")
	user2 = u2.get("1.0", tk.END).strip("\n")
	user3 = u3.get("1.0", tk.END).strip("\n")
	universe = universebox.get("1.0", tk.END).strip("\n") #this is what we will use anytime we're looking for any valid character
	dropped = drop.get("1.0", tk.END).strip("\n")


	def processfield(field): #this makes sure to add both lower and uppercase letters to our fields, it makes backslash groups into () groups, and it makes <> groups into () groups. 
		field = field.upper() + field.lower()
		field = "["+field+"]"
		multichar = re.findall(r"\<[^\>]*\>", field)
		multichar.sort(key=len, reverse=True) #sort by length, so that it tries to match the longest ones first. But this needs to be in descending order 
		for entry in multichar:
			field = field.replace(entry, "", 1)
			field = "(" + entry.strip("<>") + ")|" + field	#because down here, we're building left from the main field.
		if re.search(r"\[\]", field): #nothing inside the []
			field = field.replace("|[]", "", 1) 	
		return field

		
	universe = processfield(universe)
	consonantlist = processfield(consonantlist)
	vowellist = processfield(vowellist)
	cdigraphs = processfield(cdigraphs)
	vdigraphs = processfield(vdigraphs)
	svowels = processfield(svowels)
	sonors = processfield(sonors)
	nonsonorant = processfield(nonsonorant)
	complexs = processfield(complexs)
	user1 = processfield(user1)
	user2 = processfield(user2)
	user3 = processfield(user3)
#end def updatefields


def find_matches(field, string, lexing = False): #sketch of new way of matching things to a given field. This will be used everywhere I need to find something in 'universe' or 'consonants'
	result = ""
	count = 0
	while re.match("(?i)"+field, string):
		result += re.match("(?i)"+field, string).group() #this seems to be the best way to match [A-Z]|(Ch)|(Sh) etc. in such a way that allows any group or character class to occur in any frequency
		string = string.replace(re.match("(?i)"+field, string).group(), "", 1)
		if lexing and len(string)>0:
			if string[0].isupper():
				return result #also stop when you get to another capital letter, not just when you reach a non-universe letter, but only when in the lexer
		count += 1
		if count > 1000000: 
			statusqueue.append([3, "Infinite loop in find matches, somehow\n","warning"])	
			break			
	return result
#end def find_matches



def get_rules(dosort=True): #this will be called when the translate or generate buttons are pressed, and it interprets the rulestext

	#after taking the input from the rules box, this function will first lex all of the input into tokens. 
	#Then it parses those tokens into appropriately nested functions 
	#Then it will interpret those tokens into a set of replacement rules to be followed in sequence. 
	#Then it will sort those rules so that the rules are performed correctly
	
	global statusqueue #tell the subroutine too use the global queue, not make a new local one


	updatefields()
	
	
	base = rulesinput.get("1.0", tk.END) #fetch everything in the rulesinput textbox, from beginning to end
	if not dosort: base = "A" + base.strip("\n") + "#" #if working in generater mode, append an arbitrary rule-component to the front, and make the rule non-circular by adding a #. This is a hack.
	base = re.sub(r"#(?![_$])", r"#_", base) #replace all examples of "#" not followed by a "_" with "#_", unless it's at the end of the line, (which is $)

	#the following error checks are insufficient for catching all bracket errors: "][" would pass the test, as would (ab[C)V]
	#Rulelists aren't going to be very long, so I'm happy with this
	#however, this could be properly implemented in the parser if desired.
	#at "5", these are "low level" warnings. "High level" warnings are ones that should be stopping the translation cold
	if base.count("[") < base.count("]"):
		statusqueue.append([5, "Warning: Unopened ] brackets\n", "warning"])
	if base.count("(") < base.count(")"):
		statusqueue.append([5, "Warning: Unopened ) brackets\n", "warning"])
	if base.count("{") < base.count("}"):
		statusqueue.append([5, "Warning: Unopened } brackets\n", "warning"])
	if base.count("[") > base.count("]"):
		statusqueue.append([5, "Warning: Unclosed [ brackets\n", "warning"])
	if base.count("(") > base.count(")"):
		statusqueue.append([5, "Warning: Unclosed ( brackets\n", "warning"])
	if base.count("{") > base.count("}"):
		statusqueue.append([5, "Warning: Unclosed { brackets\n", "warning"])
		

	
	base = re.split(", ", base) #first we need to break up the sets of rules into an array of strings
	rules = []  
	for ruleset in base:
		rules.append(re.split("_",ruleset)) #then in each set of rules, we need to break up each rule



	#first, let's tokenize everything in a lexer. The lexer is just straight code running, as opposed to many of the recursive functions to follow
	#It's good practice to always write a tokenizer in a way that doesn't require recursion. It should simplify everything that comes afterwards and make it well-defined, not be complex itself. 
	#There's nothing persay wrong with resurcive lexers, but the style I was taught always advised to push any recursion to the parser
	#I think many people making an L-P-I without knowing that's what they're making will skip the lexing step and simply integrate all the functions into the parser
	rulelist = []
	for ruleset in rules: #everything is now in nested arrays, so we need to crack open the first array
		rulelistinner = []
		for rule in ruleset: #and then crack open the second array
			lexing = rule
			lexed = []
			count = 0
			insidebackslash = False
			while len(lexing) > 0:
				count += 1
				if count > 1000000:
					statusqueue.append([3, "Issue when lexing, infinite loop was interupted \n", "warning"])
					statusqueue.append([3, lexing + "\n", "warning"])
					break		
				
				if not re.match("(?i)"+universe+r"|[\{\(\}\)\[\]#\s\/\<\>\\]", lexing): #check to see if the first characters are NOT any valid characters. Because of the way universe is formed, we can't use the [^ABC] constructionn of RegEx
					statusqueue.append([3, "Malformed rules at " + lexing +"\n Is/are the character(s) there supposed to be in the \"All Valid Characters\" box?\n ", "warning"])
					break
				match = re.match("(?i)"+universe, lexing) #check to see if the first characters are something that should start a normal character search
				if match:
					lexed.append("<CHARACTERS>")
					characters = find_matches(universe,lexing, True) 
					lexing =lexing.replace(characters,'',1)
					match = re.match("[1-4]", lexing)
					if match: 
						characters += "<POSITION"+match.group()+">"
						lexing = lexing.replace(match.group(),'',1)
					lexed.append(characters)
					continue	
				if lexing[0:1] == "{":
					lexed.append("<WAVY>")
					lexing = lexing.replace("{",'',1)
					continue
				if lexing[0:1] == "}":
					lexed.append("<WAVYCLOSE>")
					lexing = lexing.replace("}",'',1)
					continue
				if lexing[0:1] == "(":
					lexed.append("<CURVY>")
					lexing = lexing.replace("(",'',1)
					continue
				if lexing[0:1] == ")":
					lexed.append("<CURVYCLOSE>")
					lexing = lexing.replace(")",'',1)
					continue
				if lexing[0:1] == "#":
					lexed.append("<NOWRAP>")
					lexing = lexing.replace("#",'',1)
					continue				
				match = re.match(r"(\/)", lexing)  #check to see if the starting characters are "/ " 
				if match:
					lexing =lexing.replace(match.group(),'',1)
					lexed.append("<DELETE>")
					continue				
				match = re.match(r"\\", lexing) # check to see if there is backslash grouped text
				if match:
					if insidebackslash:				
						lexed.append("<END GROUP>")
						insidebackslash = False
					else:
						lexed.append("<CHARACTER GROUP>")
						insidebackslash = True
					lexing =lexing.replace(match.group(),'',1)
					continue		
				if lexing[0:1] == "[":
					lexed.append("<FIELD>")
					lexing =lexing.replace("[",'',1)
					characters = find_matches(universe+"|[=><0-9]",lexing) 
					lexing = lexing.replace(characters,'',1)
					lexed.append(characters)
					if lexing[0:1] == "]":
						lexed.append("<FIELDCLOSE>")
						lexing = lexing.replace("]",'',1)
					else:
						statusqueue.append([5, "Did not reach end of square brackets in lexer \n", "warning"])	
					if re.match(universe.lower(), lexing[0:1]):
						lexed.append("<FIELDCONTINUE>")
						characters = find_matches(universe,lexing)
						lexed.append(characters)
						lexing = lexing.replace(characters,'',1)
					continue	
				if lexing[0:1] == "\n": lexing =lexing.replace("\n",'',1)

			#end while	
			if insidebackslash:
				statusqueue.append([5, "Issue when lexing, unclosed backslashgroup \n", "warning"])	
	
			rulelistinner.append(lexed)		
		rulelist.append(rulelistinner)			

	#end lexer
	statusqueue.append([20, "Lexer result: " + str(rulelist) +"\n"])
	printstatusqueue(statusqueue)

 
	#valid tokens should now be "<CHARACTERS>, <WAVY>, <WAVYCLOSE>, <CURVY>,<CURVYCLOSE>, <NOWRAP>,<FIELD>, <FIELDCLOSE>, <FIELDCONTINUE>, <CHARACTER GROUP>, <END GROUP>, <DELETE>"
	#Each of these are followed by data inputs until the next symbol. Some of these are mode changes rather than data inputs, like wavy/curvy/field. Some are straight commands like nowrap or delete.
	
	def recursive_parser(block, start=0): #"recursive" means that the function will call itself. In this case, it will call itself to resolve blocks like "[text]", "(text)", and "{text}"
								#an important thing is that recursive functions always need an exit condition or else they'll just...go forever. 
								#In this case, we have a finite rules text, so there's only so many [] blocks it can contain
								#It needs to be recursive because {} and () can contain blocks inside them. An arbitrary number of.

		#If we're in a block that doesn't contain anything, exit and returning nothing.								
		if len(block) == 0: return None
		#Now, we can be certain that our block contains something.

		# if the block being passed in is an array, itself, then take each entry of the array, recursively parse it, and then remake the array with the parsed entries
		if isinstance(block[0],list): #this checks whether block is an array of arrays, or an array of elements. 
			intermediate = []
			for entry in block:
				temp = recursive_parser(entry)
				if temp: intermediate.append(temp) #if we entered empty blocks, we don't want to append "None" to our result
			return intermediate		

		

		result = []
		j = start
		count = 0
		while j < len(block):		
			if block[j] == "<CHARACTERS>":
				j += 1
				result.append(block[j])  			
			elif block[j] == "<WAVY>" or block[j] == "<CURVY>":
				j += 1 
				recursive = recursive_parser(block,j)
				j = recursive[1]
				result.append(recursive[0])
			elif block[j] == "<CURVYCLOSE>": #technically, this means that {) and (} both work. It does not care which one closes.
				return [["<CURVY>", result],j] 
			elif block[j] == "<WAVYCLOSE>":
		 		return [["<WAVY>", result],j]		
			elif block[j] == "<NOWRAP>":
				result.append(block[j])
			elif block[j] == "<DELETE>":
				result.append(" ")	
			elif block[j] == "<FIELD>": 
				topass = ""
				while j < len(block)-1:
					j += 1
					if block[j] == "<FIELDCLOSE>":
						break
					topass += block[j]	
				else:
					statusqueue.append([3, "Unclosed square bracket?", "warning"])
					return None
				topass = "[" + topass + "]" # it might seem weird to strip there and then re-equip these, but that's because the part where these are interpreted was moved. This also makes the status more readable.	
				if j + 1 < len(block):
					if block[j+1] == "<FIELDCONTINUE>":		
						j += 2				
						topass += block[j]
				result.append(topass)	
			elif block[j] == "<CHARACTER GROUP>":
				j += 1		
				recursive = recursive_parser(block,j)
				j = recursive[1]
				result.append(recursive[0])
			elif block[j] == "<END GROUP>":
				result = "".join(result) # make our array into a string
				return [result, j]	
			j += 1
			count += 1
			if count > 1000000: 
				statusqueue.append([3, "Infinite loop in Recursive Parser, somehow\n","warning"])	
				break			
		return result
	#def end recursive_parser

					
	rulelist = recursive_parser(rulelist) # until this line, none of the code above actually executes!
	statusqueue.append([12, "parser result is: " + str(rulelist) +"\n", "alternate"])	
	printstatusqueue(statusqueue)
		
		
	#Now it's time to construct our ruleset, which will consist of an ordered array of arrays of two entries; the thing to replace and the replacement. 
	#Python devs might think this is a good time for a dictionary, but dictionaries are unordered, and that's important here
	#the rule "turn A's to E's" might occur multiple times in a ruleset, doing different things each time. 
	#A sticky point: you may have noticed that there are both "_" and ", " delimiters of rules. 
	#_ denotes a different rule, ", " denotes a different rulestring
	#so rules joined by _ are all done at the same time, and then the next batch of _'s separated by ", " are done
	#So the ruleset AEIOU_EBC is invalid because E has multiple things to turn into, in general the same [A-Z][a-z]* cannot show up twice in one rule string
	#This also means that longer matches happen first!
	#So CECh as a rule would turn "Chair" into "Cair", not "Eair"
		
	def match_to_next(i, rulestring, passed = None): #this will be called when we need to decide what to replace a match with in a rule. Since we can have A(B)C, where A maps to C, and C maps to A, it isn't just "pick the next element in the array". And if we are in a () or {} block, then C should map to D, which is outside of the context entirely. In this case, "D" should be passed to the function	
		for j in itertools.chain(range(i + 1, len(rulestring)), range(0,i)): # this takes care of wrapping around for us
			if j < i and passed: #if we have a passed variable, don't wrap around to the beginning again
				return passed
			if not isinstance(rulestring[j],list) and not rulestring[j] == "<NOWRAP>":
				return rulestring[j]
				break
			elif rulestring[j] == "<NOWRAP>":
				return None #literally return nothing
				break #these breaks are just syntactic sugar for newbs, by the way
		return passed		
	#end def match_to_next


	def examine_array_of_rules(rulestring, curvybracket = False, passed = None): #this is the interpreter! It needs to be a function so that it can call itself recursively
		results = []
		next = match_to_next(0, rulestring, passed)
		if rulestring[0] == "<CURVY>": 
			results += examine_array_of_rules(rulestring[1], True,next) #recursive curvy bracket mode will match everything inside to "passed"
		elif rulestring[0] == "<WAVY>":
			results += examine_array_of_rules(rulestring[1], False,next) #recursive wavy bracket will match everything as normal until the end, then match that to "passed"
		else:	
			for i in range(0,len(rulestring)): 
				next = match_to_next(i, rulestring, passed)		
				if isinstance(rulestring[i],list): 
					results += examine_array_of_rules(rulestring[i],False,next) #We should always be entering a curvy or wavy at this point, so we need to pass next down
				elif rulestring[i] == "<NOWRAP>" or rulestring[i] == " ": #non-acting characters
					continue
				elif re.search(universe, rulestring[i]): 
					if next and not curvybracket:				
						results.append([rulestring[i], next]) # notice that we are tossing here and not at the results. If we toss the results, we lose data from inside the block, which might be an internal {}						
					elif curvybracket and passed:
						results.append([rulestring[i],passed])	
							
		return results				
	#end def examine_array_of_rules						
		
	rulesexamined = []

	for rulestring in rulelist: 
		rulesexamined.append(examine_array_of_rules(rulestring))
		
	statusqueue.append([11, "rules creator result is: " + str(rulesexamined) +"\n"])			
	printstatusqueue(statusqueue)

	for ruleset in rulesexamined: # find ill-defined strings
		norepeats = []
		for rule in ruleset:	
			if norepeats.count(rule[0]) == 1:
				statusqueue.append([5, "warning: "+ str(rule[0]) + " is repeated multiple times in one stage of encoding \n", "warning"])
			norepeats.append(rule[0])
			if re.search("<POSITION",rule[1]):
				statusqueue.append([5, "warning: "+ str(rule[1]) + " is a positional unit and should not be a replacement in a ruleset.\n", "warning"])
	#end for

	rulessorted = []	

	for ruleset in rulesexamined: #find length and sort by it.
		intermediate = [] 
		braindeadsort = []
		count = 0
		for entry in ruleset:
			keepme = entry[0] #Not sure if this works, need to check
			while len(entry[0]) > 0:
				longestsubstring = 1
				if entry[0][0] == "[":
					count += 5 #we need to find the actual length here. That's going to be a whole subroutine
					intermediate.append([keepme,entry[1],count])
					count = 0
					break	
				if re.match(universe, entry[0]): #The next entry is just a normal letter, so add it
					length = len(re.match(universe, entry[0]).group()) #because if we match <sh> or similar, it might not be a single character
					entry[0] = entry[0][length:]
					count += 1 #but we still want to count it as "one character"
					continue 					
				elif re.match(r"[1-4](?=s)", entry[0]):
					braindeadsort.append([keepme,entry[1],count])
					count = 0
					break
				elif re.match(r"\<[^>]*\>", entry[0]):
					length =len(re.match(r"\<[^>]*\>", entry[0]).group()) #this should be a position tag, just add it
					entry[0] = entry[0][length:]
					continue
				else:
					statusqueue.append([3, "Failed to match something within a matching string in the sorter\n" + "current string is: " + str(entry[0]) + "\n", "warning"])
					break						
			#end while		
			else: #if we didn't break
				intermediate.append([keepme,entry[1],count])		
				count = 0	
		#end for
		braindeadsort += intermediate		
		if dosort: braindeadsort = sorted(braindeadsort, key=lambda entry: entry[2],reverse=True) #sort by the length of the keys				
		rulessorted.append(braindeadsort)

	statusqueue.append([10, "rules sorting result is: " + str(rulessorted) +"\n", "alternate"])
	printstatusqueue(statusqueue)
	return rulessorted		
#end def get_rules()
	

def write_characters(inputblock): # used in both translate and generate, so here it needs to be outside both
	#receives something like "a[Vx<3]o"

	block = inputblock
	listofcharacters = []
	referenceswrite = []
	while len(block)>0: # bugged at current; needs to care about repeats and references 
		if re.match(universe, block):
			listofcharacters.append(["MANDATORY", block[0]])	
			block = block[1:] #and get rid of it	
		elif re.match(r"\s", block): #check to see if we're deleting something
			listofcharacters.append(["MANDATORY", ""])
			block = block[1:]		
		elif block[0] == "[":
			match = re.match(r"\[[^\]]*\]", block)
			block = block.replace(match.group(),"",1)
			subblock = square_bracket_interpreter(match.group())	
			count = 0
			while len(subblock) > 0:
				count += 1
				if count > 1000000: 
					statusqueue.append([3, "Issue writing a square bracket, infinite loop in innerwhile?\n", "warning"])	
					printstatusqueue(statusqueue)		
				if subblock[0] == "(": #are we entering a choice? (which is a () block inside a field)
					if subblock[1] == "[" or subblock[1] == "(": # if we are at the start of a ((sh)|[aeiou]) block 
						subblock = subblock[1:] #get rid of opening (
						continue
					subblock = subblock[1:] #get rid of "("
					textmatch = find_matches(universe, subblock)
					subblock = subblock.replace(textmatch,"",1)
					subblock = subblock[1:] #get rid of ")"
					if subblock[0] == "|": subblock = subblock[1:]
					listofcharacters.append(["CHOICE", textmatch])
					continue		
				elif subblock[0] == ")": #this only happens when we have a "([sadflkajshf])" construction, otherwise the ) is matched
					subblock = subblock[1:]
					listofcharacters.append(["ENDCHOICE", ""]) #we'll need this if we stuff multple fields into one []
					continue
				elif subblock[0] == "[":
					subblock = subblock[1:] #get rid of "["
					textmatch = find_matches(universe, subblock)	
					subblock = subblock.replace(textmatch,"",1)
					subblock = subblock[1:] #get rid of "]"
					if len(textmatch) > 0: listofcharacters.append(["CHOICEFIELD", textmatch]) #don't append empty fields! Which will probably happen, ex: in the digraph field 
					continue		
				elif re.match("<REFERENCESELF>",subblock):
					subblock = subblock.replace(re.match("<REFERENCESELF>",subblock).group(),"",1) #get rid of the tag
					listofcharacters.append(["REFERENCESELF"])
					continue
				match = re.match("<REPEATEXACTLY>", subblock)
				if match:
					subblock = subblock.replace(match.group(),"",1)
					match = re.match("[0-9]*", subblock)
					subblock = subblock.replace(match.group(),"",1)
					listofcharacters.append(["REPEATEXACTLY",match.group()])	
					continue	
				match = re.match("<REPEATMORE>", subblock)	
				if match:
					subblock = subblock.replace(match.group(),"",1)
					match = re.match("[0-9]*", subblock)
					subblock = subblock.replace(match.group(),"",1)
					listofcharacters.append(["REPEATMORE",match.group()])	
					continue
				match = re.match("<REPEATLESS>", subblock)	
				if match:
					subblock = subblock.replace(match.group(),"",1)
					match = re.match("[0-9]*", subblock)
					subblock = subblock.replace(match.group(),"",1)
					listofcharacters.append(["REPEATLESS",match.group()])
					continue
				match = re.match("<REFERENCE>", subblock)			
				if match:
					subblock = subblock.replace(match.group(),"",1)
					match = re.match("[0-9]*", subblock)
					subblock = subblock.replace(match.group(),"",1)
					listofcharacters.append(["REFERENCE", match.group()])
					continue
		
				statusqueue.append([3, "Issue writing a square bracket, non-matching character encountered\n", "warning"])	
				print(subblock)
				printstatusqueue(statusqueue)
				break		
		else:
			statusqueue.append([3, "Issue writing general characters, non-matching character encountered\n", "warning"])	
			print("mainloop "+ str(block))
			printstatusqueue(statusqueue)		
			break
	#end whilemainloop

	listofinstructions = []
	sublist = []
	mode = None	
	
	while len(listofcharacters)>0:
		if listofcharacters[0][0] == "CHOICE":
			sublist.append(listofcharacters[0]) #We populate the sublist in order to embed our choices & choicefields in an array
			listofcharacters = listofcharacters[1:] 
			if len(listofcharacters) == 0:
				listofinstructions.append(sublist)
				sublist = []
		elif listofcharacters[0][0] == "CHOICEFIELD":
			sublist.append(listofcharacters[0])
			listofcharacters = listofcharacters[1:]
			if len(listofcharacters) == 0:
				listofinstructions.append(sublist)
				sublist = []
		elif listofcharacters[0][0] == "ENDCHOICE":
			listofinstructions.append(sublist)
			sublist = []		
			listofcharacters = listofcharacters[1:] 	
		elif listofcharacters[0][0] == "REFERENCESELF":
			number = 1
			skip = 1
			if listofcharacters[1][0] == "REPEATEXACTLY":
				number = int(listofcharacters[0][1])
				skip =2
			elif listofcharacters[1][0] == "REPEATMORE":
				number = random.randint(int(listofcharacters[1][1]), int(listofcharacters[1][1])*2 + 2)
				skip = 2
			elif listofcharacters[1][0] == "REPEATLESS":
				number = random.randint(1, int(listofcharacters[1][1]))
				skip = 2
			sublist.insert(0,["REPEAT", number]) #insert!! At the beginning! And we've already chosen a number, so we can drop the more/less/exactly
			listofinstructions.append(sublist) #now we have an array of choice and choice fields
			sublist = []
			listofcharacters = listofcharacters[skip:] #we are skipping possibly both reference self and repeat
		elif 	listofcharacters[0][0] == "REFERENCE":
			number = 1
			skip = 1
			if listofcharacters[1][0] == "REPEATEXACTLY":
				number = int(listofcharacters[0][1])
				skip = 2
			elif listofcharacters[1][0] == "REPEATMORE":
				number = random.randint(int(listofcharacters[1][1]), int(listofcharacters[1][1])*2 + 2)
				skip = 2
			elif listofcharacters[1][0] == "REPEATLESS":
				number = random.randint(1, int(listofcharacters[1][1]))
				skip = 2
			sublist.insert(0,["REFERENCE",listofcharacters[0][1]])
			sublist.insert(0,["REPEAT", number]) #insert!! At the beginning! And we've already chosen a number, so we can drop the more/less/exactly
			listofinstructions.append(sublist) #now we have an array of choice and choice fields
			sublist = []
			listofcharacters = listofcharacters[skip:] #we are skipping possibly both "reference" and "repeat"
		elif listofcharacters[0][0] == "REPEATEXACTLY" or 	listofcharacters[0][0] == "REPEATMORE" or  listofcharacters[0][0] == "REPEATLESS":
			number = 1
			if listofcharacters[0][0] == "REPEATEXACTLY":
				number = int(listofcharacters[0][1])
			elif listofcharacters[0][0] == "REPEATMORE":
				number = random.randint(int(listofcharacters[0][1]), int(listofcharacters[0][1])*2 + 2)
			elif listofcharacters[0][0] == "REPEATLESS":
				number = random.randint(1, int(listofcharacters[0][1]))
			for it in range(number):
				listofinstructions.append(sublist) # just append the sublist a repeated number of times!
			sublist = []
			listofcharacters = listofcharacters[1:] #we are only skipping "repeat"
		elif listofcharacters[0][0] == "MANDATORY":
			if len(sublist) > 0: #accounting for the case where there is no repeats
				listofinstructions.append(sublist)
				sublist = []
			listofinstructions.append(listofcharacters[0])
			listofcharacters = listofcharacters[1:]
		else:
			statusqueue.append([3, "Issue writing a square bracket, infinite loop was interupted in parser", "warning"])	
			print(listofcharacters)
			printstatusqueue(statusqueue)			
			break
	#end while
	if len(sublist)>0: listofinstructions.append(sublist) #just to wrap up any non-integrated fields left over

	#at this point, we should have something like [[MANDATORY, m], [[REPEAT,1], [CHOICE,sh],[CHOICE,ch]], [[REFERENCE,1],[REPEAT,3]],[[REPEAT,2],[CHOICE, ch], [CHOICE, sh], [CHOICEFIELD, aeiou]]]	
	result = ""
	while len(listofinstructions)>0:
		if listofinstructions[0][0]=='MANDATORY':
			result += listofinstructions[0][1]
			listofinstructions = listofinstructions[1:]
		else:
			if listofinstructions[0][0][0] == "REFERENCE":
				number = listofinstructions[0][1][1] #digging into the "repeat" block that mandatorily comes next
				reference = listofinstructions[0][0][1]
				for it in range(number):
					result += referenceswrite[reference] #I am going to need so many error codes and checks to implement this fully correctly
				listofinstructions = listofinstructions[1:]	
				continue
			
			if listofinstructions[0][0][0] == "REPEAT": 
				number = listofinstructions[0][0][1]
				listofinstructions[0] = listofinstructions[0][1:]
			else: 
				number = 1
			
			temp = random.choice(listofinstructions[0])
			listofinstructions = listofinstructions[1:]
			tempresult = ""	
			if temp[0] == "CHOICE":
				tempresult += temp[1]
			elif temp[0] == "CHOICEFIELD":
				tempresult += random.choice(temp[1])
			else:
				print(temp)
				print(listofinstructions)
				statusqueue.append([3, "Issue writing a square bracket, infinite loop was interupted in writer\n", "warning"])	
				printstatusqueue(statusqueue)
				break
			for it in range(number):
				result += tempresult
			referenceswrite.append(result) #only append the result if it came from a choice block
			
	#end while			
	return result		
#end def write_characters 	

def square_bracket_interpreter(block): #And this will be called whenever we have square brackets
	output = ""
	count = 0
	block = block.strip("[]")
	while len(block) > 0:	
		match = re.match("Cc", block) 
		if match:
			output += "("+ consonantlist+r")<REFERENCESELF><REPEATEXACTLY>1" #I am putting these all in brackets so that they will be compatible with the "\1" backreference
																#known limitation with the backreference: if there is more than one field in the same square bracket, the regex produced will have multiple capture groups. 
																#I may be getting rid of "/1" anyways?
			block = block.replace(match.group(),'',1)					
			continue
		match = re.match("Ch", block) 
		if match:
			output += "("+cdigraphs+")"
			block = block.replace(match.group(),'',1)					
			continue	
		match = re.match("Cm", block) 
		if match:
			output += "("+complexs+")"
			block = block.replace(match.group(),'',1)	
			continue	
		match = re.match("Cn", block) 
		if match:
			output += "("+nonsonorant+")"
			block = block.replace(match.group(),'',1)	
			continue		
		match = re.match("Vh", block) 
		if match:
			output += "("+vdigraphs+")"
			block = block.replace(match.group(),'',1)					
			continue		
		match = re.match("Vv", block) 
		if match:
			output += "("+vowellist+r")<REFERENCESELF><REPEATEXACTLY>1"
			block = block.replace(match.group(),'',1)	
			continue	
		match = re.match("x", block) 
		if match:		
			block = block.replace(match.group(),'',1)	
			if block[0:1] == "=":
				output += "<REPEATEXACTLY>"
			if block[0:1] == "<":
				output += "<REPEATLESS>" 
			if block[0:1] == ">":
				output += "<REPEATMORE>"
			output +=  re.match("[0-9]*",block[1:]).group() 	
			block= block.replace(block[0:2],'',1)			
			continue	
		match = re.match(r"s(?=x[\<\>\=][0-9])", block) #this actually only matches the s: the rest is a lookahead 
		if match:
			block = block.replace(match.group(),'',1)	
			output += "<REFERENCESELF>"		
			continue		
		match = re.match("C", block) 
		if match:
			output += "("+consonantlist+")"
			block = block.replace(match.group(),'',1)
			continue
		match = re.match("V", block) 
		if match:
			output += "("+vowellist+")"
			block = block.replace(match.group(),'',1)	
			continue
		match = re.match("X", block) 
		if match:
			output += "("+universe+")"
			block = block.replace(match.group(),'',1)	
			continue	
		match = re.match("Y", block) 
		if match:
			output += "("+svowels+")"
			block = block.replace(match.group(),'',1)	
			continue	
		match = re.match("N", block) 
		if match:
			output += "("+sonors+")"
			block = block.replace(match.group(),'',1)	
			continue						
		match = re.match("Ua", block) 
		if match:
			output += "("+user1+")"
			block = block.replace(match.group(),'',1)	
			continue	
		match = re.match("Ub", block) 
		if match:
			output += "("+user2+")"
			block = block.replace(match.group(),'',1)	
			continue	
		match = re.match("Uc", block) 
		if match:
			output += "("+user3+")"
			block = block.replace(match.group(),'',1)	
			continue						
		count += 1
		if count > 1000000: 
			statusqueue.append([3, "Issue interpreting a square bracket, infinite loop was interupted \n","warning"])	
			break		
	#end while
	return output				
#end square_bracket_interpreter




def encipher_on_button(event):
	#this is where the all the computation starts
	global statusqueue
	statusqueue = []
	updatefields()

	output.delete("1.0", tk.END)
	ruleslist = get_rules()
	printstatusqueue(statusqueue)

	ptext = plaininput.get("1.0", tk.END).strip("\n")
	plaintext = ptext #we need to separate these out for diacritic reasons

	if diacritics.get() >= 2: # strip all diacritics before translating
		plaintext = unicodedata.normalize("NFD", ptext).encode('ascii', 'ignore').decode("utf-8")
	intermediatetext = ""
	changed = [False] * len(plaintext) #gotta remember to account for dropped characters too,	

	capital = []
	for character in plaintext:
		capital.append(character.isupper())



	for rulesset in ruleslist: # for each stage of coding
		i = 0	
		count = 0
		while i < len(plaintext):
			count += 1
			if count > 1000000: 
				statusqueue.append([3, "Infinite loop in encipher_on_button mainloop, somehow\n","warning"])	
				break	
			for entry in rulesset: #for each rule within the rulelist at this stage
				length = entry[2]
				match = None
				positioning = re.search("<POSITION[1-4]>",entry[0])
				stripped = entry[0] 
				referencesread = [] #this will be used in match_next to keep track of what we've read so far. Used when matching the *same* match, like [c]i[1] matching pip
				referentgroups = [] #this will be used in match_next to keep track of the field we've using to match; useful when making a match several times, but not copying it. [c]i[c] matching sip
				#Do I need this? Or do I just need to store the most recent one? 
				global referenceswrite 
				referenceswrite = [] #this will keep track of what we've written so far


				if positioning: 
					stripped = stripped.replace(positioning.group(), "", 1)
					positioning = re.search("[1-4]",positioning.group()).group() #I think that's the right index to snipe the number			


				if positioning == "1" or (positioning == "4" and not i ==0):
					if not re.match(r"\s",plaintext[i-1:]):
						continue #continue means "go to the next entry in the while loop" in this context. 
				if (positioning == "3" or positioning == "2") and not i ==0:
					if not re.match(universe, plaintext[i-1:i]):
						continue
									

				#regex doesn't work here because we cannot predict in advance what reference groups will be numbered
				#actually, there might be a way, and it involves counting the subgroups in each sidebar. 
				#but when implementing future features, I will run into other regex troubles. May as well write it now 
				
				
				#Where I left off: need to fix the repeats, bearing in mind that they have already matched one thing, and to fix repeatless, which needs to fail on larger clusters. 
				#right now I need a[Vx<3]o to match aaooo and aaoo correctly; not to match the first and to match the latter. 

				def match_squares(i, tomatch, plaintext, restofmatch, referentgroups = None,mode=None, first = False): #should return: the new i, (the match can be inferred from the difference!)]\
					if not referentgroups: referentgroups = []				
					if len(tomatch) == 0: return match_next(i, restofmatch, plaintext, False) 
					elif i is False: return False #pass any false's up the chain of recursion. Also, "is" is needed here because 0 == False, but 0 is not False. 
					elif tomatch[0] == "(":
						amatch = re.match(r"\((\([^)]+\)\|?)*\[?[^\]]*\]?\)", tomatch)
						referentgroups.append(amatch.group())
						bmatch = re.match("(?i)"+amatch.group(), plaintext[i:])
						if bmatch:
							i += len(bmatch.group())
							referencesread.append(bmatch.group())
							tomatch = tomatch.replace(amatch.group(), "", 1)
							return match_squares(i, tomatch, plaintext, restofmatch, referentgroups, mode, first) # don't modify first because it's not the first in this sequence
						else: return False # if there's no match, this entry doesn't work at this position						
					elif re.match("<REFERENCESELF>",tomatch):
						tomatch = tomatch.replace("<REFERENCESELF>", "", 1)
						return match_squares(i, tomatch, plaintext,restofmatch, referentgroups, "REFERENCESELF", first=first)
					elif re.match("<REFERENCE>",tomatch):
						mode = re.match("[0-9]*",tomatch).group()
						tomatch = tomatch.replace("<REFERENCE>", "", 1)
						tomatch = tomatch.replace(re.match("[0-9]*",tomatch).group(), "", 1)
						return match_squares(i, tomatch, plaintext,restofmatch, referentgroups, mode)
					elif re.match("<REPEAT", tomatch): #remember, by the time you get here, you've already matched the field once
						if first and i >= 2 and not mode == "REFERENCESELF" and re.match("(?i)"+referentgroups[len(referentgroups)-1], plaintext[i-2:]): #check if we would have matched the character before the first one we checked.
							return False  #we failed this check before, so we should fail it a second time.
						elif first and i >= 2 and re.match("(?i)"+referencesread[len(referencesread)-1], plaintext[i-2:]):		
 							return False 
						othertest = tomatch.replace(re.match("<REPEAT[A-Z]*>[0-9]+", tomatch).group(), "", 1)
						if len(othertest) + len(restofmatch) > 0: # if there's something to test for after our current repetition, either inside the square block or outside
							failforlength = False
						else:
							failforlength = True #set a variable to let us know to fail repeat actions if there's too many matches.	
											
	
						if re.match("<REPEATEXACTLY>",tomatch): #remember, by the time you get here, you've already matched the field once
							tomatch = tomatch.replace("<REPEATEXACTLY>", "",1)
							number = re.match("[0-9]*",tomatch).group()
							tomatch = tomatch.replace(number, "", 1)
							number = int(number) 
							if mode == "REFERENCESELF":
								mode = len(referencesread)-1
								number -= 1 #because we've already matched once.
							if mode == None: 
								number -= 1 #because we've already matched once.
								tocheck = "(?i)"+referentgroups[len(referentgroups)-1]
								for it in range(number):
									match = re.match(tocheck, plaintext[i:])
									if match:
										referencesread[len(referencesread)-1] = referencesread[len(referencesread)-1] + match.group() # if we have [Cx=2], and it matches "Sh", then we want to match "sh" when referenced
										i += len(match.group())		
									else: return False	
								if failforlength and re.match("(?i)"+referentgroups[len(referentgroups)-1], plaintext[i:]):
									return False #we want clusters of ONLY this size. If we can go one or more larger, and there's nothing after to match, then we need to fail
								else:		
									return match_squares(i, tomatch,plaintext,restofmatch, referentgroups)	
							else: #mode must be a #
								for it in range(number):
									match = re.match("(?i)"+referencesread[mode],plaintext[i:])
									if match:
										i += len(match.group())	
									else: return False	
								if failforlength and re.match("(?i)"+referencesread[mode],plaintext[i:]):
									return False #we want clusters of ONLY this size. If we can go one or more larger, and there's nothing after to match, then we need to fail
								else:		
									return match_squares(i, tomatch,plaintext,restofmatch, referentgroups)			
						elif re.match("<REPEATLESS>",tomatch):	#remember, by the time you get here, you've already matched the field once
							tomatch = tomatch.replace("<REPEATLESS>", "",1)
							number = re.match("[0-9]*",tomatch).group()
							tomatch = tomatch.replace(number, "", 1)		
							number = int(number)
							if number < 1: return i #since we've already matched once before we reached here!
							if mode == "REFERENCESELF":
								mode = len(referencesread)-1
								number -= 1 #because we've already matched once.
							if mode == None:
								number -= 1
								greedy = 0
								matchpoint = [i]
								morei = i
								while re.match("(?i)"+referentgroups[len(referentgroups)-1], plaintext[morei:]):
									morei += len(re.match("(?i)"+referentgroups[len(referentgroups)-1], plaintext[morei:]).group())
									greedy += 1
									matchpoint.append(morei)
								if greedy >= number and failforlength: return False #if we need to match something afterwards, then we can accept too-long matches
								if greedy < number: number = greedy + 1 # because number starts from 1 meaning 2 repeats, but greedy starts from 0 meaning 1 repeat. 
								for it in reversed(range(number)): #working backwards from the maximum number, see if anything 
									morei = match_squares(matchpoint[it], tomatch, plaintext,restofmatch, referentgroups)
									if morei is not False: return morei  #don't just return match_squares because we need to try again if it fails
								else: return i #since we've already matched once before we reached here!
							else: #mode must be a number
								greedy = 0
								matchpoint = [i]
								morei = i
								while re.match("(?i)"+referencesread[mode],plaintext[morei:]):
									morei += len(re.match("(?i)"+referencesread[mode],plaintext[morei:]).group())
									greedy += 1
									matchpoint.append(morei)																
								if greedy >= number and failforlength: return False
								if greedy < number: number = greedy + 1
								for it in reversed(range(number)): #working backwards from the maximum number, see if anything 	
									morei = match_squares(matchpoint[it], tomatch, plaintext,restofmatch, referentgroups)
									if morei is not False: return morei  #otherwise we need to enter the for loop again
								else: return i #already matched once
								mode = None	 
						elif re.match("<REPEATMORE>",tomatch):	#remember, by the time you get here, you've already matched the field once
							tomatch = tomatch.replace("<REPEATMORE>", "",1)
							number = re.match("[0-9]*",tomatch).group()
							tomatch = tomatch.replace(number, "", 1)	
							number = int(number)
							if mode == "REFERENCESELF":
								mode = len(referencesread)-1
							if mode == None:
								greedy = 0
								matchpoint = [i]
								morei = i
								#the usecase for refereant groups has changed, it might no longer be necessary
								match = re.match("(?i)"+referentgroups[len(referentgroups)-1], plaintext[morei:])
								while match: #tracking down how many matches we can make
									morei += len(match.group())
									greedy += 1
									matchpoint.append(morei)
									match = re.match("(?i)"+referentgroups[len(referentgroups)-1], plaintext[morei:])
								if number > greedy: return False #we haven't got more than the number of repeats we need. 							
								for it in reversed(range(greedy+1)): #working backwards from the maximum number, try to match the rest of the string
									morei = match_squares(matchpoint[it], tomatch, plaintext,restofmatch, referentgroups)
									if morei is not False: return morei  
									if it < number: return False
								else: return False
							else: #mode must be a number
								greedy = 0
								matchpoint = [i]
								morei = i
								while re.match("(?i)"+referencesread[mode],plaintext[morei:]): #find the maximum number of matches
									match = re.match("(?i)"+referencesread[mode],plaintext[morei:])
									morei += len(match.group())
									greedy += 1
									matchpoint.append(morei)																
								if number > greedy: return False
								for it in reversed(range(greedy+1)): #working backwards from the maximum number, see if anything 	
									morei = match_squares(matchpoint[it], tomatch, plaintext,restofmatch, referentgroups)
									if morei is not False: return morei
									if it < number: return False
								else: return False	 
								mode = None	 		
					else: statusqueue.append([3, "Unknown character within match_squares\n","warning"])				
				
				#end def match_squares
			
				def match_next(i, stripped, plaintext, first = True): #it feels bad to nest a function here, but I need recursion
					if len(stripped)==0: return i
					elif re.match("(?i)"+universe, stripped): #if our search tag continues a plain letter
						amatch = re.match("(?i)"+universe, stripped).group() #check to see if the first character is a plaintext character
						bmatch = re.match("(?i)"+amatch, plaintext[i:]) #search for that plain letter in the plaintext
						if bmatch:
							return match_next(i+1, stripped[1:],plaintext,False)
						else: return False			
					elif stripped[0] == "[":
						newthing = square_bracket_interpreter(re.match(r"\[[^\]]*\]", stripped).group())	
						restofmatch = stripped.replace(re.match(r"\[[^\]]*\]", stripped).group(), "",1)	
						newi = match_squares(i,newthing,plaintext, restofmatch, first=first) 
						referencesread.append(plaintext[i:newi]) #what we matched is just something in the orig plaintext, so no need to extract it from the subroutine
						#here should be where I create reference groups. 
						if newi is False: return False
						return newi 
					elif re.match(r"/s",stripped) or stripped[0] == "]": return match_next(i,stripped[1:],plaintext, first) #skip over any whitespace or "]"'s in ruletext
					else: 
						statusqueue.append([3, "Unknown character within rule when matching\n","warning"])	
						printstatusqueue(statusqueue)
						return None
				#end def match_next	

				morei = match_next(i,stripped,plaintext)
				if morei is False: continue
				 
				
				
				if (positioning == "1" or positioning == "3") and not re.match(universe, plaintext[morei:]): #universe doesn't include whitespace; anyways, "beginning" and "medial" need non-whitespace after them
					continue #not actually a match! look at next rule	
				if (positioning == "2" or positioning == "4") and not re.match(r"\s|$", plaintext[morei:]): #"final" and "isolated" need whitespace after them
					continue 
					
				towrite = write_characters(entry[1])				
					
				matchexamine = plaintext[i:morei]
				for character in range(len(matchexamine)):
					if character > len(matchexamine) or character > len(towrite)-1: break #no out of bounds checks, please
					if plaintext[i + character].isupper(): 
						towrite = towrite[:character] + towrite[character].upper() + towrite[character + 1:]
					else:
						towrite = towrite[:character] + towrite[character].lower() + towrite[character + 1:]
						
				if diacritics.get() == 3:
					matchexamine =	ptext[i:morei] #ptext being the unstripped plaintext, which might not match in length anymore 
					number = 0
					for character in range(len(matchexamine)):
						if character > len(matchexamine) or character > len(towrite): break #no out of bounds checks, please
						unichar = unicodedata.normalize("NFD", matchexamine[character]).encode("UTF-8") # this gives us the unicode breakdown of the character examined
						if unichar: #I'm not sure this could ever fail, but just in case
							if	re.search(r"\\xcc[^']*", str(unichar)): #I'm pretty sure \xcc means "the next character is a combining character"		
								towrite = towrite[:character] + unicodedata.normalize("NFC",(towrite[character].encode("UTF-8") + re.search(b"\\xcc[^']*", unichar).group()).decode("UTF-8")) + towrite[character:]					
								#normalize the character in towrite, then add the diacritics, then turn it back into a string

				start = len(changed)-len(plaintext) + i
				insertlength = len(towrite)
				end = len(changed)-len(plaintext) + morei


				changed = changed[:start] + [True] * insertlength + changed[end:] # Mark all we replaced in as changed
				if insertlength > end - start: #if we're writing more characters than we're replacing, we need to insert some falses
					capital = capital[:end] + [False] * (insertlength - (end - start)) + capital[end:] #keep track of capitals, any extra letters are lowercase by default 
				if insertlength < end-start:  #if we're writing *less* characters than we're replacing, we need to delete some entries
					capital = capital[:start+insertlength] + capital[end:]
				#if there match & replace are the same size, we're all good	
					 	
				i = morei
				intermediatetext += towrite 
				break #out of the for loop, since we've already matched a rule

			else: #else in this sense means "the for loop completed without meeting a break". Which means none of our rules matched the text	
				intermediatetext += plaintext[i:i+1] #mark it and pass the character through. We mark the unchanged because they will always be single characters
				i += 1	

			#end inner for

		#end while

		plaintext = intermediatetext.lower()
		intermediatetext = ""
		ptext = plaintext
	
	#end outer for
	
	managecapitals = ""
	for character in range(len(plaintext)):
		if capital[character]: managecapitals += plaintext[character].upper()
		else: managecapitals += plaintext[character]
	plaintext = managecapitals
	

	if trackchanges.get() == 3:
		output.insert(tk.END, plaintext)
	else:	   
		character = 0
		count = 0
		while character < len(plaintext): 
			if re.match(dropped, plaintext[character]): #delete any "dropped" characters
				character += 1
				continue
			if trackchanges.get() == 1: #if you're using capitals to track changes
				if changed[character]:
					output.insert(tk.END, plaintext[character].upper())
				else:	
					output.insert(tk.END, plaintext[character].lower())
				character += 1
			elif trackchanges.get() == 2: #if you're using capitals to track changes
				if changed[character]:
					output.insert(tk.END, plaintext[character], "alternate")
				else:	
					output.insert(tk.END, plaintext[character])
				character += 1		
			count += 1
			if count > 1000000: 
				statusqueue.append([3, "Infinite loop in trackchanges, somehow\n","warning"])	
				break	
		
	printstatusqueue(statusqueue)	


					

					




translate.bind("<Button-1>", encipher_on_button) 
# this binds the above function to clicking the 1st mouse button (the left click) on the button element named "translate"



def savetofile(event):
	updatefields()
	fn = asksaveasfile(mode='w', defaultextension="cds")
	fn.writelines(["Crytolang Config File","\n",rulesinput.get("1.0",tk.END).strip("\n"),"\n",universe,"\n",consonantlist,"\n",vowellist,"\n",cdigraphs,"\n",vdigraphs,"\n",svowels,"\n",sonors,"\n",nonsonorant,"\n",complexs,"\n",user1,"\n",user2,"\n",user3, "\n", dropped])
	fn.close()

#end def savetofile
 
def loadfromfile(event):
	fn = askopenfilename()
	f= open(fn, "r")
	config = f.read()
	f.close()	
	config = config.split("\n")
	if not config[0] =="Crytolang Config File":
		status.insert("1.0","Invalid configuration file \n")
	else:	
		rulesinput.delete("1.0",tk.END)
		universebox.delete("1.0",tk.END)
		consonants.delete("1.0",tk.END)
		vowels.delete("1.0",tk.END)
		consonantdigraph.delete("1.0",tk.END)
		voweldigraph.delete("1.0",tk.END)
		semivowel.delete("1.0",tk.END)
		sonor.delete("1.0",tk.END)
		nonsonorants.delete("1.0",tk.END)
		complexes.delete("1.0",tk.END)
		u1.delete("1.0",tk.END)
		u2.delete("1.0",tk.END)
		u3.delete("1.0",tk.END)
		rulesinput.insert("1.0",config[1])
		universebox.insert("1.0",config[2])
		consonants.insert("1.0",config[3])
		vowels.insert("1.0",config[4])
		consonantdigraph.insert("1.0",config[5])
		voweldigraph.insert("1.0",config[6])
		semivowel.insert("1.0",config[7])
		sonor.insert("1.0",config[8])
		nonsonorants.insert("1.0",config[9])
		complexes.insert("1.0",config[10])
		u1.insert("1.0",config[11])
		u2.insert("1.0",config[12])
		u3.insert("1.0",config[13])
		drop.insert("1.0",config[14])
	updatefields()	
#end def savetofile

savefile.bind("<Button-1>", savetofile) 
loadfile.bind("<Button-1>", loadfromfile)

def generatewords(event): #amazing how simple this is. I love it
	global statusqueue
	updatefields()
	statusqueue = []
	status.delete("1.0",tk.END)
	rules = get_rules(False)
	output.delete("1.0", tk.END)

	outputstring = ""
	

	
	for repeat in range(100):
		for rule in rules[0]: #only uses the first ruleset
			outputstring += write_characters(rule[1]).lower()												
		outputstring += " "
	output.insert("1.0", outputstring)
	printstatusqueue(statusqueue)
	
#end def



generate.bind("<Button-1>",generatewords)

window.mainloop()

