import os
src_dir = "src"
videos = os.listdir(src_dir)
for video in videos:

    os.system(f"ffmpeg -y -i {src_dir}/{video} -vf scale=w=0.5*iw:h=0.5*ih -crf 30 {video.replace('.mp4','.mp4')}")
