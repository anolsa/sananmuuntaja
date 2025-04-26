Many people think that creating spoonerized word pairs in Finnish means swapping either the first letters or the first syllables around. Neither is true, however, and it is in fact the first moras of the words that are swapped. A mora is defined as the first vowel and any preceding consonants, i.e. for the word "sana" the first mora is "sa" and for the word "auto" it's "a".

This is a very simple Python function that takes two strings as input and swaps their first moras around, creating a spoonerized word pair that is output as a tuple. Designed for and commented in Finnish.

Example input "pallo", "keppi" outputs ("kello", "pappi").

Ignores vowel harmony, but takes mora vowel length into account.

mätä - muna -> mutä - mäna
