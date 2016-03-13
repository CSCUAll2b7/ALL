def linearSearch(self, array, val):
        pos = 0
        while pos < len (array):
            if array[pos] == val:
                return True
            pos = pos + 1
        return False
