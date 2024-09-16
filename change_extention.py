#change file extentions from jpeg to jpg

import glob, os

for filename in glob.iglob(os.path.join('images', '*.jpeg')):
    os.rename(filename, filename[:-5] + '.jpg')
