import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('clown.jpg', 0)

cols, rows = img.shape[0:2]

def notch_reject_filter(raio=9, dist_y=0, dist_x=0):
    output = np.zeros((cols, rows))
    for i in range(0, cols):
        for j in range(0, rows):
            
            # calcular posiçao dos pontos
            point_1 = np.sqrt((i - cols / 2 + dist_y) ** 2 + (j - rows / 2 + dist_x) ** 2)
            point_2 = np.sqrt((i - cols / 2 - dist_y) ** 2 + (j - rows / 2 - dist_x) ** 2)
            
            # criar ponto preto
            if point_1 <= raio or point_2 <= raio:
                output[i, j] = 0.0
            else:
                output[i, j] = 1.0
    return output

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
phase_spectrumR = np.angle(fshift)
magnitude_spectrum = 20*np.log(np.abs(fshift))

# aplicando pontos pretos nos focos de ruidos do espectrum

# raio, dist_y e dis_x entre os pontos
H1 = notch_reject_filter(10, 20, 15)
H2 = notch_reject_filter(15, -20, 40)

NotchFilter = H1*H2
NotchRejectCenter = fshift * NotchFilter 
NotchReject = np.fft.ifftshift(NotchRejectCenter)
inverse_NotchReject = np.fft.ifft2(NotchReject)

Result = np.abs(inverse_NotchReject)

plt.subplot(222)
plt.imshow(img, cmap='gray')
plt.title('Original')

plt.subplot(221)
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('magnitude spectrum')

plt.subplot(223)
plt.imshow(magnitude_spectrum*NotchFilter, "gray") 
plt.title("Notch Reject Filter")

plt.subplot(224)
plt.imshow(Result, "gray") 
plt.title("Result")


plt.show()