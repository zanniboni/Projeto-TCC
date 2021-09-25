# ----------- Código para executar o modelo treinado 'nota_50'
# Specify the path to your image
from detecto import core, utils, visualize
import cv2

model = core.Model.load('nota_50.pth', ['nota_50'])
# image = utils.read_image('frames/dinheiro13.jpg')
# predictions = model.predict_top(image)
# labels, boxes, scores = predictions
# visualize.show_labeled_image(image, boxes, labels)


cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()

    predictions = model.predict_top(frame)
    labels, boxes, scores = predictions
    cv2.rectangle(frame, boxes, boxes, (0, 0, 255), 1)

    cv2.imshow('Objetct detection', frame)

    if cv2.waitKey(10) ** 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()