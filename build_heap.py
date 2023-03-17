# python3

import os
#indexMas = []
swaps = []

def build_heap(data):
    #swaps = []
    #count = 0
    for elementIndex in range(len(data) - 1, -1, -1):
        sort(data, elementIndex)
    #rootIndex = data.index(min(data))
    #middleIndex = (len(data) - 1)/2
    #print(rootIndex)
    #for i in enumerate(data):
    #swaps.append(count)
    
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    #return swaps

def sort(data, elementIndex):
    minEl = elementIndex 
    leftEl = 2 * elementIndex + 1  
    rightEl = 2 * elementIndex + 2 

    if leftEl < len(data) and data[elementIndex] > data[leftEl]:
        minEl = leftEl


    if rightEl < len(data) and data[minEl] > data[rightEl]:
        minEl = rightEl

    if minEl != elementIndex:
        data[elementIndex],data[minEl] = data[minEl],data[elementIndex]
        #count = count + 1
        swaps.append([elementIndex, minEl])
        #swaps.append(minEl)
        sort(data, minEl)


def main():
    
    check = input()
    check = check.replace("\r","")
    check = check.replace("\n","")
    if check == 'I':
        n = int(input())
        if n < 1 and n > 100000:
            print("error")
            quit()
        data = list(map(int, input().split()))
        assert len(data) == n
        build_heap(data)

    if check == 'F':
        path = os.getcwd() + '/tests'
        os.chdir(path)
        file_name = input()
        if 'a' in file_name:
            print("error")
            quit()        
        else:
            file_path = f"{path}/{file_name}"
            with open(file_path, "r", encoding="utf-8-sig") as f:
                newLines = f.readlines()
                n = int(newLines[0].replace("\n", ""))
                if n < 1 and n > 100000:
                    print("error")
                    quit()
                data = newLines[1].replace("\n", "").split()
                data = [int(i) for i in data] 
                assert len(data) == n
            build_heap(data)


    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    #n = int(input())
    #data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    #assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    #build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
