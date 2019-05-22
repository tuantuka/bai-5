import numpy as np
student_id = [1023, 5202, 6230, 1671, 1682, 5241, 4532]
student_height = [40., 42., 45., 41., 38., 40., 42.0]
sort = np.lexsort((student_id, student_height))
print("Chỉ số: ", sort)
print("Dữ liệu sắp xếp: ", [(student_id[i], student_height[i]) for i in np.argsort(student_height)])