import json
def data(filename,xaxis, yaxis):
    values = {'x': xaxis, 'y': yaxis}
    with open(filename, 'w') as f:
        json.dump(values, f)
    return values

class StatsCalculator:
    def __init__(self,file_name):
        self.file = file_name
        self.data = None

    def load_data(self):
        with open(self.file,'r') as f:
            data01 = json.load(f)
            self.data = data01

    #def data(self,xaxis,yaxis):
        #emptylist = [1,2]
        #if type(xaxis) == type(emptylist):
            #return False
        #if type(yaxis) == type(emptylist):
            #return False
        #values = {'x':xaxis,'y':yaxis}
        #with open(self.file,'w') as f:
            #json.dump(values,f)
        #return values

    def calculate_mean(self):
        data02 = self.data
        x_values = data02['x'].copy()
        y_values = data02['y'].copy()
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

    def cummulative_frequency(self):
        data03 = self.data
        print(data03)
        y_values = data03['y'].copy()
        print(y_values)
        active = True
        cumla_fre = []
        while active:
            x = y_values[0]
            x += y_values[1]
            cumla_fre.append(x)
            y_values[0] = x
            del y_values[1]
            if len(y_values) == 1:
                active = False
        cumla_fre.insert(0,1)
        print(data03)
        return cumla_fre

    def relative_frequency(self):
        dataa = self.data
        print(dataa)
        y_values = dataa['y'].copy()
        print(y_values)
        ys_values = y_values.copy()
        summation = sum(ys_values)
        print(summation)
        rela_frequency = []
        for x in y_values:
            print(x)
            x /= summation
            x *= 100
            print(x)
            rela_frequency.append(x)
        print(rela_frequency)


if __name__ == '__main__':
    statss = StatsCalculator('data.json')
    data('data.json',[2,4,6,8],[1,1,2,1])
    statss.load_data()
    statss.calculate_mean()
    statss.cummulative_frequency()
    print(statss.__dict__)
    statss.relative_frequency()