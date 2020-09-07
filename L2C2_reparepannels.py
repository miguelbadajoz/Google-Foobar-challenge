# level 2 / Challenge 2
def getPannels(xs):

    def product(array) : 
        result = 1
        for x in array: 
            result = result * x  
        return result  

    # Algunas excepciones:
    if len(xs)==2 and len([num for num in xs if num < 0])==2:
        return str(max(xs))

    # Guardamos el original:
    xs_0 = xs
    # Contamos longitud inicial
    len_0 = len(xs)
    
    # Quitar todos los 0 y 1:
    xs = list(filter(lambda a: a != 0, xs))
    xs = list(filter(lambda a: a != 1, xs))

    candidate = product(xs)

    if (len(xs) == 0) or (len(xs) == 1 and candidate < 0):
        if xs_0.count(1) > 0:
            return str(1)
        elif xs_0.count(0) > 0:
            return str(0)
        else:
            return str(candidate)
        
    if candidate < 0:
        max_neg = max([num for num in xs if num < 0])
        return str(int(candidate / max_neg))

    elif len(xs) == len_0:
        list_pos = [num for num in xs if num > 0]
        list_neg = [num for num in xs if num < 0]

        if len(list_pos) > 0:
            min_pos = min(list_pos)
        if len(list_neg) > 1:
            max_neg_1 = max(list_neg)
            list_neg.remove(max_neg_1)
            max_neg_2 = max(list_neg)

        if len(list_pos)>0 and len(list_neg) > 1:
            if (max_neg_1*max_neg_2) < min_pos:
                return str(int(candidate / (max_neg_1*max_neg_2)))
            else:
                return str(int(candidate / min_pos))
        elif len(list_pos)>0:
            return str(int(candidate / min_pos))
        else:
            return str(int(candidate / (max_neg_1*max_neg_2)))

    else:
        return str(candidate)
