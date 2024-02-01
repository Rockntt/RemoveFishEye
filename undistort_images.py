from __future__ import print_function
import numpy as np
import cv2
import os

def splitfn(file_path):
    file_path_parts = file_path.split(sep=os.sep)
    _path = os.path.join(*file_path_parts[:-1])
    file_name = file_path_parts[-1]
    file_name_parts = file_name.split(sep='.')
    return _path, file_name_parts[0], file_name_parts[1]

folder_path = 'frames/'

file_list = []

for filename in os.listdir(folder_path):
    file_list.append(folder_path + filename)

img_names_undistort = file_list
new_path = "undist/"

camera_matrix = np.array([[2.21729823e+03, 0.00000000e+00, 1.92418137e+03],
 [0.00000000e+00, 2.15031504e+03, 8.95376680e+02],
 [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])
dist_coefs = np.array([-0.43375672, 0.24203699, 0.00256289, -0.00120674, -0.07640675])

i = 0

for img_found in img_names_undistort:
    img = cv2.imread(img_names_undistort[i])
    img = cv2.resize(img, (3760, 2120))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    h, w = img.shape[:2]
    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, dist_coefs, (w, h), 1, (w, h))

    dst = cv2.undistort(img, camera_matrix, dist_coefs, None, newcameramtx)

    dst = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)

    x, y, w, h = roi
    dst = dst[y:y+h-50, x+70:x+w-20]

    name = img_found[7:]
    full_name = new_path + "undistorted_" + name.replace('.png','') + '.jpg'

    cv2.imwrite(full_name, dst)
    i = i + 1
    print(f'Processing... {i}/{len(file_list)}')