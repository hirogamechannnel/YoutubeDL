'''import文
Youtube_dl:Youtubeのダウンロードができるようになる
argparse:コマンドラインからの引数を取得できる
'''
import yt_dlp
import argparse
import sys


def main():
    
    #エンコーディング設定
    sys.stdout.reconfigure(encoding='utf-8')

    #引数の定義
    parser = argparse.ArgumentParser(description='Youtube Video Downloader')

    '''
    各引数の説明
    URL:YoutubeのURLを指定
    Format:MP3かMP4を指定
    Output_Folder:出力先のフォルダ
    Output_FileName:出力先のファイル名
    '''

    parser.add_argument('URL',type=str)
    parser.add_argument('Format',type=str,choices=['MP3','MP4'])
    parser.add_argument('Output_Folder',type = str)
    parser.add_argument('Output_FileName',type = str)

    args = parser.parse_args()


    #Youtube_dlの設定
    ydl_Dic = {
        'outtmpl': f"{args.Output_Folder}/{args.Output_FileName}.%(ext)s",
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' if args.Format == 'MP4' else 'bestaudio[ext=mp3]',
    }
    
    with yt_dlp.YoutubeDL(ydl_Dic) as YDL:
        YDL.download([args.URL])

if __name__ == '__main__':
    main()