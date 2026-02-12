import cv2

# Carrega e redimensiona
imagem = cv2.imread('imagem.jpg')
imagem = cv2.resize(imagem, (800, 800))

# Converte para Cinza
imagem_pb = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# APLICA O BLUR (Suavização)
blur = cv2.GaussianBlur(imagem_pb, (5, 5), 0)

# APLICA O EDGES (Detecção de bordas no blur)
edges = cv2.Canny(blur, 50, 150)

# Gera a Máscara (Usando o BLUR para melhor resultado)
# O uso do 'blur' aqui ajuda o Otsu a ser mais preciso
_, mask = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Aplica a máscara na imagem
resultado = cv2.bitwise_and(imagem_pb, imagem_pb, mask=mask)

# --- EXIBIÇÃO ---
cv2.imshow('1. Blur', blur)
cv2.imshow('2. Edges', edges)
cv2.imshow('3. Resultado Final', resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()