import pymongo
from bson.objectid import ObjectId
from dbConnection import ( db )

courses = db["test_courses"]

def getAll():
    courses_array = []
    for course in courses.find():
        # print(course["_id"])
        courses_array.append(course)

    return courses_array

def getDownlodCourses():
    download_courses_array = []
    for course in courses.find({"processed": False, "download": True}):
        download_courses_array.append(course)
    # print(download_courses_array)

    return download_courses_array

def updateVideoStyle(video_style, course):
    select_query = { "_id": ObjectId(course["_id"])}
    insert_value = { "$set": { "videoStyle": video_style} }
    courses.update_one(select_query, insert_value)

    return True

# mycourse = getAll()[0]
# print(mycourse)
# videoStyle = {}
# videoStyle["talkingHead"] = 30
# videoStyle["slide"] = 10
# videoStyle["code"] = 60
# videoStyle["conversation"] = 0
# videoStyle["animation"] = 0
# videoStyle["whiteboard"] = 0
# print(videoStyle)
# updateVideoStyle(videoStyle, mycourse)