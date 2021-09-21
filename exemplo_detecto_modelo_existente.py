# ------- Código exemplo para utilizar o detecto com um modelo pré treinado
from detecto import core, utils, visualize
image = utils.read_image("apple.jpg")
#Initializes a pre-trained model
model = core.Model()
labels, boxes, scores = model.predict_top(image)
visualize.show_labeled_image(image, boxes, labels)