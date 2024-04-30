import json

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("\n")
    print("*" * 70)

def add_video(videos):
    vname = input("Enter video name: ")
    vtime = input("Enter video time: ")
    videos.append({'name': vname, 'time': vtime})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))
    if(1 <= index <= len(videos)):
        vname = input("Enter the new video name: ")
        vtime = input("Enter the new video time: ")
        videos[index-1] = {'name':vname, 'time': vtime}
        save_data_helper(videos) 
    else:
        print("invalid index selection")
       
def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted: "))
    if(1 <= index <= len(videos)):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid Video index selected")

def load_data():
    videos = []
    try:
        with open("youtube.txt", 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open("youtube.txt", 'w') as file:
        json.dump(videos, file)

def main():
    videos = load_data()
    while True:
        print("Youtube Manager | Choose your option")
        print("1. All Videos ")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit")
        choice = input("Enter your choice: ")
        print(videos)
        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()