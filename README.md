# Steganography

Steganography is the practice of hiding secret information in a communication channel such that the very existence of information is concealed.

This is a tiny package I coded in a few hours which performs a basic form of steganography predicated on the idea of Least Significant Bit encoding.

## Usage
There are 2 ways to use this tool, although I sincerely doubt there is much practical application of steganography in *most* people's daily lives, outside of a fun party trick.

The methods:
1. I put together a package on PyPi, available here.
2. Clone this repository and use the command line tool. Instructions for the flags and commands will be available at the bottom of this readme

## Least Signifant Bit Encoding

To understand LSB encoding, we first must understand how images on digital screens work. 
- Many images use the standard RGB format, where each representable pixel has three values (Red, Green, Blue). 
- Each of these three values is determined using a number from 0-255 (ie. 8 bits)
- The numbers on the left side ("the more significant bits") have a larger impact on the final colors of the image. (ie. changing an R value from 100 -> 200 would have a much larger impact than changing it from 100 -> 101.

You might see where this is going by now- we can simply exploit this "significant bit" property of images and use those insignifant bits to store an entirely different image, or text, or anything representable in bits.

## Image encoding
For images, we do the following for each pixel.

For every channel, loop through the individual pixels and add their bits replace the "host" image's least significant bits with them. 

## Text encoding
We perform a very similar process for text.

Instead of encoding the pixels, we convert the text to their binary representation (ie. their ASCII value equivalent- in 8 bits) and hide them in the same way as images

## But how do we know the length??
We just encode the length in the first 16 bits for text and the height/width in the first 2 16-bit sections for images!

