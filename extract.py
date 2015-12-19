# Written by Jerzy Baran 2015

# This code takes filenames (videos) as arguments and extracts each frame
# from them.

import sys
import cv2

def printUsage():
	print "Usage:"
	print "extract.py file [file, ...]"

def processVideo(videoFile):
	# Open the file for reading
	file = cv2.VideoCapture(videoFile)
	index = 0	# Used to number the frames

	# Extract a frame
	ret, frame = file.read()

	# Save the frame to file
	if ret:
		cv2.imwrite(videoFile + "%d.jpg" % index, frame)

	while ret:
		# Extract a frame
		ret, frame = file.read()

		# Save the frame to file
		if ret:
			cv2.imwrite(videoFile + "%d.jpg" % index, frame)

		index += 1

	file.release()

def main(argv):
	print "Python Frame Etractor, using OpenCV " + cv2.__version__
	print "Preparing to process %d videos" % len(argv)

	for file in argv:
		print "Extracting from " + file
		processVideo(file)

if __name__ == "__main__":
	if len(sys.argv) == 1:
		print "Pass at least one argument"
		print ""
		printUsage()
		sys.exit()

	main(sys.argv[1:])