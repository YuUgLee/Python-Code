def integer_to_reverse_binary(x):
    y=''
    while x>0:
        y+=str(x%2)
        x=x//2
    return reverse_string(y)

def reverse_string(input_string):
    num=''
    i=len(input_string)-1
    while i >=0:
        num+=input_string[i]
        i=i-1
    return num

if __name__ == '__main__':
    user=int(input())
    print(integer_to_reverse_binary(user))

