# Enter your code here. Read input from STDIN. Print output to STDOUT
def list_to_set(list1):
    set1 = set()
    for num in list1:
        set1.add(num)
    return set1

def set_sum(myset):
    sum = 0
    for x in myset:
        sum=sum+int(x)
    return sum

def operation(op,set1,set2):
    if op=="update":
        set1.update(set2)
    elif op=="intersection_update":
        set1.intersection_update(set2)
    elif op=="difference_update":
        set1.difference_update(set2)
    elif op=="symmetric_difference_update":
        set1.symmetric_difference_update(set2)
    else:
        print("invalid operation")
    return set1
    
def parse_line(N):
    lines=[]
    for x in range(0,2*N):
        line=input()
        lines.append(line)
        x=x+1
    return lines
    
def parse_op(N,line):
    ops=[]
    for x in range(0,N):
        op=line[2*x].split(" ")[0]
        ops.append(op)
        x=x+1
    return ops
    
def parse_set(N,line):
    mylists=[]
    mysets=[]
    final_set=set()
    for x in range(0,N):
        mylist=line[2*x+1].split(" ")
        myset=list_to_set(mylist)
        mysets.append(myset)
        x=x+1
        
    return mysets
       
        
def main():
    num_of_A=input()
    A=set(input())
    N=int(input())
    line=parse_line(N)
   # print(line)
    ops=parse_op(N,line)
  #  print(ops)
    final_set=parse_set(N,line)
  #  print(final_set)
    for x in range(0,N):
        operation(ops[x],A,final_set[x])
    
   # print(A)
    print(set_sum(A))

if __name__ == "__main__":
    main()