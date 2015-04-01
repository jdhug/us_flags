#!/usr/bin/env python3
""" Selenium Unit tests for flags page"""

import unittest
import os
from selenium import webdriver


SOURCE_DIR = './images'
REGION_DIRS = ['us']
SVG_DIR = 'svg'

DEBUG = True

class TestFlagPageAttributes(unittest.TestCase):
    """ Selenium Unit test for Flags """
    def setUp(self):
        """ set up the driver """
        self.driver = webdriver.Firefox()

    def test_modals(self):
        """ unit test of attributes in modal dialog  """
        if DEBUG:
            print('**** Checking modal attributes.')
        driver = self.driver
        driver.get("http://localhost:8080")

        # This is an unfortunate hack so the modal does not fade and
        # we don't have to sleep when closing the dialog
        driver.execute_script("document.getElementById('flagModal').className = 'modal'")

        for region in REGION_DIRS:
            flags = os.listdir(os.path.join(SOURCE_DIR, region, SVG_DIR))
            # format is flags_xx_xx_name_name_name.svg
            flags.sort(key=lambda x: x.split("_", 3)[-1])
            # Maybe set the region here someday
            for i, flag_file in enumerate(flags):
                driver.find_element_by_id("f_c" + str(i)).click()
                img_element = driver.find_element_by_id("resize_image")

                img_src = img_element.get_attribute('src')
                img_alt = img_element.get_attribute('alt')

                if DEBUG:
                    print('Checking modal attributes for %s (%d, %s).' % (flag_file, i, img_alt))

                assert flag_file in img_src, "%s not in %s" % (flag_file, img_src)
                assert img_alt.replace(' ', '_') in flag_file, "%s not in %s" % (img_alt, flag_file)
                driver.find_element_by_id("cancel_button").click()

    def test_attributes(self):
        """ unit test of attributes in main page """
        if DEBUG:
            print('**** Checking main page attributes.')
        driver = self.driver
        driver.get("http://localhost:8080")
        # test implicitly confirms that they are sorted correctly
        for region in REGION_DIRS:
            flags = os.listdir(os.path.join(SOURCE_DIR, region, SVG_DIR))
            flags.sort(key=lambda x: x.split("_", 3)[-1])
            # Maybe set the region here someday
            for i, flag_file in enumerate(flags):
                # elements
                img_element = driver.find_element_by_id("f_a" + str(i))
                svg_element = driver.find_element_by_id("f_b" + str(i))
                dl_element = driver.find_element_by_id("f_c" + str(i))

                # attributes
                img_src = img_element.get_attribute('src')
                img_alt = img_element.get_attribute('alt')
                svg_href = svg_element.get_attribute('href')
                dl_dff = dl_element.get_attribute('data-flag-file')
                dl_dfn = dl_element.get_attribute('data-flag-name')

                if DEBUG:
                    print('Checking attributes for %s (%s).' % (flag_file, dl_dfn))

                assert flag_file in img_src, "%s not in %s" % (flag_file, img_src)
                assert flag_file in svg_href, "%s not in %s" % (flag_file, svg_href)
                assert flag_file == dl_dff, "%s != %s"  % (flag_file, dl_dff)
                assert img_src == svg_href, "%s != %s"  % (img_src, svg_href)
                assert img_alt == dl_dfn, "%s != %s"  % (img_alt, dl_dfn)
                assert dl_dfn.replace(' ', '_') in flag_file, "%s not in %s" % (dl_dfn, flag_file)
                assert img_alt.replace(' ', '_') in flag_file, "%s not in %s" % (img_alt, flag_file)

    def tearDown(self):
        """ unit test tear down """
        self.driver.close()

if __name__ == "__main__":
    unittest.main(warnings='ignore')
