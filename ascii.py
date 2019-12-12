from PIL import Image
import argparse
#first of all ,build cmd canshu chuli
parser = argparse.ArgumentParser()
parser.add_argument('file') #input
parser.add_argument('-o','--output') #output
parser.add_argument('--width',type = int,default = 80)
parser.add_argument('--height',type = int,default = 80)
args = parser.parse_args()
IMG = arg.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output
