#This file takes chrome bookmarks in an exported file and converts them to .url files.

import os

my_file_name = input("Input the file name to read: ")
dir_name = input("Input the folder where you want the files to go: ")
os.makedirs(dir_name)

#read in all the lines from the old file
f = open(my_file_name, "r")
lineArray = []
for line in f:
	line.strip()
	lineArray.append(line)
f.close()

#extract only the necessary information from the array
newArray = []
for line in lineArray:
	#GET URL
	link_begin_index = line.find("http")
	link_end_index = line.find("ADD_DATE") - 2
	link = (line[link_begin_index:link_end_index])
	if(link.find("http") == -1):
		link = "http://" + link
	#GET TITLE
	title_begin_index = line.find('">') + 2
	title_end_index = line.find("</A>")
	title = line[title_begin_index:title_end_index]
	#get rid of all the unneeded chars/chars that mess everything up
	title = title.strip('\r')
	title = title.strip('\n')
	title = title.strip('\t')
	title = title.strip('\r')
	title = title.replace("/"," ")
	title = title.replace("|"," ")
	if(link != "http://"): # if the link is not blank
		filename = dir_name + "/" + title + ".url"
		open(filename, 'w')
		file = open(filename, 'w')
		file.write("[InternetShortcut]\n")
		file.write("URL=" + link)
		file.close()
# 	
# #rewrite the lines to a different file
# file = open("youtube-vids2.txt", "w")
# for lineNum in range(0, len(newArray)):
# 	file.write(newArray[lineNum])
# file.close()