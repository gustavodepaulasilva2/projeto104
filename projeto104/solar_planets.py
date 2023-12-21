import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "sol",(100,80),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
cv2.putText(img, "Mercurio",(120,180),cv2.FONT_HERSHEY_COMPLEX,0.3,(0,0,255))
cv2.putText(img, "Venus",(200,170),cv2.FONT_HERSHEY_COMPLEX,0.3,(0,0,255))
cv2.putText(img, "Terra",(290,170),cv2.FONT_HERSHEY_COMPLEX,0.3,(0,0,255))
cv2.putText(img, "marte",(390,180),cv2.FONT_HERSHEY_COMPLEX,0.3,(0,0,255))
cv2.putText(img, "jupiter",(500,80),cv2.FONT_HERSHEY_COMPLEX,0.3,(0,0,255))
cv2.putText(img, "saturno",(850,170),cv2.FONT_HERSHEY_COMPLEX,0.3,(0,0,255))
cv2.putText(img, "Urano",(975,140),cv2.FONT_HERSHEY_COMPLEX,0.3,(0,0,255))
cv2.putText(img, "Netuno",(1125,150),cv2.FONT_HERSHEY_COMPLEX,0.3,(0,0,255))


cv2.imshow("resultado",img)
cv2.waitKey(0)