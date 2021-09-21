# ----------- Código para executar o modelo treinado 'nota_50'
# Specify the path to your image
from detecto import core, utils, visualize
model = core.Model(['nota_50.pth'])
image = utils.read_image('frames/dinheiro2.jpg')
predictions = model.predict(image)
# predictions format: (labels, boxes, scores)
labels, boxes, scores = predictions
# ['alien', 'bat', 'bat']
print(labels)
print(boxes)
# tensor([0.9952, 0.9837, 0.5153])
print(scores)
visualize.show_labeled_image(image, boxes, labels)