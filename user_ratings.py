class UserRatings:

    def __init__(self, product_id: int, comments: str):
        self.product_id = product_id
        self.comments = comments

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        self._product_id = product_id

    @property
    def comments(self):
        return self._comments

    @comments.setter
    def comments(self, comments):
        self._comments = comments
