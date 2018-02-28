from get_all_new_videos import download_videos, get_new_video_ids
from move_files import move_video_to_itunes
from datetime import datetime

if __name__ == "__main__":
    channels = {
        "hanjou": "UCRb4IVckX44UIDzyykek_gA",
        "nanato": "UCXqocGp-RQ_sTw8EpPDg10A",
        "motty": "UCPfJisP85wKhzK9Lv3pQLRg",
        "yugo1": "UC8VYesWbdGT6kP4B6vju-rQ",
        "hinekure": "UCg4HES65j_MN2TVeovGF64A",
        "yaritaiji": "UCTrckUWmmrRZcNrfu1mZDOg",
        "kugumu": "UCVDviKFOW9_ukuLzobg_FOA",
        "hashigo": "UCwagRVF16HDNEa6gNLADo5A"
        }
    date = datetime.now().strftime("%Y-%m-%dT00:00:00Z")
    max_results = 25
    q = "スプラトゥーン"

    video_id_all = []

    for name, channelId in channels.items():
        video_ids = get_new_video_ids(channelId, date, max_results, q)
        video_id_all += video_ids

    print(video_id_all)
    download_videos(video_id_all)
    move_video_to_itunes(".")
