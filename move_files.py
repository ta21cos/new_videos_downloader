import pathlib
import shutil
import settings

def move_video_to_itunes(path):
    DIST_DIR = settings.DIST_DIR
    _path = pathlib.Path(path)
    video_paths = list(_path.glob("*.mp4"))
    dist_path = pathlib.Path(DIST_DIR)

    for video_path in video_paths:
        shutil.move(str(video_path), str(dist_path))
