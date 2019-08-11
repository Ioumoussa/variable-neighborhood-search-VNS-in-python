import random
import time

def calcul_fonction(l):
    somme_des_periodes = 0
    somme_wt = 0
    for i in l:
        somme_des_periodes += les_periodes[i-1]
        somme_wt += (les_weights[i-1] * max(0, (somme_des_periodes - les_due_dates[i-1])))

    return somme_wt


def random_list_from_list(L):
    lenL = len(L)
    i = random.randint(0, lenL-1)
    return L[i]

def tuple_not_exists(list, t):
    for elm in list:
        if elm == t:
            return False
    return True
//
def shaking(L, k):
    resultat_swap = []
    resultat_inversion = []
    resultat_left_pivot = []
 #shaking par swap
    if k == 1:
        randomIndice = []
        while len(resultat_swap) < 5:
            i=0
            j=0
            while True:
                i = random.randint(0, len(L)-1)
                j = random.randint(0, len(L)-1)
                if(i!=j and tuple_not_exists(randomIndice, (i, j))):
                    break

            randomIndice.append((i, j))
            randomIndice.append((j, i))
            list1 = [] + L
            list1[i], list1[j] = list1[j], list1[i]
            resultat_swap.append(list1)
        return  resultat_swap
       # shaking par inversion
    if k == 2:
        randomIndice = []
        while len(resultat_inversion) < 5:
            i=j=0
            while True:
                i = random.randint(0, len(L)-1)
                j = random.randint(0, len(L)-1)
                if(i!=j and tuple_not_exists(randomIndice, (i, j)) and abs(j - i) > 4):
                    break
                randomIndice.append((i, j))
                randomIndice.append((j, i))
                list2 = [] + L
                list2[i:j+1] = reversed(list2[i: j+1])
                resultat_inversion.append(list2)
        return resultat_inversion
    # shaking avec left pivot
    if k == 3:
         i = 0
         while len(resultat_left_pivot) <= 5 :
             list3 = [] + L
             i = random.randint(0, len(L)-1)
             list3[:i+1] = reversed(list3[:i+1])
             resultat_left_pivot.append(list3)
         return resultat_left_pivot
    return []

somme =0

les_taches = list(range(1,101))
les_periodes = []

for i in range(1,101):
    x = random.randint(1,100)
    les_periodes.append(x)


les_weights = []
for j in range(1,101):
    y = random.randint(1,10)
    les_weights.append(y)

for elem in les_periodes:
    somme += elem

inf = int(0.2 * somme)
sup = int(0.6 * somme)

les_due_dates = []
for k in range(1,101):
    z = random.randint(inf,sup)
    les_due_dates.append(z)


print("les taches")
print(les_taches)
print("les Periodes")
print(les_periodes)
print("les weights")
print(les_weights)
print("les Due Date")
print(les_due_dates)

somme_wt= 0
soome_des_periodes = 0

# pour la condition du temps


run_time = time.time()+10
x_ = 0
x_list = 0
x_prime = 0
x_prime_list = 0
x_second = 0
while time.time() <= run_time :
    #A
    x_ = calcul_fonction(les_taches)
    x_list = les_taches
    k=1
    Kmax = 4
    variable = 0
    local_optimum_better_inqumbent = False
    while k != Kmax :
         #on stock la liste de
         x_prime_list = random_list_from_list(shaking(x_list,k))

         if local_optimum_better_inqumbent:
            x_prime_list = variable
         x_prime = calcul_fonction(x_prime_list)
            #B
         l = 1
         Lmax = 4
         while l != Lmax:
              liste_générer_par_insertion = shaking(x_prime_list,l)
              local = (0, 1000000000)
              j = 0
              for elem in liste_générer_par_insertion:
                  val = calcul_fonction(elem)
                  if local[1] > val:
                      local = (j, val)
                  j+=1
              x_second = local[1]

              if (x_second < x_prime) :
                  # on stock la valeur de x_second
                  x_prime = x_second
                  # on stock la sequence de x_second
                  x_prime_list = liste_générer_par_insertion[local[0]]
                  l = 1
              else:
                  l += 1
         #C

         if x_prime < x_:
             x_ = x_prime
             x_list = x_prime_list
             k = 1
             variable = x_prime_list
             local_optimum_better_inqumbent = True
         else:
             k += 1
             local_optimum_better_inqumbent = False



print( " le meilleur voisinage est : ")
print( x_list)
print("sa valeur est : ")
print(x_)
