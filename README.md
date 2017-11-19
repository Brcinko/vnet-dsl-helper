# vnet-dsl-helper
XML Request Helper tool for requesting DSL lines from telekom


# Preanalysis
Frontend

1. Screena vyber produktu
2. Screena - vyber ziadosti - zriadenie/prekladka/zrusenie DSL
3. Screena - zadavanie hodnot
4. Screena - nacitanie hodnot z XML do sytemu - zistit co a ako treba
5. Screena - zoznam aktualnych vytvorenych ziadosti v subore


Backend

1. Serializer - dictionary->xml
2. Deserializer - xml->dictionary - OPTIONAL zatial
3. Sablona XML pre kazdy produkt a ziadost
	- samostatne priecinky pre rozne typy ziadosti napriklad
4. Server pre API - Flask idealne

Mimo beta verzie by bolo vhodne mat uz aj databazu, kde si budem ukladat vsetky vytvorene XML a mozno aj user mgnmt.


Spravime to ako s DB?
    - vsetky ziadosti sa budu ukladat do db(z nej asi zaloha)
    - zaroven sa moze vygenerovat xml a pastnut sa moze do suboru - KONZISTENCIA?
    - cize by som mohol spravit portal, kde by bol "admin" pristup a mohol by som vidiet vsetky ziadosti
    - vedelo by to napriklad vyplut vsetky lokality, ktore sme odoslali - moze pomocot pri zadavani novych adries
