#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            dividend = my_list_1[i]
            divisor = my_list_2[i]
            
            if type(dividend) not in (int, float) or type(divisor) not in (int, float):
                raise TypeError("wrong type")

            if divisor == 0:
                raise ZeroDivisionError("division by 0")

            result.append(dividend / divisor)
        
        except IndexError:
            print("out of range")
            result.append(0)
        except (TypeError, ZeroDivisionError) as e:
            print(e)
            result.append(0)
    
    return result
