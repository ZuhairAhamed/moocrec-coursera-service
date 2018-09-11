from scrapper.coursera_dl import ( scrapper )
from db.coursedb import ( Courses )



if __name__ == '__main__':
    # scrapper()
    courses = Courses()
    # print(courses.getDownloadCoursesPaths())

    download_courses = courses.getDownlodCourses()

    for course in download_courses:
        if scrapper(course["path"]):
            courses.updateProcessedTrue(course)
        else:
            courses.updateProcessedFalse(course)
        