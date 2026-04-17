people = ['Dr. Christopher Brooker', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(people):
    newpeople = []
    for p in people:
        x = p.split()
        newpeople.append(x[0] +" "+ x[-1])
    return newpeople


result = split_title_and_name(people)
print (result)


#foo = list(map(split_title_and_name, people))
#print(foo)









#list(map(split_title_and_name, newpeople))