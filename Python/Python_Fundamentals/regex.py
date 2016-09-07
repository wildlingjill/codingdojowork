# -*- coding: utf-8 -*-

import re

def get_matching_words(regex):
 words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

 return [word for word in words if re.search(regex, word)]



# All words that contain a v
print get_matching_words("v")


# All words that contain a double-“s”
print get_matching_words("ss")


# All words that end with an “e”
print get_matching_words("e$")


# All words that contain an “b”, any character, then another “b”
print get_matching_words("b.b")


# All words that contain an “b”, at least one character, then another “b”
print get_matching_words("b.+b")


# All words that contain an “b”, any number of characters (including zero), then another “b”
print get_matching_words("b.*b")


# All words that include all five vowels in order
print get_matching_words("a.*e.*i.*o.*u")


# All words that only use the letters in “regular expression” (each letter can appear any number of times)
print get_matching_words("^[regulexpsiona]+$")


# All words that contain a double letter
print get_matching_words("([a-z])\\1")


# matches any numerical values, but not numbers inside words - .group(0) shows what the regex search matches to
# re.search(r"^\d+$", "998").group(0)

# # matches any words that match the search exactly
# re.search(r"^Daniel$|^Jill$", "Jill").group(0)
# re.search(r"^(Daniel|Jill)$", "Jill").group(0)

# # searches for multiple words
# re.search(r"^(Daniel|Jill) (Brain|Robinson)$", "Jill Brain").group(0)


