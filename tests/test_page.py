#!/usr/bin/env python3
""" Selenium Unit tests for flags page"""

import unittest
import os
import requests
from selenium import webdriver, selenium



SOURCE_DIR = './images'
REGION_DIRS = ['us']
SVG_DIR = 'svg'

DEBUG = False

class TestFlagPageAttributes(unittest.TestCase):
    """ Selenium Unit test for Flags """
    def setUp(self):
        """ set up the driver """
        self.driver = webdriver.Firefox()

    def test_modals(self):
        return
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

    def test_get_artifacts(self):
        """ Get some screen shots (CircleCI only since I don't push yet) """
        if os.environ.get('CIRCLE_ARTIFACTS'):
            print('\nGet some screen shots: ', end='', flush=True)
            window_sizes = [[300, 600], [700, 600], [800, 600], [1000, 1000], [1300, 1300]]
            
            artifacts_dir = os.environ.get('CIRCLE_ARTIFACTS')
            if not os.path.exists(artifacts_dir):
                os.makedirs(artifacts_dir)                
            
            driver = self.driver
            driver.get("http://localhost:8080")
            for w_size in window_sizes:
                driver.set_window_size(w_size[0], w_size[1])
                path = artifacts_dir + '/ff_shot_%d_%d.png' % (w_size[0], w_size[1])
                driver.save_screenshot(path)
                print('.', end="", flush=True)
                if DEBUG:
                    print ('Captured %s' % path)
        else:
            print('\nNo screen shots: ', end='', flush=True)
            
    def test_all_images(self):
        """ Make sure no images are 404 """
        print('\nTest image links: ', end='', flush=True)
        driver = self.driver
        driver.get("http://localhost:8080")
        driver.save_screenshot('flags.png')
        all_images  = driver.find_elements_by_tag_name('img')
        for image in all_images:
            src = image.get_attribute('src')
            alt = image.get_attribute('alt')
            r = requests.get(src)
            assert r.status_code == 200, 'Bad http status (%d) for %s' % (r.status_code, src)
            assert len(alt) > 0, 'Missing or empty alt tag for %s' % (src)
            print('.', end="", flush=True)
            if DEBUG:
                print ('Src=%s' % src)
                
    def test_attributes(self):
        return
        """ unit test of attributes in main page """
        print('Checking main page attributes.')
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
