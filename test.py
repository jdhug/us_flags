#!/usr/bin/env python3
from __future__ import print_function
import unittest
from svg_convert import convert_image, get_dimensions
import shutil
import os

TEST_IMG_DIR = 'tests/images'
SOURCE_DIR = 'images'
COUNTRY_DIRS = ['us']
SVG_DIR = 'svg'

SVG_SOURCES  = 'images/us/svg'

# Here's our "unit".
def IsOdd(n):
    return n % 2 == 1

# Here's our "unit tests".
class ConverterTests(unittest.TestCase):
    def setUp(self):
        if not os.path.exists(TEST_IMG_DIR):
            os.makedirs(TEST_IMG_DIR)
        
    def tearDown(self):
        pass
        #if os.path.exists(TEST_IMG_DIR):
        #    shutil.rmtree(TEST_IMG_DIR)    
        
    def testSvgDimensions(self):
        
        dirs= [x[0] for x in os.walk(SOURCE_DIR)]
        
        for country in COUNTRY_DIRS:
            src_dir = os.path.join(SOURCE_DIR, country, SVG_DIR)
            for svg_file in os.listdir(src_dir):
                (img_width, img_height) = get_dimensions(SVG_SOURCES, svg_file)
                file_dimensions = [int(i) for i in svg_file.split('_')[1:3]]
                self.assertEqual(img_width, file_dimensions[0], 'Image width (%d) not equal to filename width (%s/%s)' % (img_width, src_dir, svg_file))
                self.assertEqual(img_height, file_dimensions[1], 'Image height (%d) not equal to filename height (%s/%s)' % (img_height, src_dir, svg_file))

def main():
    unittest.main()

if __name__ == '__main__':
    main()