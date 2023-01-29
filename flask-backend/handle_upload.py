from flask import Blueprint, jsonify, request
from werkzeug.utils import secure_filename
import json

handle_upload = Blueprint('handle_upload',__name__)

@handle_upload.route('/file_upload', methods=["POST"])
def notes():
    # does this have to be define here because of blueprints?

    from db import Note
    from app import db

    # TODO: check the data is in the right format
    # inform the user that this endpoint only takes 
    # make it more generic later on to accept multiple inputs

    if "note" not in request.data.decode(): 
        return jsonify({'error': 'Not not found'}, 400)

    if "note" in request.data.decode():
        print(request.data.decode())

        data = request.data.decode()
        json_data = json.loads(data)
        # TODO: add this data to 

        new_note = Note(
            name = json_data["name"],
            last_modified_date = json_data["last_modified_date"],
            created_date = json_data["created_date"],
            text = json_data["note"]
        )

        db.session.add(new_note)
        db.session.commit()

    return jsonify({'success': 'Note added to database'}), 200


# @handle_upload.route('/file_upload', methods=["POST"])
# def notes():
#     # handle uploaded file here - then display to the frontend
#     # if there is json data, parse that instead. 
    
#     if "note" not in 
#     print(request.data)

#     if 'file' not in request.files:
#         return jsonify({'error': 'No file found'}), 400

#     file = request.files['file']

#     if file.filename == '':
#         return jsonify({'error': 'No file selected'}), 400

#     if file:
#         # use the secure_filename function to secure the filename
#         filename = secure_filename(file.filename)
#         file.save(f'path/to/save/{filename}')
#         return jsonify({'message': 'File uploaded successfully'})

#     return jsonify({'error': 'An error occurred'}), 500

