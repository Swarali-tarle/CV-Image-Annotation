import cv2
import numpy as np

# img = cv2.imread('bike.jpg',1)
img = np.zeros((512,512,3))

img = cv2.line(img, (0,0), (255,255), (0,0,255), 5)
img = cv2.arrowedLine(img, (0,255), (255,255), (0,255,0), 5)
img = cv2.rectangle(img, (345,0) , (510,123), (255,0,0) , -1)
img = cv2.circle(img, (227,63), 63, (0,0,235) ,-1)

font = cv2.FONT_ITALIC
img = cv2.putText(img, ('opencv'), (10,500), font,4,(0,255,0), 10, cv2.LINE_AA)

center = (200, 200)           
axes = (100, 50)              
angle = 30                    
startAngle = 0                
endAngle = 360                 
color = (255, 0, 0)            
thickness = 2                 
cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness)

point1 = (100, 300)
point2 = (300, 300)
point3 = (200, 100)
color = (0, 255, 0) 
thickness = 2       
cv2.line(img, point1, point2, color, thickness)
cv2.line(img, point2, point3, color, thickness)
cv2.line(img, point3, point1, color, thickness)

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()