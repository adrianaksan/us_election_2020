from pytchat import LiveChat
livechat = LiveChat(video_id = "1gvpuY6ISoI")
# It is also possible to specify a URL that includes the video ID:
# livechat = LiveChat("https://www.youtube.com/watch?v=Zvp1pJpie4I")
while livechat.is_alive():
  try:
    chatdata = livechat.get()
    for c in chatdata.items:
         try:
                  print(f"{c.message}")
                  chatdata.tick()
         except:
                  pass

  except KeyboardInterrupt:
    livechat.terminate()
    break
