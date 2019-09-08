from crawler import *
def comparison(actor1,actor2):
    list1=set(movie_list(actor1))
    list2=set(movie_list(actor2))
    combined_list=[list1 & list2]
    return combined_list
actor_1 = input('first actor: ')
actor_2 =  input('second acor: ')
print(comparison(actor_1,actor_2))
