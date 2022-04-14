import spacy
raw_text="INTERNATIONAL BESTSELLING AUTHOR NORA BARRETT THE KING OF DRUGS"
raw_text = raw_text.lower()
# raw_text = "Nora Barrett"

NER = spacy.load("en_core_web_sm")

text= NER(raw_text)
for w in text.ents:
    print(w)
    print(w.text,w.label_)







# import pprint
# # importing modules
# import cv2
# import pytesseract
# pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tessaract\\tesseract.exe'

# img = cv2.imread("C:\\Users\\lenovo\\Desktop\\Adhoora\\academics\\year3\\cs305\\assignment3\\test\\resources\\book-covers-big-2019101610.jpg")
# import os

# def get_string(img_path, method):
#     img = cv2.imread(img_path)

#     # Extract the file name without the file extension
#     file_name = os.path.basename(img_path).split('.')[0]
#     file_name = file_name.split()[0]

#     # Create a directory for outputs
#     output_path = os.path.join(output_dir, file_name)
#     if not os.path.exists(output_path):
#         os.makedirs(output_path)
#     # Rescale the image, if needed.
#     img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
#     # Convert to gray
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # Apply dilation and erosion to remove some noise
#     kernel = np.ones((1, 1), np.uint8)
#     img = cv2.dilate(img, kernel, iterations=1)
#     img = cv2.erode(img, kernel, iterations=1)
#     # Apply threshold to get image with only black and white
#     img = apply_threshold(img, method)
#     # Save the filtered image in the output directory
#     save_path = os.path.join(output_path, file_name + "_filter_" + str(method) + ".jpg")
#     cv2.imwrite(save_path, img)

#     # Recognize text with tesseract for python
#     result = pytesseract.image_to_string(img, lang="eng")
#     return result


# h, w, c = img.shape
# boxes = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
# print(boxes)
