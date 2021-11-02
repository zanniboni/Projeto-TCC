from detecto import core, utils, visualize
dataset = core.Dataset('images/')
#'nota50','50cent','10cent','5cent'
model = core.Model(['nota_10','nota20','nota100','25cent','nota_5','1real','nota_2','5cent','nota50','50cent'])
#model = core.Model(['nota_10'])
model.fit(dataset)
model.save('notas_oficial.pth')