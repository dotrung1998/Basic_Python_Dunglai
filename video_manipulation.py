#Check all function
#1: "\n": Wrong
#2: choice = int(choice): Already number in "while not"
#3: choice = select in range(...) -> playlist.videos[choice]
#4: "print.videos" -> "print_videos": ERROR 'builtin_function_or_method' object has no attribute 'videos'
import webbrowser 

class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link
		self.seen = False

	def open(self):
		webbrowser.open(self.link)
		self.seen = True

class Playlist: 
	def __init__(self, name, description, rating, videos):
		self.name = name
		self.description = description
		self.rating = rating
		self.videos = videos

def read_video():
	title = input("Enter title: ") +"\n" #1
	link = input("Enter link: ") + "\n" #1
	video = Video(title, link)
	return video

def print_video(video):
	print("Video title: ", video.title, end="")
	print("Video link: ", video.link, end="")

def read_videos():
	videos = []
	total_video = int(input("Enter how many videos: "))
	for i in range(total_video):
		print("Enter video: ", i+1)
		vid = read_video()
		videos.append(vid)
	return videos

def print_videos(videos):
	print("---")
	for i in range(len(videos)):
		print("Video " + str(i+1) + ":")  #!!
		print_video(videos[i])

def write_video_txt(video, file):
	file.write(video.title) #1
	file.write(video.link)

def write_videos_txt(videos, file):
	# with open("data.txt", "r") as file: 
	total = len(videos)
	file.write(str(total) + "\n")
	for i in range(total):
		write_video_txt(videos[i], file)

def read_video_from_txt(file):
	title = file.readline()
	link = file.readline()
	video = Video(title, link)
	return video

def read_videos_from_txt(file): 
	videos = []
	# with open("data.txt", "r") as file: 
	total = file.readline()		
	for i in range(int(total)):
		video = read_video_from_txt(file)
		videos.append(video)
	return videos

def read_playlist():
	playlist_name = input("Enter playlist name: ") + "\n" #\: backward slash #1
	playlist_description = input("Enter playlist description: ") + "\n" #1
	playlist_rating = input("Playlist rating (1-5): ") +"\n" #1
	playlist_videos = read_videos()
	playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos) 
	return playlist

def write_playlist_to_txt(playlist):
	with open("data.txt", "w") as file:
		file.write(playlist.name) #1: Upper has "\n"
		file.write(playlist.description)
		file.write(playlist.rating)
		write_videos_txt(playlist.videos, file) #1 Add file to use that file  and not rewrite the textfile

def read_playlist_from_txt():
	with open("data.txt", "r") as file: 
		 playlist_name = file.readline()
		 playlist_description = file.readline()
		 playlist_rating = file.readline()
		 playlist_videos = read_videos_from_txt(file)
		 playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
	return playlist

def print_playlist(playlist):
	print("----")
	print("Playlist name: " + playlist.name, end = "") 
	print("Playlist description: " + playlist.description, end = "")
	print("Playlist rating: " + playlist.rating, end = "")
	print_videos(playlist.videos) 

def show_menu():
	print("----------------------------")
	print("| Option 1: Create playlist |")
	print("| Option 2: Show playlist   |")
	print("| Option 3: Play video      |")
	print("| Option 4: Add video       |")
	print("| Option 5: Update playlist |")
	print("| Option 6: Delete video    |")
	print("| Option 7: Save and exist  |")
	print("| Option 8: Search  video   |")
	print("----------------------------")

def select_in_range(promt, min, max):
	choice = input(promt)
	while not choice.isdigit() or int(choice) < min or int(choice) > max: #Number : True, NOT number: false ; 
		choice = input(promt)

	choice = int(choice) #2: Already number in "while not"
	return choice

def play_video(playlist): #
	print_videos(playlist.videos) #4: print.videos: ERROR 'builtin_function_or_method' object has no attribute 'videos'
	total = len(playlist.videos)

	choice = select_in_range("Select video (1-" + str(total) + "): ", 1,total)
	print("Open video: " + playlist.videos[choice - 1].title + playlist.videos[choice - 1].link, end = "")
	# webbrowser.open(playlist.videos[choice - 1].link)
	playlist.videos[choice-1].open() #Also when use webbrowser

