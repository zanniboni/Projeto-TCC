# ------- Código exemplo para utilizar o detecto com um modelo pré treinado
# from detecto import core, utils, visualize
# image = utils.read_image("apple.jpg")
# #Initializes a pre-trained model
# model = core.Model()
# labels, boxes, scores = model.predict_top(image)
# visualize.show_labeled_image(image, boxes, labels)

# -------- Código exemplo para remover todos os png's da pasta
# import glob
# import pathlib
# for file in glob.glob('frames/*.png'):
#   path = pathlib.Path(file)
#   path.unlink()

# ----------- Código para renomear os arquivos da pasta "Collection"
# import os
# os.getcwd()
# collection = "frames"
# for i, filename in enumerate(os.listdir(collection)):
#   print(filename)
#   os.rename(collection + "/" + filename, collection + "/dinheiro" + str(i) + ".jpg")

# ----------- Código para executar o modelo treinado 'nota_50'
# # Specify the path to your image
# from detecto import core, utils, visualize
# model = core.Model(['nota_50'])
# image = utils.read_image('frames/dinheiro2.jpg')
# predictions = model.predict(image)
# # predictions format: (labels, boxes, scores)
# labels, boxes, scores = predictions
# # ['alien', 'bat', 'bat']
# print(labels)
# print(boxes)
# # tensor([0.9952, 0.9837, 0.5153])
# print(scores)
# visualize.show_labeled_image(image, boxes, labels)