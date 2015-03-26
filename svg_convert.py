#!/usr/bin/env python3
""" Convert the svg file to png. """
from __future__ import print_function

import sys
import os
import re

from xml.dom import minidom
from wand.api import library
import wand.color
import wand.image

DEBUG = False

MAX_DIMENSION = 5000
IMAGE_FORMATS = {'png':'png32', 'jpg':'jpeg'}

def get_dimensions(source_dir, svg_file, force_width=150):
    """ Get the dimensions from the svg file and return scaled
    values (for ratio) given the width """

    try:
        doc = minidom.parse(os.path.join(source_dir, svg_file))
    except FileNotFoundError:
        return (None, None)

    svg_width = int(round(float(re.sub("[^0-9.]", "",
                                       [path.getAttribute('width') for path in
                                        doc.getElementsByTagName('svg')][0]))))
    svg_height = int(round(float(re.sub("[^0-9.]", "",
                                        [path.getAttribute('height') for path in
                                         doc.getElementsByTagName('svg')][0]))))
    doc.unlink()

    if DEBUG:
        print(source_dir, svg_file, svg_width, svg_height)

    return (force_width, round(float(svg_height) * (force_width/ svg_width)))


def convert_image(source_dir, svg_file, img_format, width=None, height=None):
    """ Convert the svg to png or jpg and scale as directed """
    if DEBUG:
        print(source_dir, svg_file, img_format, str(width), str(height))

    if img_format not in IMAGE_FORMATS.keys():
        return None

    if (width and width > MAX_DIMENSION) or (height and height > MAX_DIMENSION):
        return None

    real_width = width
    real_height = height
    image_result = None

    if not width or not height:
        try:
            doc = minidom.parse(os.path.join(source_dir, svg_file))
        except FileNotFoundError:
            return None

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

    try:
        with wand.image.Image() as image:
            with wand.color.Color('transparent') as background_color:
                library.MagickSetBackgroundColor(image.wand, background_color.resource)
            image.read(filename=os.path.join(source_dir, svg_file))
            if real_width and real_height:
                image.resize(real_width, real_height)
            image_result = image.make_blob(IMAGE_FORMATS[img_format])
    except wand.exceptions.BlobError:
        return None

    return image_result

def _create_icon():
    """ create a single icon for the favicon """
    image_results = convert_image('./images/us/svg', 'flag_150_79_USA.svg', 'png', 260, 260)
    with open('my_icon.png', 'wb') as out:
        out.write(image_results)

def _convert_directory(source_dir, target_dir, img_format='png', width=0, height=0):
    """ Convert directory of svg files to directory of png files"""

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for svg_file in os.listdir(source_dir):
        image_results = convert_image(source_dir, svg_file, img_format, width, height)

        with open(os.path.join(target_dir, svg_file.replace('.svg', '.'+ img_format)), 'wb') as out:
            print('Creating ./%s/%s (%d x %d)' % \
                   (target_dir, svg_file.replace('.svg', '.' + img_format), width, height))
            out.write(image_results)

def main():
    """ Simple driver main (not used) """
    #_create_icon()
    _convert_directory('./images/us/svg', './images/us/png_150_0', 'png', width=150, height=0)

if __name__ == "__main__":
    sys.exit(main())
