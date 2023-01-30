import os
import re

# This program when run will fix an .NFO file's formatting.
#
# When you use yt-dlp and download the video's information, the info comes in the form of a JSON format. There is a program
#   that I have also downloaded that will take that JSON file and convert it to a Kodi-ready .NFO file. The problem with this is
#   the program does not handle new line chars correctly. So, my program will fix that - once the program runs it will: 
#   search for any files in a directory that end in .NFO, 
#   find their description tag, 
#   take all the text, 
#   find the new-line chars, 
#   and replace them with their .NFO counterpart.

path = "/Users/etdirksen/Documents/Coding/"
dir_list = os.listdir(path)

for file in dir_list:
    if re.search(".nfo", file):
        with open(f"{path}{file}") as f:
            for line in f:
                x = re.findall(pattern="<plot>", string=line)
                if x:
                    print(line)
                #z = re.sub("\n", "&#xA;", line)

                #if z:
                    #print(z)