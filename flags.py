#!/usr/bin/env python3
""" flab bottle driver """

from glob import glob
import os
from bottle import route, run, template, error, static_file, response, abort
from svg_convert import convert_image
from io import BytesIO
from sys import argv

# Mime types
SOURCE_DIR = './images'
REGION_DIRS = ['us']
SVG_DIR = 'svg'

ALLOWED = {'png':'image/png', 'jpg':'image/jpg'}
REGIONS = ['us']
DEBUG = False

@error(404)
def error404(http_error):
    """ It is a 404 """
    return 'Sorry, no flag here: ' + str(http_error)

@route('/generate/<image_path:path>/<filename>')
def generate_image(image_path, filename):
    """ return resized image in new format """
    if DEBUG:
        print(image_path, filename)

    (region, width, height) = image_path.split('/')
    root = './images/' + region + '/svg'
    width = int(width)
    height = int(height)

    # Validate dimensions
    if width > 1000:
        width = 1000
        height = None
    elif height > 1000:
        height = 1000
        width = None
    if region not in REGIONS:
        region = REGIONS[0]

    # validate format and file
    img_format = filename[-3:]
    svg_files = glob(root + '/flag_*' + filename[:-4] + '.svg')
    if len(svg_files) != 1:
        abort(404, 'Bad filename.')
    if img_format not in ALLOWED:
        abort(404, 'Bad format.')

    contents = convert_image(root, os.path.basename(svg_files[0]), img_format,
                             width=width, height=height)
    # Something wrong so 404
    if contents is None:
        abort(404, "Error Generating " + os.path.basename(svg_files[0]))

    output = BytesIO()
    output.write(contents)
    output.seek(0)

    response.headers['Content-Type'] = ALLOWED[img_format]
    response.headers['Content-Disposition'] = 'attachment'  # try to force download
    return output

@route('/static/<filename>', name='static')
def static(filename):
    """ return static js and css """
    return static_file(filename, root='./static')

@route('/images/<image_path:path>/<filename>')
def send_image(image_path, filename):
    """ return static images """
    return static_file(filename, root='./images/' + image_path)

@route('/')
def index():
    """ index view """
    region = 'us'
    flags = os.listdir(os.path.join(SOURCE_DIR, region, SVG_DIR))
    flags.sort(key=lambda x: x.split("_", 3)[-1])   # format is flags_xx_xx_name_name_name.svg
    return template('flags', flags=flags, region=region)

PORT = argv[1] if len(argv) >= 2 else '8080'  # Heroku configured for argv[1]
run(host='0.0.0.0', port=PORT, debug=False)
