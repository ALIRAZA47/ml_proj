import random


# helping funcs
def DecToBin(n):
    old_n =n
    a=[]
    while(n>0):
        dig=n%2
        a.append(dig)
        n=n//2
    a.reverse()
    if len(a) == 0:
        a.append(0)
    elif old_n < 0:
        a.insert(0, 1)
    elif old_n > 0:
        a.insert(0, 0)
    return a
def BinToDec(binNum):
    # print(binNum)
    sign_bit = binNum[0]
    binNum[0] = 0
    res = int("".join(str(x) for x in binNum), 2)
    if sign_bit == 1:
        res = res*(-1)
    elif sign_bit == 0:
        res = res * 1    
    return res 
class ANN:
    def __init__(self):
        pass
    def inp_neuron(self, w1, w2, w3, i1, i2):
        o1 = (w1*i1) + (w2*i2) + (w3*1)
        if o1 >= 0:
            return 1
        elif o1 < 0:
            return 0    
    def out_neuron(self, w1, w2,w3, i1, i2):
        out = (w1*i1) + (w2*i2) + (w3*1)
        if out >= 0:
            return 1
        elif out < 0:
            return 0          
    def init_ann(self, weights, inp1, inp2, desOut):
        out_neuron1 = self.inp_neuron(weights[0], weights[1], weights[2], inp1, inp2)
        out_neuron2 = self.inp_neuron(weights[3], weights[4], weights[5], inp1, inp2)
        self.err_count = 0
        actual_out = self.out_neuron(weights[6], weights[7], weights[8], out_neuron1, out_neuron2)
        return actual_out 
    def cmp_act_des(self, des, actual): #compare desired and actual output
        if des == actual:
            return True
        else:
            return False
