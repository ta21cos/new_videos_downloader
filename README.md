# new_videos_downloader
その日更新された動画を一通りiPhoneに入れる

## Prerequisites
* `youtube-dl`
  * https://rg3.github.io/youtube-dl/download.html
  * `brew install youtube-dl`で取得可能
* Python 3.4以上？
* google-api-python-client
  * https://github.com/google/google-api-python-client
  * pipでインストール可能
* python-dotenv
  * https://github.com/theskumar/python-dotenv
  * pipでインストール可能


## How to use

* .env.sampleをコピーして.envファイルを作成
* API_KEYとDIST_DIRを入力する
  * API_KEYはGoogleのサイトから取得
  * DIST_DIRは"/Users/ユーザ名/Music/iTunes/iTunes Media/Automatically Add to iTunes.localized"のような形式になるはず
* `main.py`の中のchannelsに取得したいチャンネルIDを書き込む
  * チャンネルIDはチャンネルTOPのURLのうち`UC...`で始まる部分
  * 例: `https://www.youtube.com/channel/UCg4HES65j_MN2TVeovGFxxx`なら`UCg4HES65j_MN2TVeovGFxxx`
* `main.py`の中の`q`に動画名で絞りたいキーワードがある場合は入力
* 下のコマンドを実行
  * 実行した場所に動画がダウンロードされ，iTunesに追加するようのフォルダに移される

```
python ./..../main.py
```
