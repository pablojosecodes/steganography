import sys
import argparse
from src.stegopytooling.stego import stego
import os
import cv2


def encoding(args, StegClass):
    if args.input is None:
        raise Exception("You must specify input for encoding options")
    if args.output is None:
        raise Exception("You must specify output for encoding options")

    if not os.path.exists(args.value):
        raise Exception(args.value + " doesn't exist")


    outputVal = None
    if (args.image):
        outputVal = StegClass.encode_image(cv2.imread(args.value))
        cv2.imwrite(args.output,outputVal)

    elif (args.text):
        txt = ""
        with open(args.value) as f:
            for i in f.readlines():
                txt = txt + i
        print("OUTPUT " + str(txt) + " " + str(args.output))
        outputVal = StegClass.text_hide(txt)
        cv2.imwrite(args.output,outputVal)
    
    if outputVal is None:
        raise Exception("No image or text value specified")
    
    

def main():
    parser = argparse.ArgumentParser(
        prog='Stego CLI',
        description='Stegonagraphy')
    parser.add_argument('-i', '--input',
                        help="Input image path")      # option that takes a value
    parser.add_argument('-o', '--output',
                        help="Output image path",
                        required=False)
    parser.add_argument('-v', '--value',
                        help="Input image path or text file",
                        required=False)
    parser.add_argument('-img', '--image',
        action='store_true')  # on/off flag
    parser.add_argument('-txt', '--text',
        action='store_true')  # on/off flag
    parser.add_argument('-e', '--encode',
        action='store_true')  # on/off flag
    parser.add_argument('-d', '--decode',
        action='store_true')  # on/off flag
    args = parser.parse_args()

    if not os.path.exists(args.input):
        raise Exception(args.input + " doesn't exist")
    
    
    StegClass = stego(cv2.imread(args.input))

    if (args.encode):
        encoding(args, StegClass)

    if (args.decode):
        

        print("DECODE")
        if (args.image):
            if args.output is None:
                raise Exception("You must specify output for image decoding")
            cv2.imwrite(args.output, StegClass.decode_image())
        elif (args.text):
            print("TEXT SEEK")
            print(StegClass.text_seek()[:10])




        
        



    






if __name__ == "__main__":
    main()