gcng
====

The Gated Community Name Generator.

Quite simple at this stage. (Because it's the first thing I've ever done)
My crack at a one-page joke site in the vein of 
[It's This For That](http://itsthisforthat.com/) or [Dogeweather](http://dogeweather.com/).
Reads names from `communities.json` and generates a gated community name.
Just run `gcng` in python and it spits out a name.

###Recent changes:
* Rewrote everything to be a github page.

###Stuff I want to add:
* Gated community names are mainly Florida based. Maybe later, I'll offer a "Southwest" option.

###JSON Specs
`gcng` now uses a JSON file to read its list of names.
This file is named `communities.json` and is in the main directory.
The JSON file must contain at least two elements: a `names` array, and
at least one array of possible gated community name parts. `names` is an
array containing the names of all of the name part arrays.

Example: {"names": ["first", "second"], "first": ["Bonita", "Palmetto"],
  "second": ["Springs", "Shores"]}

A gated community name can be of arbitrary length, eg "The | Palms | at | Snowbird | Springs"
