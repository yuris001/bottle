#!/root/mockup/alert/bin/python

import better_exceptions
from bottle import route,run,template,error,jinja2_template as template,static_file,url

better_exceptions.MAX_LENGTH = None



@route('/static/img/<filename>',name='hage')
def img_dir(filename):
    """ set img dir """
    return static_file(filename,root="./static/img")

@route('/static/js/<filename>')
def js_dir(filename):
    """ set js dir """
    return static_file(filename, root="./static/js")

@route('/')
def index():
    return template('hoge',url=url) # viewsディレクトリ配下にhoge.tpl hoge.htmlがあった場合はhoge.tplが優先される?

@route('/api/<id>')
def api(id):
    return template('hoge',id=id,url=url)

@error(404)
def error404(error):
    return template('404')

run(host='0.0.0.0', port=80, debug=True, reloader=True)
