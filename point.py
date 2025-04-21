class Point():
    def __init__(self, value = None, left=False, top=False, right=False, bottom=False):
        self.value = value
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
    def __repr__(self):
        borders = ""
        if self.left:
            borders += "L"
        if self.top:
            borders += "T"
        if self.right:
            borders += "R"
        if self.bottom:
            borders += "B"

        return f"Point({self.value} [{borders}])"
