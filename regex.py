from spotify import get_dict
from youtube import get_youtube_video_ids

def main():
    print("Yo")

def gen_play(ls):
    playlist_link = "https://www.youtube.com/watch_videos?video_ids=" + ','.join(ls)
    return playlist_link

if __name__ == "__main__":
    main()
    a = get_dict(input("Enter playlist :"))
    b = get_youtube_video_ids(a)
    print(gen_play(b))