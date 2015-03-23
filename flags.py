#!/usr/bin/env python3

from glob import glob
from os import listdir
from bottle import route, run, template, error, static_file, response
from svg_convert import convert_image
from io import BytesIO

ALLOWED = {'png':'image/png', 'jpg':'image/jpg'}

@error(404)
def error404(error):
    return 'Sorry, No flags here.'

@route('/generate/<image_path:path>/<filename>')
def generate_image(image_path, filename):
    # Validate dimensions
    dims = image_path.split('/')
    for i, d in enumerate(dims):
        dims[i] = int(dims[i])
        dims[i] = 0 if (dims[i] > 1000 or dims[i] < 0) else dims[i]
    
    # validate format and file
    format = filename[-3:]
    svg_files = glob('./images/us/svg/flag_*' + filename[:-4] + '.svg')
    if len(svg_files) != 1:
        return None
    if format not in ALLOWED:
        return static_file(svg_files[0], root='./images/us/svg')
 
    contents = convert_image(svg_files[0], format, width=dims[0], height=dims[1])
    output = BytesIO()
    output.write(contents)
    output.seek(0)
    
    response.headers['Content-Type'] = ALLOWED[format]
    response.headers['Content-Disposition'] = 'attachment'  # try to force download
    return output

@route('/static/<filename>', name='static')
def static(filename):
    return static_file(filename, root='./static')
    
@route('/images/<image_path:path>/<filename>')
def send_image(image_path, filename):
    return static_file(filename, root='./images/' + image_path)

@route('/')
def index(): 
    flags=listdir('./images/us/svg')
    flags.sort(key=lambda x: x.split("_", 3)[-1])   # format is flags_xx_xx_name_name_name.svg
    return template('flags', flags=flags)  
  
run(host='0.0.0.0', port=argv[1], debug=True)
