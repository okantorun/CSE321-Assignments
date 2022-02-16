def  bruteForce(letters,start,end):
    count = 0
    for i in range(0,len(letters)):
        for j in range(i+1,len(letters)):
            if(letters[i] != start):
                break
            else:
                if(letters[j] == end):
                    count=count+1
    return count

letters = " TXZXXJZWX"
start='X';
end ='Z';
print((bruteForce(letters, start, end)))