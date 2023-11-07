from PIL import Image
import pytesseract

# Load the image
image = Image.open('Monalisa.jpg')


try:
    extracted_text = pytesseract.image_to_string(image, config='--psm 6')
except Exception as e:
    print(f"An error occurred: {e}")

# Save to a text file
with open('extracted_text.txt', 'w', encoding='utf-8') as file:
    file.write(extracted_text)
