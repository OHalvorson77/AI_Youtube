import os
import requests

PEXELS_API_KEY = "0oPlJCM04RoClLAskxz86JUXBLWxhZ3PoGpYVA505UGqEmuPjtAUeaq1"
PEXELS_API_URL = "https://api.pexels.com/videos/search"


def keyWordVideoGen(keywords):
    video_paths=[]
    for keyword, _ in keywords:
        path = fetch_video_for_keyword(keyword)
        if path:
            video_paths.append(path)
    
    return video_paths

def fetch_video_for_keyword(keyword, output_folder="stock_clips"):
    headers = {
        "Authorization": PEXELS_API_KEY
    }

    params = {
        "query": keyword,
        "per_page": 1
    }

    response = requests.get(PEXELS_API_URL, headers=headers, params=params)
    data = response.json()

    if not data["videos"]:
        print(f"No video found for keyword: {keyword}")
        return None

    video_url = data["videos"][0]["video_files"][0]["link"]
    video_filename = os.path.join(output_folder, f"{keyword}.mp4")

    
    os.makedirs(output_folder, exist_ok=True)
    video_data = requests.get(video_url)
    with open(video_filename, "wb") as f:
        f.write(video_data.content)

    print(f"Downloaded video for '{keyword}' to {video_filename}")
    return video_filename
