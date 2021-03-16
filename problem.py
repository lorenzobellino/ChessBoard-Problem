import random


N = 4
board = []
key = []
def setup():
    for i in range(N):
        row=[]
        for j in range(N):
            row.append(random.randrange(0,2))
        board.append(row)

if __name__ == "__main__":
    setup()
    while(len(key) <2 or len(key) >2):
        key = []
        print("enter key position as a tuple row,col")
        try:
            for i in input().split(","): key.append(int(i))
            if(key[0]>=N or key[1]>=N or key[0]<0 or ky[1]<0):
                print('value permitted are between 0 and ',N)
                key = []
            else:
                break
        except:
            print("you must enter the digits in that specific form")
    print(key)
