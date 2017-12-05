""" This script will create a markdown (.md) file based on the URL files in a certain directory.
It will organize the links into categories based on the file structure of the directory you pass it.
I typically use this script to convert video links stored in a directory to URLs, but in theory it can be used
for any similar task. """
import os

root_dir = input("Input the root directory to convert to markdown: ")
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
	#index += '\n<div>\n'
	#Table of Contents -- each bullet needs to be indented by 4 spaces for a nested list in markdown
	if(level != 0):
		index += ("&nbsp&nbsp&nbsp&nbsp&nbsp" * (level - 1)) + "<a href=#" + current_dir + ">- " + current_dir + "</a><br>\n"
	#index += "\n</div>\n"
	#create the new directory heading, and then we will add all the video links in it
	bodytext += ("\n<div>\n")
	bodytext += ("&nbsp&nbsp&nbsp&nbsp&nbsp" * (level - 1))
	if(level == 1):
		bodytext += ('<span class="h1" id=' + current_dir + ">" + current_dir + "</span>")
	elif(level == 2):
		bodytext += ('<span class="h2" id=' + current_dir + ">" + current_dir + "</span>")
	elif(level == 3):
		bodytext += ('<span class="h3" id=' + current_dir + ">" + current_dir + "</span>")
	elif(level >= 4):
		bodytext += ('<span class="h4" id=' + current_dir + ">" + current_dir + "</span>")
	bodytext += ("\n</div>\n")
	#create the actual URLs
	bodytext += "\n<div>\n"
	for file in files: #for each file in the current directory
		if file != ".DS_Store":
			#open the file and read the url
			f = open(root + '/' + file, "r")
			url = f.readlines()[1][4:]
			f.close()
			#print out the URL as markdown
			bodytext += "<br>" + ("&nbsp&nbsp&nbsp&nbsp&nbsp" * (level - 1)) + ("- " + "<a href=" + url + " target=_blank>" + file[:-4] + "</a>\n")
	bodytext += "\n</div><br>\n"

output_file.write('<html> <head> <link rel="stylesheet" href="styles.css"> </head> <body>')
output_file.write('<span class="vidintro">Below are some videos I have liked from across the Internet, organized into categories.')
output_file.write(' Most come from Youtube, and were exported from my "Liked Videos" playlist using <a href= "https://sourceforge.net/projects/youtubeexport/">Youtube Export</a>.')
output_file.write(' I manually moved all my video URLs into the categories below, and used a <a href="https://github.com/domcc3/url_organizer">script</a> to create this webpage. Please note that all links will open in a new window.')
output_file.write('\n<br><br><div id="TOC"> Table of Contents</div></span><br>\n')
output_file.write('<div class="index">' + index + '<br><br></div>')
output_file.write(bodytext)
output_file.write('</body></html>')
output_file.close()