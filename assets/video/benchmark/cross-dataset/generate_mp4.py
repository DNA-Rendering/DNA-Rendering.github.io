import os
src_dir = "src"
videos = os.listdir(src_dir)
for video in videos:

    os.system(f"ffmpeg -y -r 25 -i {src_dir}/{video} -filter:v 'setpts=12.5*PTS' -r 2 {video.replace('.mp4','.mp4')}")
