import cv2

imagem = cv2.imread('imagem.jpg')

imagem = cv2.resize(imagem, (800, 800))

imagem_pb = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

_, mask = cv2.threshold(imagem_pb, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

resultado = cv2.bitwise_and(imagem_pb, imagem_pb, mask=mask)

cv2.imshow('Resultado Preto e Branco', resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()