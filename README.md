# yt_dl_nfo_fix

This is supposed to fix the yt-dl-json-to-nfo script. New lines (and other special characters) in the NFO format are different than in the JSON format. So when the description shows in Jellyfin or Kodi, the new line characters are not properly accounted for or displayed. This program aims to find all new line characters in the nfo file and replace them to keep correct formatting.
