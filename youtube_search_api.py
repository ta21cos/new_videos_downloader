#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser

from datetime import datetime

import settings

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = settings.API_KEY
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
            developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        # q=options.q,
        part = "id,snippet",
        q = options["q"],
        maxResults = options["max_results"],
        channelId = options["channel_id"],
        publishedAfter = options["published_after"]
        ).execute()

    videos = []

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append({"title": search_result["snippet"]["title"], "videoId": search_result["id"]["videoId"]})

    # for video in videos:
    #     print(video["videoId"], video["title"])

    return videos


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
    q = "スプラトゥーン"

    for name, channelId in channels.items():
        options = {
            "channel_id": channelId,
            "published_after": date,
            "max_results": max_results,
            "q": q
        }
        try:
            youtube_search(options)
        except HttpError as e:
            print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
