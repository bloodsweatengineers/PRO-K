class compare_values:
    def __init(self, new_values, old_values):
        self.new_values = new_values
        self.old_values = old_values
        self.compare_list = []

        for x in range(len(new_values)):
            if new_values[x] == old_values[x]:
                compare_list.append(None)
            elif new_values[x] != old_values[x]:
                compare_list.append(new_values[x])
    
    def __call__(self):
        return compare_list
      
