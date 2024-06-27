import matplotlib.pyplot as plt
country=['US','China','Japan','Britain','ROC','Australia','Netherland','France','Germany','Italy']
gold=[39,38,27,22,20,17,10,10,10,10]
silver=[41,32,14,21,28,7,12,12,11,10]
brownz=[33,18,17,22,23,22,14,11,16,20]
plt.plot(country,gold,marker='o')
plt.plot(country,silver,marker='o')
plt.plot(country,brownz,marker='o')
plt.xlabel("COUNTRIES")
plt.ylabel("Number of Medals")
plt.title("MEDALS")
plt.suptitle("TOKOYO 2020 OLYMPIC")
plt.legend(["gold","silver","brownz"])
plt.show()
