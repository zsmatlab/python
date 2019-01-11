import numpy.random as npr

#read trainval file
txt = '/home/jianchao/Desktop/1/train.txt'
with open(txt, 'r') as f:
    lines = f.readlines()
    splitlines = [x.strip().split(' ') for x in lines]

    #shuffle the images
    npr.shuffle(splitlines)


    test = []
    train = []
    #select the first 100 image to test
    for img in range(len(splitlines)):
        if img >= len(splitlines) * 0.2: break
        test.append(splitlines[img][0])
    test = sorted(test, key=lambda x:str(x))

    #select the others to train
    for img in range(len(splitlines)):
        if img < len(splitlines) * 0.2: continue
        train.append(splitlines[img][0])
        train = sorted(train, key=lambda x:str(x))

    #save the test file
    with open('/home/jianchao/Desktop/1/test.txt', 'w') as wt:
        print('write into test')
        for name in range(len(test)):
            wt.write(str(test[name]) + '\n')

    #save the train file
    with open('/home/jianchao/Desktop/1/train1.txt', 'w') as wt:
        print('write into train')
        for name in range(len(train)):
            wt.write(str(train[name]) + '\n')
