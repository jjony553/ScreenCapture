from PIL import ImageGrab
import time

now = time.localtime()
time = "%04d-%02d-%02d-%02dh-%02dm-%02ds" %(now.tm_year, now.tm_mon, now.tm_mday
,now.tm_hour,now.tm_min,now.tm_sec)

img = ImageGrab.grab()
saveas = '{}{}'.format(time,'.png')
img.save(saveas)