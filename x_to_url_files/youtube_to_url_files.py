#This file converts from an extracted Youtube playlist (in a text file) to .url files

#read in all the lines from the old file
textfile_name = input("Enter your file name: ")
f = open(textfile_name, "r")
lineArray = []
for line in f:
	line.strip()
	lineArray.append(line)
f.close()

#extract only the necessary information from the array
newArray = []
for line in lineArray:
	link_index = line.find("www")
	link = (line[link_index:(link_index + 35)]) #youtube links are always 35 chars long
	if(link.find("http") == -1):
		link = "http://" + link
	#to get the title, find where the last \t char occurs
	old_title_index = 0
	while line.find("\t", old_title_index, len(line)) != -1: #the last 2 arguments are the substring to look in
		title_index = line.find("\t", old_title_index, len(line))
		old_title_index = title_index + 2 #add 2 so we skip over the \t
	title = line[title_index:len(line)]
	# get rid of all the unneeded chars/chars that mess everything up
	title = title.strip('\r')
	title = title.strip('\n')
	title = title.strip('\t')
	title = title.strip('\r')
	title = title.replace("/"," ")
	title = title.replace("|"," ")
	newArray.append("* [" + title + "](" + link + ")\n")
	filename = title + ".url"
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
