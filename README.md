## Project to heuristically fix ebook

### INSTALL NOTES:
#### Requires:
* numpy
* nltk
* progressbar


### Notes:
* Consider using fuzzy logic for the paragraph breaks, with a fuzzy break-level-input
* Will eventually migrating this to a Calibre plugin (Thus keeping external libraries to a minimum)
* For license see LICENSE.md

### TODO:
* Add fuzzy detection of chapters
    * User fuzzy pattern matching like "C{c}apter 1{I}"
* Improve skipping to new time / place

### Fuzzy Paragraphing System
1. First will decide the 'Pulpiness' of the book, that is the number of paragraph breaks
    1. Will do this by Author, Genre, and textual analysis (weighted)
    2. NOTE: Could use input on Author and Genres list. Would like to expand into HIGH MED LOW categories
2. Second will iterate through sentences (Found with Regex)
    1. Using a s_norm t_norm pair will decide if there should be a paragraph break
    2. (cond1 OR cond2 OR .. condN) AND pulpiness
    3. Deffuzification is 0 if < 5; 1 if >= 5
3. Will create an internal text string with all the sentences patched together with line breaks put in.

#### Breaks used:
* Dialogue
* Skipping to a new time (keywords)
* Skipping to a new place (keywords)
* When the story changes speakers (keywords?)
* When the paragraph is dragging on (linear value from 0.0 to 1.0 so a ten-sentence paragraph will be 1.0)
    * This is balanced by the pulpiness value of the book


#### Skipping to a new time
* Later that {morning, afternoon, evening, night, day, week, month}
* The next {morning, afternoon, evening, night, day, week, month}

