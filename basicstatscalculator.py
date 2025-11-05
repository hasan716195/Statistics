import json , math
def data(filename,xaxis, yaxis):
    values = {'x': xaxis, 'y': yaxis}
    with open(filename, 'w') as f:
        json.dump(values, f)
    return values

def sort_data(data):

    dataco1 = data.copy()
    dataco = sorted(dataco1)
    datacoo = dataco
    print(datacoo,datacoo[3:])
    n = len(data)
    sortedobs = sorted(data)
    print(sortedobs)
    active = True
    freq = []
    obs = []
    while active:
        x = datacoo[0]
        nc = datacoo.count(x)
        obs.append(x)
        freq.append(nc)
        datacoo = datacoo[nc:]
        if len(datacoo) == 0:
            active = False
        else:
            continue
    return freq , obs

def inputsdata(filename,data01):
    ret_val = sort_data(data01)
    data(filename,ret_val[1],ret_val[0])


class StatsCalculator:
    def __init__(self,file_name):
        self.file = file_name
        self.data = None

    def load_data(self):
        """A method that loads the file given as a class parameter into class instance self.data"""
        with open(self.file,'r') as f:
            data = json.load(f)
            self.data = data

    def calculate_mean(self):
        """A method that takes data from class instance self.data and calculate arithmatic mean on that data"""
        data = self.data
        x_values = data['x'].copy() #copied x values of data
        y_values = data['y'].copy() #copied frequencies of those x values
        summation = sum(y_values) #calculate total frequencies
        empty_list = []
        active = True
        while active:        #this whole loop takes up an x value multiply it -
            x = x_values[0]  # - with its frequency and then append that value into an empty list
            x *= y_values[0]
            empty_list.append(x)
            y_values = y_values[1:]
            x_values = x_values[1:]
            if len(y_values) == 0:
                active = False
        frequency_x_value = sum(empty_list)

        mean = frequency_x_value / summation #formula of arithmatic mean
        print(mean)

    def cummulative_frequency(self):
        """A method that calculates cumulative frequency of a dataset """
        data = self.data
        print(data)
        y_values = data['y'].copy()
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
        print(data)
        return cumla_fre

    def relative_frequency(self):
        data = self.data
        print(data)
        y_values = data['y'].copy()
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

    def clsnclsint(self):
        data = self.data
        x_values = data['x'].copy()
        y_values = data['y'].copy()
        lengthx = sum(y_values)
        clses = math.ceil(1 + 3.22 * math.log10(lengthx))
        print(clses)
        list_s = self.make_lists(clses)
        print(list_s)
        maxi , mini = max(x_values) , min(x_values)
        addup = maxi + mini
        clsint = round(addup / clses)
        copclsint = clsint

        starto = 0
        active = True
        while active:
            class01 = list_s[starto]
            class01.append(mini - clsint) , class01.append(mini)
            starto += 1
            mini += clsint
            print(clses)
            if starto == clses:
                active = False
            else:
                continue
        #return list_s
        upper_lowerboundary = []
        for x in list_s:
            upper_lowerboundary.append(x)
        clsses = dict(zip(x_values,upper_lowerboundary))
        return clsses , copclsint

    def median(self):
        data = self.data
        x_values = data['x'].copy()
        y_values = data['y'].copy()
        lengthy = len(y_values) + 1
        med = math.ceil(lengthy/2) - 1
        cumfre = self.cummulative_frequency()
        return cumfre[med]

    def interpolation_formula(self,m,k):
        data = self.data
        x_values = data['x'].copy()
        y_values = data['y'].copy()
        n = sum(y_values)
        cumfre = self.cummulative_frequency()
        pos = n/k
        pos *= m
        copypos = pos
        math.ceil(pos)
        emp = []
        emp2 = []
        for x in cumfre:
            if x < pos:
                emp.append(x)
        for x in x_values:
            if x > pos:
                emp2.append(x)

        freofcurrentclass0 = min(emp2)
        dictfre = self.valuesnfredict()
        freofcurrentclass = dictfre[freofcurrentclass0]
        precumfre = max(emp)
        cls_rtn = self.clsnclsint()
        returned_dict = cls_rtn[0]
        returned_list = returned_dict[4]
        lower_boundry = returned_list[0]
        class_width = cls_rtn[1]

        return copypos , lower_boundry , class_width , freofcurrentclass , precumfre

    def valuesnfredict(self):
        data = self.data
        x_values = data['x']
        y_values = data['y']
        return dict(zip(x_values,y_values))

    def make_lists(self,n):
        return tuple([] for _ in range(n))


if __name__ == '__main__':
    statss = StatsCalculator('data.json')
    data('data.json',[2,4,6,8],[1,1,2,1])
    statss.load_data()
    statss.calculate_mean()
    #print(statss.cummulative_frequency())
    #print(statss.__dict__)
    #statss.relative_frequency()
    #statss.returns_nlists(3)
    #print(statss.clsnclsint())
    #print(statss.median())
    #sort_data([1000,2000,1000,1100,1100,1100,2000,1000,2000,2000])
    #inputsdata('data2.json',[1000,2000,1000,1100,1100,1100,2000,1000,2000,2000])
    #print(statss.interpolation_formula(1,2))

