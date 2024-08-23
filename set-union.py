def list_to_set(list1):
    set1 = set()
    for num in list1:
        set1.add(num)
    return set1

def main():
    n=input()
    s1=input()
    b=input()
    s2=input()
    list1=s1.split(" ")
    list2=s2.split(" ")
    set1=list_to_set(list1)
    set2 = list_to_set(list2)
    myset=set1.union(set2)
    print(len(set1)+len(set2)-len(myset))

if __name__ == "__main__":
    main()