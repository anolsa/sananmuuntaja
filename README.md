Many people think that creating spoonerized word pairs in Finnish means swapping either the first letters or the first syllables around. Neither is true, however, and it is in fact the first moras of the words that are swapped. A mora is defined as the first vowel and any preceding consonants, i.e. for the word "sana" the first mora is "sa" and for the word "auto" it's "a".

This is a very simple Python function that takes two strings as input and swaps their first moras around, creating a spoonerized word pair that is output as a tuple. Designed for and commented in Finnish.

Example input `"pallo", "keppi"` outputs `("kello", "pappi")`.

Ignores Finnish vowel harmony, because I personally don't consider vowel harmony breaking to be valid in spoonerizing. The length of the mora vowel is taken into account.

`mätä - muna` -> `mutä - mäna`

`rooli - pallo` -> `paali, rollo`

The text file `lopullinen_lista.txt` contains a little over 250 000 pairs of real Finnish words that can be spoonerized into another pair of real words, in the format `"kani - korkea, koni - karkea"`. There shouldn't be any flipped duplicates, in the sense that if `kani - korkea` is there, then `korkea - kani` isn't.
