# ----------- Código para executar o modelo treinado 'nota_50'
# Specify the path to your image
from detecto import core, utils, visualize
import pyttsx3
engine = pyttsx3.init()


model = core.Model.load('nota_50.pth', ['nota_50'])
# model = core.Model(['nota_50'])
image = utils.read_image('frames/dinheiro13.jpg')
predictions = model.predict_top(image)
# predictions = model.predict(image)
# predictions format: (labels, boxes, scores)
labels, boxes, scores = predictions
# ['alien', 'bat', 'bat']
print(labels)
print(boxes)
print(boxes[0][1])
# tensor([0.9952, 0.9837, 0.5153])
print(scores)
engine.say("Nota de 50 Reais")
engine.runAndWait()
visualize.show_labeled_image(image, boxes, labels) 