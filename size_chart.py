class SizeChart:

    def __init__(self, chest, waist, hips, inseam, body_height, weight):
        self.chest = chest
        self.waist = waist
        self.hips = hips
        self.inseam = inseam
        self.body_height = body_height
        self.weight = weight

    @property
    def chest(self):
        return self._chest

    @chest.setter
    def chest(self, chest):
        self._chest = chest

    @property
    def waist(self):
        return self._waist

    @waist.setter
    def waist(self, waist):
        self._waist = waist

    @property
    def hips(self):
        return self._hips

    @hips.setter
    def hips(self, hips):
        self._hips = hips

    @property
    def inseam(self):
        return self._inseam

    @inseam.setter
    def inseam(self, inseam):
        self._inseam = inseam

    @property
    def body_height(self):
        return self._body_height

    @body_height.setter
    def body_height(self, body_height):
        self._body_height = body_height

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight
