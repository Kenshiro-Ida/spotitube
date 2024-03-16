from youtubesearchpython import VideosSearch
from spotify import get_dict

def get_youtube_video_ids(song_data):
    video_ids = []
    for song, artist in song_data.items():
        query = f"{song} {artist} official music video"
        videosSearch = VideosSearch(query, limit=1)
        results = videosSearch.result()
        if results['result']:
            video_id = results['result'][0]['id']
            video_ids.append(video_id)
    return video_ids

def main():
    print("hello")
    # a = get_dict("https://open.spotify.com/playlist/73Pb0ylLKE6BQjun5r0iCf")
    # b = get_youtube_video_ids(a)
    # print(b)

if __name__ == "__main__":
    main()