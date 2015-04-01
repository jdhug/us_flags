#!/usr/bin/env python3
""" Unit tests for flags """

import unittest
import os
from io import BytesIO
from wand.image import Image
from svg_convert import convert_image, get_dimensions

DEBUG = True

SOURCE_DIR = 'images'
REGION_DIRS = ['us']
SVG_DIR = 'svg'
TEST_FORMATS = ['png', 'jpg']

# [fixed_width, fixed_height, fixed_both, same_as_svg]
TEST_DIMENSIONS = [[256, None], [None, 256], [256, 256], [None, None]]


class ConvertTests(unittest.TestCase):
    """ Test unit for svg_convert.py """

    def test_svg_dimensions(self):
        """ Check file name for proper internal width, height ratio """
        if DEBUG:
            print('Run test_svg_dimensions')
        for region in REGION_DIRS:
            src_dir = os.path.join(SOURCE_DIR, region, SVG_DIR)
            for svg_file in os.listdir(src_dir):
                (img_width, img_height) = get_dimensions(src_dir, svg_file)
                file_dimensions = [int(i) for i in svg_file.split('_')[1:3]]

                if DEBUG:
                    print('SvgDimensions: %s/%s (%d,%d)' %
                          (region, svg_file, img_width, img_height))

                self.assertEqual(img_width, file_dimensions[0],
                                 'SvgDimensions: Bad width (%d) for (%s/%s).' %
                                 (img_width, src_dir, svg_file))
                self.assertEqual(img_height, file_dimensions[1],
                                 'SvgDimensions: Bad height (%d) for (%s/%s).' %
                                 (img_height, src_dir, svg_file))

    def test_convert(self):
        """ Check all of the svg files and make sure they will all convert to png and jpg """

        for region in REGION_DIRS:
            src_dir = os.path.join(SOURCE_DIR, region, SVG_DIR)
            for target_format in TEST_FORMATS:
                for dims in TEST_DIMENSIONS:
                    if DEBUG:
                        print('***** Convert: %s (%s,%s)' %
                              (target_format.upper(), str(dims[0]), str(dims[1])))
                    for svg_file in os.listdir(src_dir):
                        contents = convert_image(src_dir, svg_file, target_format,
                                                 width=dims[0], height=dims[1])
                        output = BytesIO()
                        output.write(contents)
                        output.seek(0)
                        with Image(blob=contents) as img:
                            if DEBUG:
                                print('Convert: %s/%s to %s (%s,%s) -> (%d,%d)' %
                                      (region, svg_file, target_format, str(dims[0]), str(dims[1]),
                                       img.width, img.height))
                            if dims[0]:
                                self.assertEqual(img.width, dims[0],
                                                 'Convert: Incorrect width %s, %d, %s.' %
                                                 (target_format, img.width, svg_file))
                            if dims[1]:
                                self.assertEqual(img.height, dims[1],
                                                 'Convert: Incorrect height %s, %d, %s.' %
                                                 (target_format, img.height, svg_file))
                        output.close()


    def test_conditions(self):
        """ Test error conditions in convert_image """
        src_dir = os.path.join(SOURCE_DIR, REGION_DIRS[0], SVG_DIR)

        if DEBUG:
            print('Conditions: Bogus target image format')
        contents = convert_image(src_dir, 'flag_150_100_Arizona.svg',
                                 'bogus', width=256, height=256)
        self.assertIsNone(contents, 'Conditions: Bogus format, results should be None.')

        if DEBUG:
            print('Conditions: Bogus file in convert_image (x2)')
        contents = convert_image(src_dir, 'bad_file_name.svg', 'jpg', width=256, height=256)
        self.assertIsNone(contents, 'Conditions: Bogus filename (1), results should be None.')
        contents = convert_image(src_dir, 'bad_file_name.svg', 'jpg')
        self.assertIsNone(contents, 'Conditions: Bogus filename (2), results should be None.')

        if DEBUG:
            print('Conditions: Dimensions too large in convert_image')
        contents = convert_image(src_dir, 'flag_150_100_Arizona.svg',
                                 'bogus', width=10000, height=10000)
        self.assertIsNone(contents, 'Conditions: Dimensions too large, results should be None.')

        if DEBUG:
            print('Conditions: Bogus file in get_dimensions')
        (img_width, img_height) = get_dimensions(src_dir, 'bad_file_name.svg')
        self.assertIsNone(img_width, 'Conditions: Bogus filename in get_dimensions (w).')
        self.assertIsNone(img_height, 'Conditions: Bogus filename in get_dimensions (h).')


def main():
    """ Unit test driver """
    unittest.main()

if __name__ == '__main__':
    main()
