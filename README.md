# Python-panorama-stitching
This program is designed to take pictures and stitch them together into one big panorama. Eventually, I want it to be able to stitch together a panorama of multiple pics, and then to be able to work with frames of a video; but for right now, it's just for 2 pictures.

Process:
1. Place files into designated folder
2. The program checks the folder for photos
3. Using opencv, it will identify any points of similarity between the photos, comparing one photo to the next item on the list
4. If it doesn't identify any similarities, it will say so
5. If it does find any, it'll say how many it found and proceed to merge them together
6. Once it has gone through all of the photos in the folder, it'll say so, and the panorama will be finished.

NEED TO DO:
- all the things lol
