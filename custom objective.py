from keras.models import Sequential
from keras.layers import Dense
import numpy as np

width = 800
height = 800

def custom_objective(y_true, y_pred):
    inx = ( a for a,b in y_true )
    innum = ( b for a,b in y_true )
    roveravg = 2
    distavg = 20
    return (1/roveravg-1/distavg)*(np.random.randint(0,10))

def nums():
    x = np.random.randint(1,100)
    y = np.random.randint(1,10000)
    z = x*y
    return ([x,y,z])

nums = nums()

def neuralnet(number):
    # create model
    model = Sequential()
    model.add(Dense(2, input_dim=1, activation='relu'))
    model.add(Dense(20, activation='relu'))
    model.add(Dense(20, activation='relu'))
    model.add(Dense(1, activation='relu'))

    #input number and i
    r = []
    number = [number]*360
    i = list((range(361)))
    del i[0]
    number = list(zip(number,i))
    print(number)
    r = r.append(max(0,model.predict(number,360)))
    model.compile(optimizer='adam',loss=custom_objective(number,r))
    print(Y_train.shape)
    #r = r.append(max(0,model.predict(number,360)))
    #r = [0]*360
    #r.append(max(0,number))
    print(r)
    return np.asarray(r)

def rotationnet(number):
    #input x, y
    roll = 0
    return roll

def shapes(number,numnum):
    r = neuralnet(number)
    pos = (width/4)*numnum
    x = [round(r*np.cos(np.deg2rad(i))+pos) for i, r in enumerate(r)]
    y = [round(r*np.sin(np.deg2rad(i))+pos) for i, r in enumerate(r)]
    return list(zip(x, y))

def detectpoints():
    xr = shapes(nums[0],1)
    zr = shapes(nums[2],2)
    yr = shapes(nums[1],3)
    print(zr)

detectpoints()