def add_video(playlist):
	print("Enter new video information: ")
	new_video_title = input("Enter new title: ") + "\n"
	new_video_link = input("Enter new link: ") + "\n"
	new_video = Video(new_video_title, new_video_link) #Call again avaiable __init__
	playlist.videos.append(new_video) #In here we just have playlist so must add video into "video" in "playlist"
	return playlist #new video is added into playlist -> return playlist

def update_playlist(playlist):
	print("Update playlist?")
	print("1. Name")
	print("2. Description")
	print("3. Rating")

	choice = select_in_range("Which option do you want to change? (1-3): ", 1,3)
	if choice == 1:
		new_playlist_name = input("Enter new playlist's name: ") +"\n"
		playlist.name = new_playlist_name
		print("Updated successfully!")
		return playlist
	if choice == 2:
		new_video_description = input("Enter new playlist's description: ") +"\n"
		playlist.description = new_video_description
		print("Updated successfully!")
		return playlist
	if choice == 3:
		new_video_rating = str(select_in_range("Select new rating (1-5): ", 1, 5)) + "\n"
		playlist.rating = new_video_rating
		print("Updated successfully!")
		return playlist

def remove_video(playlist):
	print_videos(playlist.videos)
	total = len(playlist.videos)

	choice = select_in_range("Select video you want to delete: " ,1, total)
	# del playlist.videos[choice - 1]

	new_video_list = []
	for i in range(total): #Just 
		if i == choice-1:
			continue #6: Don't add the choice to the 
		new_video_list.append(playlist.videos[i])

	playlist.videos = new_video_list	#5 Replace old list with new list
	print("Delete successfully!!")
	return playlist

def search_for_name(playlist):
	choice = input("Enter video you want to search?")
	for i in range(len(playlist.videos)):
		if choice in playlist.videos[i].title:
			print("Open video:" + choice)
			playlist.videos[i].open()	
		else:
			continue

def main():
	# videos = read_videos()
	# write_videos_txt(videos)	#4: Used in playlist #4:
	# videos = read_videos_from_txt()
	# print_videos(videos)

	# playlist = read_playlist()
	# write_playlist_to_txt(playlist)
	# playlist = read_playlist_from_txt()
	# print_playlist(playlist)

	try:
		playlist = read_playlist_from_txt() #be chosed #2: If here is read_playlist: input and then print("Loaded text successfully")
		print("Loaded text successfully")
	except:
		print("Welcome first user")


	while True:
		show_menu()
		# choice = int(input("Select an option (1-7): "))
		choice = select_in_range("Select an  option (1-8): ", 1, 8)
		if choice == 1:
			playlist = read_playlist() #Must have "playlist" ; create playlist
			input("\nPress enter to continue." + "\n")
		elif choice == 2:
			print_playlist(playlist) #Show playlist
			input("\nPress enter to continue." + "\n")
		elif choice == 3:
			play_video(playlist) #Just playlist
			input("\nPress enter to continue." + "\n")
		elif choice == 4:
			playlist = add_video(playlist) #!: Give playlist to know which playlist, and then return new playlist -> 'playlist ='
		elif choice == 5:
			playlist = update_playlist(playlist) #!: Give playlist to know which playlist, and then return new playlist -> 'playlist ='
			input("\nPress enter to continue." + "\n")
		elif choice == 6:
			playlist = remove_video(playlist)
			input("\nPress enter to continue." + "\n")
		elif choice == 7:
			write_playlist_to_txt(playlist) #save and exist
			input("\nPress enter to continue." + "\n")
			break
		elif choice == 8:
			search_for_name(playlist)
			input("\nPress enter to continue." + "\n")
		# else:
		# 	print("Wrong input, exist")     # Already loop choice
		# 	break


main()