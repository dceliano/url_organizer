""" This script will create a markdown (.md) file based on the URL files in a certain directory.
It will organize the links into categories based on the file structure of the directory you pass it.  """
import os

root_dir = input("Input the root directory to convert to markdown: ")
#root_dir = "video_links"
output_filename = input("What do you want the output file to be called? ")
open(output_filename, 'w')
output_file = open(output_filename, 'w')
bodytext = ""
index = ""
blank = "_blank"
for root, dirs, files in os.walk(root_dir): #for each directory and subdirectory
	path = root.split('/')
	level = len(path) - 1
	current_dir = os.path.basename(root)
	index += "\n<div>\n"
	index += ("&nbsp&nbsp&nbsp&nbsp&nbsp" * level) + "<A href=#" + current_dir + ">- " + current_dir + "</A>\n" #Table of Contents -- each bullet needs to be indented by 4 spaces for a nested list in markdown
	index += "\n</div>\n"
	#create the new directory heading, and then we will add all the video links in it
	bodytext += ("\n<div>\n")
	if(level == 1):
		bodytext += ("<h1 id=" + current_dir + ">" + current_dir + "</h1>")
	elif(level == 2):
		bodytext += ("<h2 id=" + current_dir + ">" + current_dir + "</h2>")
	elif(level == 3):
		bodytext += ("<h3 id=" + current_dir + ">" + current_dir + "</h3>")
	elif(level >= 4):
		bodytext += ("<h4 id=" + current_dir + ">" + current_dir + "</h4>")
	bodytext += ("\n</div>\n")
	bodytext += "\n<div>\n"
	for file in files: #for each file in the current directory
		if file != ".DS_Store":
			#open the file and read the url
			f = open(root + '/' + file, "r")
			url = f.readlines()[1][4:]
			f.close()
			#print out the URL as markdown
			bodytext += ("- " + "<a href=" + url + " target=_blank>" + file[:-4] + "</a>\n")
	bodytext += "\n</div>\n"
output_file.write("Below are some videos I have liked on Youtube, organized into categories. I made this list by using Youtube Export, using a custom python script to get the link/text into Markdown format, and then manually moving the videos in the categories below.")
output_file.write("---\nlayout: page\ntitle: Videos\n---\n")
output_file.write("Index of videos: \n\n" + index + '\n')
output_file.write(bodytext)
output_file.close()