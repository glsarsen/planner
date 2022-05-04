class CustomList(list):
    def remove_if_exist(self, elem):
        if elem in self:
            self.remove(elem)
        