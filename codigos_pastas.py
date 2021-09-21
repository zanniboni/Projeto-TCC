# 1º Primeiro efetua o download das imagens na Web através da extensão download all images
# 2º Remover todos os arquivos png e todos os arquivos svg (1º passo)
# 3º Renomear os arquivos para algo que faça sentido
# 4º pip3 install labelImg # Download LabelImg using pip
#     labelImg # Launch the application

# -------- Código exemplo para remover todos os png's da pasta
# import glob
# import pathlib
# for file in glob.glob('nota-20-reais/*.png'):
#   path = pathlib.Path(file)
#   path.unlink()

# ----------- Código para renomear os arquivos da pasta "Collection"
# import os
# os.getcwd()
# collection = "nota-20-reais"
# for i, filename in enumerate(os.listdir(collection)):
#   print(filename)
#   os.rename(collection + "/" + filename, collection + "/nota-20-" + str(i) + ".jpg")

