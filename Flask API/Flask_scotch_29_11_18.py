from flask import Flask,request

app=Flask(__name__)

@app.route('/query-example')
def query_example():
    language=request.args.get('language')
    framework=request.args.get('framework')
    website=request.args.get('website')
    return '''<h1>The language value is :{}</h1>
              <h1>The framework value is :{}</h1>
              <h1>The website value is : {}</h1>'''.format(language,framework,website)

@app.route('/form-example')
def form_example():
    return 'Todo..'

@app.route('/json-example')
def json_example():
    return 'Todo..'


if __name__=='__main__':
    app.run(debug=True, port=5000)

