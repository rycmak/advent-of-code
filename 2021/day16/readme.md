I made a (wrong) assumption in Python about how a hex string is converted to a decimal integer
and then converted to binary with `bin(int(hex_string), base=16))`, which screwed up 
the answer I was getting and puzzled me for a bit because my algorithm logic 
was otherwise correct (worked on all the examples).

I had assumed that `bin()` would return 4 bits for each character in the hex string 
representation: e.g., `bin(int('2AB07', base=16))[2:]` would return `00101010101100000111`;
however, for the first char in the hex string, it actually only returns the most significant bits, 
in this case `101010101100000111`.  So I needed to pad the beginning of the
binary with enough 0's to ensure the length of the resulting binary is exactly 
4x the length of the hex representation.