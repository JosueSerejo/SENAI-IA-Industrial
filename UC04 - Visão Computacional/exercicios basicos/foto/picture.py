import cv2

imagem = cv2.imread('imagem.jpg')

redimensionada = cv2.resize(imagem, (800, 800))

cv2.imshow('Imagem', redimensionada)

cv2.waitKey(0)

cv2.destroyAllWindows()
