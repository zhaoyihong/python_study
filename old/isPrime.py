# -*- coding:utf8 -*-
# 在此输入你的代码

import math
 
def isPrime(n):
    if n%2 == 0 and n>2:
        return False

    for i in range(3,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    
    return True
                             
print isPrime(4),isPrime(100),isPrime(11)
                                                                                                                            
                                                                                                                                               
                                                                                                                                                               
                                                                                                                                                                            
