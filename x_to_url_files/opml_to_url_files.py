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
	line.strip()
	title_begin = line.find("title=")
	if (title_begin != -1):
		title_end = line.find('"', (title_begin + 7))
		title = (line[(title_begin + 7):title_end])
	url_begin = line.find("htmlUrl=")
	if(url_begin != -1):
		url_end = line.find('"', (url_begin + 9))
		link = (line[(url_begin + 9):url_end])
	if (title_begin != -1):
		#get rid of all the unneeded chars/chars that mess everything up
		title = title.strip('\r')
		title = title.strip('\n')
		title = title.strip('\t')
		title = title.strip('\r')
		title = title.replace("/"," ")
		title = title.replace("|"," ")
		if(link != "http://"): # if the link is not blank
			filename = dir_name + "/" + "[Channel] " + title + ".url"
			open(filename, 'w')
			file = open(filename, 'w')
			file.write("[InternetShortcut]\n")
			file.write("URL=" + link + "/videos") #link it to the most-viewed videos of the channel
			file.close()