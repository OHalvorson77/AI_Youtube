import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.http import MediaFileUpload


SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def upload_video(file_path, title, description, category_id="22", privacy_status="public"):
    
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        "client_secrets.json", SCOPES)
    credentials = flow.run_local_server(port=8080)

    
    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)

    
    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "categoryId": category_id
        },
        "status": {
            "privacyStatus": privacy_status
        }
    }

    
    media = MediaFileUpload(file_path, chunksize=-1, resumable=True, mimetype="video/mp4")
    request = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media
    )

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Uploaded {int(status.progress() * 100)}%")

    print("Upload complete!")
    print("Video ID:", response["id"])


