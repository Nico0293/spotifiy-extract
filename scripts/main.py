import functions_framework
import requests
from google.cloud import storage


@functions_framework.http
def hello_http(request):
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'token' in request_json:
        token = request_json['token']
    elif request_args and 'token' in request_args:
        token = request_args['token']

    if request_json and 'spotify_id' in request_json:
        spotify_id = request_json['spotify_id']
    elif request_args and 'spotify_id' in request_args:
        spotify_id = request_args['spotify_id']

    client = storage.Client()
    bucket_name = 'testnf_20230901'
    bucket = client.bucket(bucket_name)

    headers = {"Authorization": "Bearer " + token}
    response = requests.get("https://api.spotify.com/v1/artists/" + spotify_id + "/albums", headers=headers).json()

    items = response['items']
    for i in range(len(items)):
        album_id = items[i]['id']
        tracks = requests.get("https://api.spotify.com/v1/albums/" + album_id + "/tracks", headers=headers).json()
        file_name = spotify_id + '_' + album_id + '.txt'
        blob = bucket.blob(file_name)
        blob.upload_from_string(str(tracks))

    return response
