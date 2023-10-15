class Message:
    def __init__(self, priority, data):
        self.priority = priority
        self.data = data
    def __str__(self):
        return str(self.data)
    
    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, p):
        if p < 0: 
            raise Exception("Priority Must be 0 or positive number")
        self._priority = p

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, d):
        if not d: 
            raise Exception("data cannot be empty")
        self._data = d
