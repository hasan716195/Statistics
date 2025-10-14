import json
def data(filename,xaxis, yaxis):
    values = {'x': xaxis, 'y': yaxis}
    with open(filename, 'w') as f:
        json.dump(values, f)
    return values

class StatsCalculator():
    def __init__(self,file_name):
        self.file = file_name
        self.data = None

    def load_data(self):
        with open(self.file,'r') as f:
            data = json.load(f)
            self.data = data

    def data(self,xaxis,yaxis):
        #emptylist = [1,2]
        #if type(xaxis) == type(emptylist):
            #return False
        #if type(yaxis) == type(emptylist):
            #return False
        values = {'x':xaxis,'y':yaxis}
        with open(self.file,'w') as f:
            json.dump(values,f)
        return values

    def calculate_mean(self):
        data = self.data
        x_values = data['x']
        y_values = data['y']
        summation = len(x_values)
        empty_list = []
        active = True
        while active:
            x = x_values[0]
            x *= y_values[0]
            empty_list.append(x)
            y_values = y_values[1:]
            x_values = x_values[1:]
            if len(y_values) == 0:
                active = False
                print(x,empty_list)

        frequency_x_value = sum(empty_list)

        mean = frequency_x_value / summation
        print(mean)



if __name__ == '__main__':
    statss = StatsCalculator('data.json')
    data('data.json',[2,4,6,8],[1,1,2,1])
    statss.load_data()
    statss.calculate_mean()