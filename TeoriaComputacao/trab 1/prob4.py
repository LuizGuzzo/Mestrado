"""
#Sequencia testada - resultado

000 - 0
001 - 0
010 - 0
011 - 1
100 - 0
101 - 1
110 - 1
111 - 1

#Codigo executado no Lambster:

alt = La b c.(a (b true (c true false) ) (b c false) )

alt false false false 
alt false false true  
alt false true false  

alt false true true   
alt true false false  
alt true false true   

alt true true false   
alt true true true    


# execução do lambster e resultado
# 1 e 0 da questão corresponde a "true" e "false" do proprio lambster, por isso que utilizei os nomes "true" e "false" na função ALT

lambster: A lambda calculus interpreter
version 1.0.6 -- type 'help' for more information
λ> alt = La b c.(a (b true (c true false) ) (b c false) )
>>> alt = (λa. (λb. (λc. ((a ((b (λt. (λf. t))) ((c (λt. (λf. t))) (λt. (λf. f))))) ((b c) (λt. (λf. f)))))))
λ> alt false false false
>>> (λt. (λf. f))
    ↳ equivalent to: false, zero
λ> alt false false true
>>> (λt. (λf. f))
    ↳ equivalent to: false, zero
λ> alt false true false
>>> (λt. (λf. f))
    ↳ equivalent to: false, zero
λ> alt false true true
>>> (λt. (λf. t))
    ↳ equivalent to: true
λ> alt true false false
>>> (λt. (λf. f))
    ↳ equivalent to: false, zero
λ> alt true false true
>>> (λt. (λf. t))
    ↳ equivalent to: true
λ> alt true true false
>>> (λt. (λf. t))
    ↳ equivalent to: true
λ> alt true true true
>>> (λt. (λf. t))
    ↳ equivalent to: true

"""