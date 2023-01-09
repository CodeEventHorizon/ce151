##########################################
## CE151 ASSIGNMENT 1: DO NOT REMOVE    ##
##########################################
import unittest
##########################################
## CE151 ASSIGNMENT 1: DO NOT REMOVE    ##
##########################################

#### Exercise 1
def fun_exercise_1(x,y):
    if x==0:
        return sum(y)
    elif x%2 == 1:
        for i in range(len(y)):
            y[i]-=1
        return sum(y)
    elif x%2 == 0:
        for i in range(len(y)):
            y[i]*=2
        return sum(y)
#### Exercise 2
def fun_exercise_2(y):
    if y[0]%2 == 1:
        prod = 1
        for i in range(len(y)):
            y[i] *= 2
            prod *= y[i]
        return prod
    elif y[2]%2 == 1:
        for i in range(len(y)):
            y[i] /= 2
        return sum(y)
    else:
        for i in range(len(y)):
            y[i] **= 2
        return sum(y)

#### Exercise 3
def fun_exercise_3(y):
    z = []
    for i in range(int(len(y)/2)):
        if y[-i-1] < y[i]:
            z.append(True)
        else:
            z.append(False)
    return z
        

#### Exercise 4
def fun_exercise_4(y):
    if len(y)>=5:
        y.sort()
        return y[-3]
    elif len(y)<5 and len(y)!=0 and len(y)!=3:
        y.sort()
        return y[-1]
    elif len(y) == 3 or len(y)!=0:
        y.sort()
        return y[-2]
    else:
        return None

#### Exercise 5
def fun_exercise_5(x):
    if x.lower() == x.lower()[::-1]:
        return False
    else:
        return True

#### Exercise 6
def fun_exercise_6(x):
    a1="abcdefghijkl"
    a2="mnopqrstuvwxyz"
    for i in range(len(x)):
        if x[i].lower() in a1:
            x = x[:i] + x[i].lower() + x[i+1:]
        elif x[i].lower() in a2:
            x = x[:i] + x[i].upper() + x[i+1:]
    y = x
    return y

#### Exercise 7
def fun_exercise_7(x):
    ptr = -1
    if len(x) <= 1:
        return ptr
    for i in range(len(x)):
        for j in range(len(x)):
            if i == j:
                continue
            elif x[i] in x[j]:
                ptr = i
                return ptr
    return ptr
            
    

#### Exercise 8
def fun_exercise_8(x):
    d={}
    for i in x:
        d[i] = d.get(i,0)+1
    return i
    
        
    
    
        
##############################################
## BEGIN: CE151 TEST CODE: DO NOT REMOVE    ##
##############################################
class TestAssignment1(unittest.TestCase):

#function 1
    def test1_exercise_1(self):
        self.assertTrue(fun_exercise_1(3,[4,2,3]) == 6)

    def test2_exercise_1(self):
        self.assertTrue(fun_exercise_1(2,[2,3,4]) == 18)

    def test3_exercise_1(self):
        self.assertTrue(fun_exercise_1(0,[5,3,2]) == 10)

    def test4_exercise_1(self):
        self.assertTrue(fun_exercise_1(3,[1,1,1]) == 0)

#function 2
    def test1_exercise_2(self):
        self.assertTrue(fun_exercise_2([3, 2, 4]) == 192)

    def test2_exercise_2(self):
        self.assertTrue(fun_exercise_2([6, 2, 3]) == 5.5)

    def test3_exercise_2(self):
        self.assertTrue(fun_exercise_2([6, 5, 4]) == 77)

    def test4_exercise_2(self):
        self.assertTrue(fun_exercise_2([1, 2, 3]) == 48)

#function 3 *****
    def test1_exercise_3(self):
        self.assertTrue(fun_exercise_3([2, 3, 4, 5, 6, 7]) ==[False, False,False])

    def test2_exercise_3(self):
        self.assertTrue(fun_exercise_3([6, 4, 3, 2, 1, 0]) == [True,True,True])

    def test3_exercise_3(self):
        self.assertTrue(fun_exercise_3([6, 5, 4, 2]) == [True, True])

    def test4_exercise_3(self):
        self.assertTrue(fun_exercise_3([1, 2, 3, 4]) == [False, False])

#function 4
    def test1_exercise_4(self):
        self.assertTrue(fun_exercise_4([5, 3, 4, 2 , 6]) == 4)

    def test2_exercise_4(self):
        self.assertTrue(fun_exercise_4([3, 2, 6]) == 3)

    def test3_exercise_4(self):
        self.assertTrue(fun_exercise_4([]) == None)

    def test4_exercise_4(self):
        self.assertTrue(fun_exercise_4([2, 3, 4, 7, 6, 5]) == 5 )

#function 5
    def test1_exercise_5(self):
        self.assertTrue(fun_exercise_5("osso") == False)

    def test2_exercise_5(self):
        self.assertTrue(fun_exercise_5("goat") == True)

    def test3_exercise_5(self):
        self.assertTrue(fun_exercise_5("Mom") == False)

    def test4_exercise_5(self):
        self.assertTrue(fun_exercise_5("boat") == True )

#function 6
    def test1_exercise_6(self):
        self.assertTrue(fun_exercise_6("osso") == "OSSO")

    def test2_exercise_6(self):
        self.assertTrue(fun_exercise_6("goat") == "gOaT")

    def test3_exercise_6(self):
        self.assertTrue(fun_exercise_6("bag") == "bag")

    def test4_exercise_6(self):
        self.assertTrue(fun_exercise_6("boat") == "bOaT" )

#function 7
    def test1_exercise_7(self):
        list1 = ["goat"]
        ptr = fun_exercise_7(list1)
        self.assertTrue(ptr == -1)

    def test2_exercise_7(self):
        list1 = ["soul", "soulmate", "origin"]
        ptr = fun_exercise_7(list1)
        self.assertTrue(ptr == 0)

    def test3_exercise_7(self):
        list1 = ["FASER", "submission", "online", "drive", "frequent"]
        ptr = fun_exercise_7(list1)
        self.assertTrue(ptr == -1)

    def test4_exercise_7(self):
        list1 = ["banana", "applejuice", "kiwi", "strawberry", "apple", "peer"]
        ptr = fun_exercise_7(list1)
        self.assertTrue(ptr == 4)

    #function 8
    def test1_exercise_8(self):
        self.assertTrue(fun_exercise_8("GTTAAA") == "T")


    def test2_exercise_8(self):
        self.assertTrue(fun_exercise_8("unforeseen") == "n")


    def test3_exercise_8(self):
        self.assertTrue(fun_exercise_8("developed") == "d")


    def test4_exercise_8(self):
        self.assertTrue(fun_exercise_8("circumstances") == "s")

if __name__ == '__main__':
    unittest.main()
##############################################
## END: CE151 TEST CODE: DO NOT REMOVE      ##
##############################################
