
class BoardSquare:

    def __init__(self, category, cw, ccw, inner=-1, outer=-1):

        self.category = category
        self.nextSquare = {'cw':cw,'ccw':ccw,'inner':inner,'outer':outer}
        self.isFinal = False

    def __str__(self):
        return str(self.nextSquare)
