1. Install OpenCV2
2. Get distortion coefficients of your camera with several test photos of a check board (examples in calibrate_dir folder, check board is in the root directory) with calibrate.py. Your calibration photos should be placed in /calibrate_dir directory.
3. Put these parameters into the ln 29-32 array as I did with mine (of my test images)
4. Put your distorted images into the /frames directory or change your path 
5. In addition, you may change path of saving your images on the 27th line.
6. Run undistort_images.py and wait until it ends it's work in /undist directory.