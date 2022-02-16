def sorting(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j][1] > arr[j+1][1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def courses(course_contents):
    f = 0
    s = 0
    numberOfCourses = 0
    for i in range(len(course_contents)):
        s = course_contents[i][0]
        if s > f:
            numberOfCourses += 1
            f = course_contents[i][1]
    return numberOfCourses

course_contents = [[1, 2],[3, 4],[0, 6],[5, 7],[8, 9],[5, 9]]
sorting(course_contents)
print("A student can attend a maximum of ",courses(course_contents), "of the above courses.")