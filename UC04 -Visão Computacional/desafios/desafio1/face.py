#detector de rosto
#Ler uma imagem do disco.
# Verificar suas dimensões (altura, largura, canais).
# Converter o padrão de cor (BGR para RGB) para exibição.
# Carregar um classificador pré-treinado (Haar Cascade).
# Executar a detecção de objetos (ex: faces) na imagem.
# Desenhar retângulos (bounding boxes) sobre os objetos detectados.

import cv2
# Carregar o classificador Haar Cascade para detecção de rosto
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Ler a imagem do disco
image = cv2.imread('dw2.jpg')

# Verificar as dimensões da imagem
height, width, channels = image.shape
print(f"Dimensões da imagem: {height}x{width}, Canais: {channels}")

# Converter a imagem de BGR para RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Detectar rostos na imagem
faces = face_cascade.detectMultiScale(image_rgb, scaleFactor=1.2, minNeighbors=4, minSize=(30, 30))

# Desenhar retângulos ao redor dos rostos detectados
for (x, y, w, h) in faces:
    cv2.rectangle(image_rgb, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Exibir a imagem com os rostos detectados
cv2.imshow('Rostos Detectados', cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR))
cv2.waitKey(0)
cv2.destroyAllWindows()

