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
    (h, w) = frame.shape[:2]

    predictions = model.predict_top(frame)
    labels, boxes, scores = predictions
    print(labels, boxes, scores)
    cor_retangulo = (0, 0, 255)
    start_X = boxes[0][0]
    start_Y = boxes[0][1]
    end_X = boxes[0][2]
    end_Y = boxes[0][3]

    (start_X, start_Y) = (max(0, start_X), max(0, start_Y))
    (end_X, end_Y) = (min(w - 1, end_X), min(h - 1, end_Y))

    print((start_X, start_Y))
    print((end_X, end_Y))

    cv2.rectangle(frame, (start_X, start_Y), (end_X, end_Y), cor_retangulo, 1)

    cv2.imshow('Object detection', frame)

    if cv2.waitKey(10) ** 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()