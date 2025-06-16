from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://youtubpy:youtubepy@cluster0.lxl3fsq.mongodb.net/", tlsAllowInvalidCertificates = True) # string created in the mongodb (ytmanager is a DB name)
# Not a good idea to harcode user and password

db = client["ytmanager"]
video_collection = db["videos"]

def list_all_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']} Name: {video['name']} and Time: {video['time']}")

def add_a_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_videos(new_name, new_time, video_id):
    video_collection.update_one(
        {'_id': ObjectId},
        {'$set': {"name": new_name, "time": new_time}}
    )

def delete_videos(video_id):
    video_collection.delete_one({'_id': video_id})

def main():
    while True:
        print("\n Youtube Manager App With MongoDB")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the application")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos()
            case '2':
                name = input("Enter the name of video: ")
                time = input("Enter the time period of video: ")
                add_a_video(name, time)
            case '3':
                video_id = input("Enter the video ID to update: ")
                name = input("Enter the name of video: ")
                time = input("Enter the time period of video: ")
                update_videos(name, time, video_id)
            case '4':
                video_id = input("Enter the video ID to delete: ")
                delete_videos(video_id)
            case '5':
                break
            case '_':
                print("Invalid input")


if __name__ == "__main__":
    main()
