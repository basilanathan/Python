import re
def get_matching_words(regex):
 words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
 matches = []
 for word in words:
 	if re.search(regex,word):
 		matches.append(word)
 print matches
 return matches

get_matching_words("v")
get_matching_words("ss")
get_matching_words("e$")
get_matching_words("b.b")
get_matching_words("b.+b")
get_matching_words("b.*b")
get_matching_words("a.*e.*i.*o.*u")
get_matching_words("[regular expression]")
# get_matching_words("")
