import cv2
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim

def match(path1, path2, show_images=True):
    img1, img2 = cv2.imread(path1, cv2.IMREAD_GRAYSCALE), cv2.imread(path2, cv2.IMREAD_GRAYSCALE)
    if img1 is None or img2 is None:
        print("Error: One or both images could not be loaded.")
        return 0
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0])) if img1.shape != img2.shape else img2
    similarity_value = round(ssim(img1, img2) * 100, 2)
    if show_images:
        fig, axes = plt.subplots(1, 2, figsize=(8, 4))
        for ax, img, title in zip(axes, [img1, img2], ["Signature 1", "Signature 2"]):
            ax.imshow(img, cmap='gray')
            ax.set_title(title)
            ax.axis("off")
        plt.suptitle(f"Similarity: {similarity_value}%", fontsize=12)
        plt.show()
    return similarity_value
