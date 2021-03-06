# ----------- Código para executar o modelo treinado 'nota_50'
# Specify the path to your image
from detecto import core, utils, visualize
import cv2
import pyttsx3
import numpy as np

model = core.Model.load('notas_final.pth', ['nota_10','nota20','nota100','25cent','nota_5','1real','nota_2','5cent','nota50','50cent'])
                                      
# image = utils.read_image('321321.jpg')
# predictions = model.predict_top(image)
# labels, boxes, scores = predictions
# print(labels, scores)
# visualize.show_labeled_image(image, boxes, labels)
engine = pyttsx3.init()


cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()

    predictions = model.predict(frame)
    print(predictions)
    labels, boxes, scores = predictions

    try:
        scores_numpy = scores.numpy()
        print(scores_numpy)
        print(labels)
        max_value = max(scores_numpy)

        max_index = np.argmax(scores_numpy)
        detectado = (max_value > 0.7)
        label_detectado = labels[max_index]
        # Quando detectar um score maio que 0.7, iremos ter o retorno sonoro da detecção
        #'nota10','nota20','nota100','25cent','nota_5','1real','nota_2','5cent','maca','nota50','50cent'
        if detectado:
            print(label_detectado)
            if label_detectado == "nota50":
                engine.say("50 reais")
            elif label_detectado == "nota20":
                engine.say("20 reais")
            elif label_detectado == "25cent":
                engine.say("25 centavos")
            elif label_detectado == "nota_5":
                engine.say("5 reais")
            elif label_detectado == "1real":
                engine.say("1 real")
            elif label_detectado == "nota_2":
                engine.say("2 reais")
            elif label_detectado == "5cent":
                engine.say("5 centavos")
            elif label_detectado == "maca":
                engine.say("Maçã")
            elif label_detectado == "50cent":
                engine.say("50 centavos")
            elif label_detectado == "nota_10":
                engine.say("10 reais")
            elif label_detectado == "nota100":
                engine.say("100 reais")

            engine.runAndWait()
        cv2.imshow('Object detection', frame)

    except:
        cv2.imshow('Object detection', frame)

    if cv2.waitKey(10) ** 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

