#!/usr/bin/env python3
""" Convert the svg file to png. """
from __future__ import print_function

import sys
import os
import re
import argparse

from xml.dom import minidom
from wand.api import library
import wand.color
import wand.image 

def get_dimensions(source_dir, svg_file):
    doc = minidom.parse(os.path.join(source_dir, svg_file))
    svg_width = int(round(float(re.sub("[^0-9.]", "",
                                           [path.getAttribute('width') for path
                                            in doc.getElementsByTagName('svg')][0]))))
    svg_height = int(round(float(re.sub("[^0-9.]", "",
                                            [path.getAttribute('height') for path
                                             in doc.getElementsByTagName('svg')][0]))))    
    doc.unlink()  
    
    width = 150
    height = svg_height * (150/ svg_width) 
    return (150, height, new_filename)
    

def convert_image(src_path, format, width=None, height=None):
    formats = {'png':'png32', 'jpg':'jpeg'}
    if format not in formats.keys():
        return (None, None, None)
        
    real_width = width
    real_height = height
    image_result = None
    
    if not width or not height:
        doc = minidom.parse(src_path)
        svg_width = int(round(float(re.sub("[^0-9.]", "",
                                               [path.getAttribute('width') for path
                                                in doc.getElementsByTagName('svg')][0]))))
        svg_height = int(round(float(re.sub("[^0-9.]", "",
                                                [path.getAttribute('height') for path
                                                 in doc.getElementsByTagName('svg')][0]))))
        doc.unlink()
        if width and not height:
            real_height = int(round((float(width) * float(svg_height)/float(svg_width))))
        elif height and not width:
            real_width = int(round((float(height) * float(svg_width)/float(svg_height))))
        else:
            real_width = svg_width
            real_height = svg_height
    
    with wand.image.Image() as image:
        with wand.color.Color('transparent') as background_color:
            library.MagickSetBackgroundColor(image.wand, background_color.resource)
        image.read(filename=src_path)
        if real_width and real_height:
            image.resize(real_width, real_height)
        image_result = image.make_blob(formats[format])
    
    return image_result
        
def convert_directory(source_dir, target_dir, format='png', width=None, height=None, files=None):
    """ Convert directory of svg files to directory of png files"""

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for svg_file in os.listdir(source_dir):
        image_results = convert_image(os.path.join(source_dir, svg_file), format, width, height)
        
        with open(os.path.join(target_dir, svg_file.replace('.svg', '.'+format)), 'wb') as out:
            print('Creating ./%s/%s (%d x %d)' % \
                   (target_dir, svg_file.replace('.svg', '.' + format), width, height))
            out.write(image_results)

def main(argv=None):
    """ Main program to convert flags from svg to png files """
    parser = argparse.ArgumentParser(description='Convert US flags from svg to png.')
    parser.add_argument('-w', '--width', dest="width", default=0, type=int,
                        help='Width of resulting png file.')
    parser.add_argument('-o', '--height', dest="height", default=0, type=int,
                        help='Height of resulting png file.')
    parser.add_argument('-f', '--format', dest="format", default='png',
                        help='Format of image (png or jpg).')
    parser.add_argument('--list',    dest='dimensions', action='store_true')
    parser.add_argument('--no-list', dest='dimensions', action='store_false')
    parser.set_defaults(dimensions=False)
    
    args = parser.parse_args(argv)
    
    if args.dimensions:
        for svg_file in os.listdir('./images/us/svg'):
            width, height = get_dimensions('./images/us/svg', svg_file)
            print ("%s: %d, %d, %s" % (svg_file, width, height))

    else:      
        convert_directory('./images/us/svg', './images/us/%s_%s' % (args.format, str(args.width) + '_' + str(args.height)), 
                      args.format, width=args.width, height=args.height)

if __name__ == "__main__":
    sys.exit(main())
