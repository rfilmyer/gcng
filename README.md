gcng
====

The Gated Community Name Generator.

Quite simple at this stage. (Because it's the first thing I've ever done)
Reads names from `names.json` and generates a gated community name.
Just run `gcng` in python and it spits out a name.

###Recent changes:
* Use a json file (`names.json`) instead of text files.
* Now a module! (To make some changes I'm about to do easier)
* Function name is PEP 8-friendly!

###Stuff I want to add:
* Gated community names right now are quite simple and mainly Florida based.
* Maybe later, I'll offer a "Southwest" option.
* I also want to make this into a website. Likely using Django, but 
   maybe just Javascript is an option. Stay tuned.

###JSON Specs
`gcng` now uses a JSON file to read its list of names.
This file must be named `names.json` and must be in the same directory
as `gcng`.
The JSON file must contain at least two elements: a `names` array, and
at least one array of possible gated community name parts. `names` is an
array containing the names of all of the name part arrays.

Example: {"names": ["first", "second"], "first": ["Bonita", "Palmetto"],
  "second": ["Springs", "Shores"]}

A gated community name can be of arbitrary length, eg "The | Palms | at | Snowbird | Springs"
