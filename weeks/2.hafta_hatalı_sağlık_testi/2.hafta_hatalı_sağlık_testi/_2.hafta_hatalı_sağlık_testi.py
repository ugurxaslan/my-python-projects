
#hatalı pozitif ölçer
nufus = 1000000
test_hata = 1/100
gorulme_orani = 1/1000
hasta = nufus * gorulme_orani
saglikli = nufus - hasta
test_hasta = hasta + saglikli*test_hata
test_saglikli = saglikli - test_hasta

gercek = hasta/ test_hasta

print("hasta sayisi : ",format(hasta, ","))
print("saglikli sayisi : ",format(saglikli, ","))
print("test hasta sayisi : ",format(test_hasta, ","))
print("test saglikli sayisi : ",format(test_saglikli, ","))
print("gercekten hasta olma orani : ", gercek)


