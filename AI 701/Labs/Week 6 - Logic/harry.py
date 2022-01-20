#Credits Brain Yu, David Malan 









from logic import *

#1 . If it didn’t rain, Harry visited Hagrid today.
#2 . Harry visited Hagrid or Dumbledore today, but not both.
#3 . Harry visited Dumbledore today.

# query: is it rained today?


rain = Symbol("rain") # It is raining (R: Rain)
hagrid = Symbol("hagrid") # Harry visited Hagrid (Q: Hagrid)
dumbledore = Symbol("dumbledore") # Harry visited Dumbledore (P: Dumbledore)

knowledge = And(
    Implication(Not(rain), hagrid), # ¬(It is raining) → (Harry visited Hagrid)
    Or(hagrid, dumbledore), # (Harry visited Hagrid) ∨ (Harry visited Dumbledore).
    Not(And(hagrid, dumbledore)), # ¬(Harry visited Hagrid ∧ Harry visited Dumbledore) i.e. Harry did not visit both Hagrid and Dumbledore.
    dumbledore #  Harry visited Dumbledore.
)

print(model_check(knowledge, dumbledore))


