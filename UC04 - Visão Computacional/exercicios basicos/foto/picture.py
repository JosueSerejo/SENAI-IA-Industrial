import cv2

imagem = cv2.imread('imagem.jpg')

imagem_pb = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

redimensionada = cv2.resize(imagem_pb, (800, 800))

cv2.imshow('Imagem', redimensionada)

cv2.waitKey(0)

cv2.destroyAllWindows()
