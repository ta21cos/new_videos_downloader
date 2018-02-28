from youtube_search_api import youtube_search
from move_files import move_video_to_itunes

from googleapiclient.errors import HttpError
from datetime import datetime
import subprocess

def gen_video_url(video_id):
    return "https://www.youtube.com/watch?v=" + video_id

def exec_youtube_dl(url):
    result = subprocess.check_output(["youtube-dl", "-f", "mp4", url])
    print(result)

def get_new_video_ids(channelId, date, max_results, q):
    options = {
        "channel_id": channelId,
        "published_after": date,
        "max_results": max_results,
        "q": q
    }
    try:
        results = youtube_search(options)
        video_ids = [result["videoId"] for result in results]
    except HttpError as e:
        print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
        exit(-1)
    if video_ids is not None:
        return video_ids

def download_videos(video_ids):
    for video_id in video_ids:
        exec_youtube_dl(gen_video_url(video_id))

if __name__ == "__main__":
    channels = {
        "hanjou": "UCRb4IVckX44UIDzyykek_gA",
        "nanato": "UCXqocGp-RQ_sTw8EpPDg10A",
        "motty": "UCPfJisP85wKhzK9Lv3pQLRg",
        "yugo1": "UC8VYesWbdGT6kP4B6vju-rQ",
        "hinekure": "UCg4HES65j_MN2TVeovGF64A",
        "yaritaiji": "UCTrckUWmmrRZcNrfu1mZDOg",
        "kugumu": "UCVDviKFOW9_ukuLzobg_FOA"
        }
    date = datetime.now().strftime("%Y-%m-%dT00:00:00Z")
    max_results = 25
    q = ""
    
    video_id_all = []
    
    for name, channelId in channels.items():
        video_ids = get_new_video_ids(channelId, date, max_results, q)
        video_id_all += video_ids

    print(video_id_all)
    download_videos(video_id_all)
    move_video_to_itunes(".")