class EvoAlgo(ANN):
    def __init__(self):
        self.population = [[0]*9 for _ in range(30)]
        self.success_perc_dict = {}
        self.trainInput = [[1,1],[9.4,6.4],[2.5,2.1],[8,7.7],[0.5,2.2],[7.9,8.4],[7,7],[2.8,0.8],[1.2,3],[7.8,6.1]]
        self.trainOutput = [1, -1, 1, -1, -1, 1, -1, 1, -1, -1]
        self.initPopulation()
    def initPopulation(self):
        for i in range(30):
            for j in range(9):
                rndm_num = random.randint(-10, 10)
                self.population[i][j] = rndm_num
        # print(self.population)
    def testRandWeights(self):
        # print(self.population)
        weights_with_errRate = {}
        for weights in self.population:
            success_count = 0
            for i in range(len(self.trainInput)):
                ann_val = self.init_ann(weights, self.trainInput[i][0], self.trainInput[i][1], self.trainOutput[i])
                if self.cmp_act_des(self.trainOutput[i], ann_val):
                    success_count +=1
            success_perc = (success_count / 10) * 100
            self.success_perc_dict[weights[0],weights[1],weights[2], weights[3], weights[4], weights[5], weights[6], weights[7], weights[8]] = success_perc
    def fit_eval(self, unsort_dict):
        # print(unsort_dict)
        sorted_population = []
        sort_pop = sorted(unsort_dict.items(), key=lambda x:x[1])
        sort_dict = dict(sort_pop)
        i = 0
        for key in sort_dict.keys():
            sorted_population.append(list(key))
        sorted_population.reverse()
        best_weights = sorted_population[0]
        # print(unsort_dict[best_weights])
        return sorted_population    
    def crossover_mutation(self, sortedList):
        self.population.clear()
        print("\n\n")
        # print(sortedList)
        sortedList = list(sortedList)
        iteri = 0
        while iteri < 30:
            neu_11 =[]
            neu_12 =[]
            neu_13 =[]
            neu_21 =[]
            neu_22 =[]
            neu_23 =[]
            # print(sortedList[iteri][0])
            w111 = sortedList[iteri][0]
            w112 = sortedList[iteri][1]
            w113 = sortedList[iteri][2]
            w121 = sortedList[iteri][3]
            w122 = sortedList[iteri][4]
            w123 = sortedList[iteri][5]
            w131 = sortedList[iteri][6]
            w132 = sortedList[iteri][7]
            w133 = sortedList[iteri][8]
            # weights of second list
            w211 = sortedList[iteri+1][0]
            w212 = sortedList[iteri+1][1]
            w213 = sortedList[iteri+1][2]
            w221 = sortedList[iteri+1][3]
            w222 = sortedList[iteri+1][4]
            w223 = sortedList[iteri+1][5]
            w231 = sortedList[iteri+1][6]
            w232 = sortedList[iteri+1][7]
            w233 = sortedList[iteri+1][8]
            # incer the iter
            iteri += 2
            w111Bin = DecToBin(w111)
            w112Bin = DecToBin(w112)
            w113Bin = DecToBin(w113)
            w121Bin = DecToBin(w121)
            w122Bin = DecToBin(w122)
            w123Bin = DecToBin(w123)
            w131Bin = DecToBin(w131)
            w132Bin = DecToBin(w132)
            w133Bin = DecToBin(w133)
            w211Bin = DecToBin(w211)
            w212Bin = DecToBin(w212)
            w213Bin = DecToBin(w213)
            w221Bin = DecToBin(w221)
            w222Bin = DecToBin(w222)
            w223Bin = DecToBin(w223)
            w231Bin = DecToBin(w231)
            w232Bin = DecToBin(w232)
            w233Bin = DecToBin(w233)
            l111 = len(w111Bin)
            l112 = len(w112Bin)
            l113 = len(w113Bin)
            l121 = len(w121Bin)
            l122 = len(w122Bin)
            l123 = len(w123Bin)
            l131 = len(w131Bin)
            l132 = len(w132Bin)
            l133 = len(w133Bin)
            l211 = len(w211Bin)
            l212 = len(w212Bin)
            l213 = len(w213Bin)
            l221 = len(w221Bin)
            l222 = len(w222Bin)
            l223 = len(w223Bin)
            l231 = len(w231Bin)
            l232 = len(w232Bin)
            l233 = len(w233Bin)
            # Now Joining
            # print(w111Bin)
            # print(w112)
            neu_11.extend(w111Bin)
            neu_11.extend(w112Bin)
            neu_11.extend(w113Bin)
            neu_12.extend(w121Bin)
            neu_12.extend(w122Bin)
            neu_12.extend(w123Bin)
            neu_13.extend(w131Bin)
            neu_13.extend(w132Bin)
            neu_13.extend(w133Bin)
            
            neu_21.extend(w111Bin)
            neu_21.extend(w212Bin)
            neu_21.extend(w213Bin)
            neu_22.extend(w221Bin)
            neu_22.extend(w222Bin)
            neu_22.extend(w223Bin)
            neu_23.extend(w231Bin)
            neu_23.extend(w232Bin)
            neu_23.extend(w233Bin)
            # neuron 1 balancing
            if len(neu_11) > len(neu_21):
                for i in range(len(neu_11) - len(neu_21)):
                    neu_21.insert(0,0)
            else:
                for i in range(len(neu_21) - len(neu_11)):
                    neu_11.insert(0,0)
            # neuron 2 balancing
            if len(neu_12) > len(neu_22):
                for i in range(len(neu_12) - len(neu_22)):
                    neu_22.insert(0,0)
            else:
                for i in range(len(neu_22) - len(neu_12)):
                    neu_12.insert(0,0)
            # neuron 3 balancing
            if len(neu_13) > len(neu_23):
                for i in range(len(neu_13) - len(neu_23)):
                    neu_23.insert(0,0)
            else:
                for i in range(len(neu_23) - len(neu_13)):
                    neu_13.insert(0,0)                                
            # now crossover neuron 1
            neu_11.reverse()
            neu_21.reverse()
            rand_cut = random.randint(0, (len(neu_11) -1))
            for i in range(0, rand_cut):
                neu_11[i], neu_21[i] = neu_21[i], neu_11[i]
            neu_11.reverse()
            neu_21.reverse()    
            # now crossover of neuron 2 
            neu_12.reverse()
            neu_22.reverse()
            rand_cut = random.randint(0, (len(neu_11) -1))
            for i in range(0, rand_cut):
                neu_12[i], neu_22[i] = neu_22[i], neu_12[i]
            neu_12.reverse()
            neu_22.reverse()    
            # now crossover of neuron 2 
            neu_13.reverse()
            neu_23.reverse()
            rand_cut = random.randint(0, (len(neu_11) -1))
            for i in range(0, rand_cut):
                neu_13[i], neu_23[i] = neu_23[i], neu_13[i] 
            neu_13.reverse()
            neu_23.reverse()           
            
            # Now mutation
            rand_mut = random.randint(0, len(neu_11) - 1)
            if neu_11[rand_mut] == 1:
                neu_11[rand_mut] == 0
            else:
                neu_11[rand_mut]=0
            if neu_12[rand_mut] == 1:
                neu_12[rand_mut] == 0
            else:
                neu_12[rand_mut]=0
            if neu_13[rand_mut] == 1:
                neu_13[rand_mut] == 0
            else:
                neu_13[rand_mut]=0
            ...
            if neu_21[rand_mut] == 1:
                neu_21[rand_mut] == 0
            else:
                neu_21[rand_mut]=0
            if neu_22[rand_mut] == 1:
                neu_22[rand_mut] == 0
            else:
                neu_22[rand_mut]=0
            if neu_23[rand_mut] == 1:
                neu_23[rand_mut] == 0
            else:
                neu_13[rand_mut]=0

            # now converting numbers back to decimal weights
            # print(neu_11)
            print(neu_22)
            w111Bin.clear()
            w112Bin.clear()
            w113Bin.clear()
            w121Bin.clear()
            w122Bin.clear()
            w123Bin.clear()
            w131Bin.clear()
            w132Bin.clear()
            w133Bin.clear()
            w211Bin.clear()
            w212Bin.clear()
            w213Bin.clear()
            w221Bin.clear()
            w222Bin.clear()
            w223Bin.clear()
            w231Bin.clear()
            w232Bin.clear()
            w233Bin.clear()
            # print(neu_11)
            # print(neu_22)
            for i in range(l113):
                popi = neu_11.pop()
                w113Bin.append(popi)
            for i in range(l112):
                popi = neu_11.pop()
                w112Bin.append(popi)
            w111Bin = neu_11
            for i in range(l123):
                popi = neu_12.pop()
                w123Bin.append(popi)
            for i in range(l112):
                popi = neu_12.pop()
                w122Bin.append(popi)
            w121Bin = neu_12 
            for i in range(l133):
                popi = neu_13.pop()
                w133Bin.append(popi)
            for i in range(l112):
                popi = neu_13.pop()
                w132Bin.append(popi)
            w131Bin = neu_13
            # ..
            for i in range(l213):
                popi = neu_21.pop()
                w213Bin.append(popi)
            for i in range(l212):
                popi = neu_21.pop()
                w212Bin.append(popi)
            w211Bin = neu_21
            for i in range(l223):
                popi = neu_22.pop()
                w223Bin.append(popi)
            for i in range(l212):
                popi = neu_22.pop()
                w222Bin.append(popi)
            w221Bin = neu_22 
            for i in range(l233):
                popi = neu_23.pop()
                w233Bin.append(popi)
            for i in range(l212):
                popi = neu_23.pop()
                w232Bin.append(popi)
            w231Bin = neu_23
            # converting binary digits back to decimal
            w111 = BinToDec(w111Bin)
            w112 = BinToDec(w112Bin)
            w113 = BinToDec(w113Bin)
            w121 = BinToDec(w121Bin)
            w122 = BinToDec(w122Bin)
            w123 = BinToDec(w123Bin)
            w131 = BinToDec(w131Bin)
            w132 = BinToDec(w132Bin)
            w133 = BinToDec(w133Bin)
            w211 = BinToDec(w211Bin)
            w212 = BinToDec(w212Bin)
            w213 = BinToDec(w213Bin)
            w221 = BinToDec(w221Bin)
            w222 = BinToDec(w222Bin)
            w223 = BinToDec(w223Bin)
            w231 = BinToDec(w231Bin)
            w232 = BinToDec(w232Bin)
            w233 = BinToDec(w233Bin)
            print(w111Bin)
            new_weights = [w111, w112, w113, w121, w122, w123, w131, w132, w133]
            new_weights2 = [w211, w212, w213, w221, w222, w223, w231, w232, w233]
            print(new_weights2, new_weights)
            self.population.append(new_weights)
            self.population.append(new_weights2)

                            
    def main(self):
        threshooo = 100
        best_fit = 0
        i=0
        while i <2:
            self.testRandWeights()
            a=self.fit_eval(self.success_perc_dict)
            self.crossover_mutation(a)  
            i+=1

                
# Test code

a = EvoAlgo()
a.main()




