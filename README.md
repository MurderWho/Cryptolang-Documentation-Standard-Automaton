This project is a quick python GUI implementing the Cryptolang Documentation Standard created by DaCracyWorldBuilder, reddit account at: https://www.reddit.com/user/DaCrazyWorldbuilder
See the help file for links to the original reddit posts describing the CDS, and more details about the implementation

The original form of the project was almost solely a series of a RegEx matches, but now it's a more complex mess, much of which simply reimplements elements of RegEx. 

At current moment, the project is badly in need of some re-factoring, but I want to iron out all of the obvious bugs first. Then re-factoring, and then implemention of additional features. 

I have included a .rar file int he files here, which has a windows executable, (created automatically by pyinstaller), that is able to run the program if you do not have python installed on your device. 

FAQ
Q: What does this do that Regex doesn't?
A: I don't believe it does. Actually, I suspect that if I was more comfortable with regex, then I could significantly simplify and shorten this application. 
If you are already experienced with RegEx, then it should be fairly straightfoward for you to make a number of RegEx replacement strings to implement any particular cryptolang ruleset. 

Q: What is the point of this project? 
A: A lot of people who dabble in Cryptolangs are not programmers and not programming-inclined, but the CDS is well-designed for them to create compact, well-defined enciphering schemes. 
The CDS Automaton is designed to auotmate the tedious work of actually translating a text for them once they have created rulestrings.

Q: Why don't you follow Python style guidelines?
A: It's on my to-do list. This is actually my first time working in Python at all, so I didn't fully absorb all of the style guidelines' rules and meanings, and I know I need to go back and review at least my use of whitespace. 

Q: How is the CDS Automaton implemented?
A: I approached it like a programming language, so the get_rules subroutine consists of a lexer, a parser, an interpreter, and then additionally a sorter to reorganize the rules so that longer strings get matched first. 

This produces a string of rules that looks like [[["Sh", "y", 2], ["y", "sh", 2"]]]. (Which would be the result of a rulestext "ShY"). The first entry of the array is a string to match to the plaintext, and the second entry is what to replace the match with.

After the get_rules subroutine, a while loop looks at each character of the plaintext in turn, going through every rule that has been created, and two recursive functions that call each other, match_next and match_square, attempt to match every part of the match to the plaintext.
If they succeed, they output the index of the plaintext that is after the entirety of the match. 

The match is then inserted into an intermediate string, with randomization if required as when writing "[C]", which represents "any character in the consonant box", and two trackers are updated: 
The "capitals" tracker tracks where capital letters should be inserted into the result text, and assumes that any new characters added are lowercase.
And the "changed" tracker keeps tracked of which characters have been modified. 

If there is more than one stage of encoding, then the while loop is repeated, this time acting on the intermediate string.

The square brackets interpreter and writer are implemented with another miniature Lexer-Parser-Interpreter programming pattern, and this is because I see a need for that with future features. 

Q: What features do you still want to implement?
A: I still need to implement position rules that apply to entire rulestrings, "13=AEIOU". I want to implement reference groups, so that ex: [1] would reference "the first square bracket group in this string". And I want to implement the moving of characters described, but not given a standard, in the CDS. And I want to implement general lookaheads/lookbehinds

Q: I want to help! Where should I start?
A: Refactoring: clean up all my old comments, and either write new comments where they're needed, or flag places where I should make comments
Functionality: I implemented square bracket interpretation ass-backward with regards to repeats & references, (yes, references aren't implemented yet, but the structure is there for them already). If repeats & references could be moved to the front of a stack, instead of following it, and the logic rewritten to not have to account for having matched once already before reaching the "repeat" ifs, that would be nice 
Aesthetics: I haven't even looked at how to make resizing the window properly happen yet. And I also want the app to open at an appropriate size for the user's monitor/setup
Functionality: It would be nice if the app could open a config file from dragging/dropping on it, running from the command line with the filepath as an option, and by associating the filetype with the app.
Functionality: It would be nice if you could ctrl-z inside the fields
Aesthetics: It would be nice if the buttons pressed down until they completed their task, then popped back up again
Re-factoring: I write in if/elif patterns a lot when case/select would be more suitable. A lot of the code could be rewritten with a single long regex string match using the | function a lot, and then case match.group():/select:
Functionality: Currently the rules sorter assumes every [] is "5 characters long". That is incorrect, and there should be a function that determines the maximum size of the match a [] could make, (or makes a reasonable estimate for "more than" purposes). 
Functionality, future proofing: Currently the rules sorter sorts things which have a position marker as ahead of everything else. This should be changed so that general lookbehinds do not add to the "length" count, and general lookaheads do add to the "length" count. 
Re-factoring/non-important: strip the length entry from the rules array after the rules sorter, and re-write any code that still relies on the length entry to instead rely on the actual length of the match.
Bugfinding :) Infinite loops, and the rulestext/other conditions that lead to them would be particularly useful.
Making mal-formed rules on purpose, and judging whether the error-text in the status bar is helpful in guiding you towards making a proper rulestext/if add'l errors could be thrown that would be helpful.
Unit test: figure out a config file, (or minimal number of config files), that implements as many of the features as possible in the rulestring, and a matching plaintext to try it on, that produces a known and easily examined ciphertext, (such as "XX XXX X XXXXX [...]", where every character is turned into X, or similar line of thinking), to confirm that every feature stills works after each change
Re-factoring: I originally placed all of my helper functions "in-place", under the idea that they would be short and sweet, and that this would be an easy introduction to the program flow for people new to programming who wanted to understand it under the surface. Specifically DaCrazyWorldBuilder. However, the project has since gotten away from me. I need to move a lot of loops into functions, and I need to move a lot of function declarations into more suitable places in the code so that program flow is readable now.

Q:I want to help and I know so much more about regex than you do
A:Oh thank god. Is it possible to implement references simply by using regex's existing "\1" syntax, with the way that I have implemented fields and square brackets? Could we changed either/both of those so that we could use that regex functionality? That would get rid of somewhere around 50% of the code if we could. 



