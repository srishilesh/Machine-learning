from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

app=FlaskAPI(__name__)

notes = {
    0 : "Sentiment Analysis"
}

def note_repr(key):
    return{
        'url':request.host_url.rstrip('/')+ url_for('notes_detail',key=key),
        'text': notes[key]
    }

@app.route("/",methods=['GET','POST'])    
def notes_list():
    if request.method == 'POST':
        note=str(request.data.get('text',''))
        idx=max(notes.keys())+1
        notes[idx]=note
        return note_repr(idx), status.HTTP_201_CREATED

    return [note_repr(idx) for idx in sorted(notes.key())]   

@app.route("/<int:key>/", methods=['GET', 'PUT', 'DELETE'])
def notes_detail(key):
    """
    Retrieve, update or delete note instances.
    """
    if request.method == 'PUT':
        note = str(request.data.get('text', ''))
        notes[key] = note
        return note_repr(key)

    elif request.method == 'DELETE':
        notes.pop(key, None)
        return '', status.HTTP_204_NO_CONTENT

    # request.method == 'GET'
    if key not in notes:
        raise exceptions.NotFound()
    return note_repr(key)


if __name__ == "__main__":
    app.run(debug=True)     