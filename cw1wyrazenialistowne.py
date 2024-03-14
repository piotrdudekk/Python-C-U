liczby = [1,2,3,4,5,6,7,8]

liczbyDoPotegi2 = [element**2
                   for element in liczby
                   ]

#liczby od 0 do 1000 co 3, podzielne przez 5 i 7
podzielne5i7 = [element
                for element in range(0,1000,3)
                if (element % 5 == 0 and element % 7 == 0)
                ]
