# Zapoctovy-program

Úvod

Rád by som Vám krátko predstavil tematiku môjho zápočtového programu:

1. Výpočet Legendrovho symbolu - je funkcia dvoch premenných A a P definovaná takto:
(A/P) = 1, pokiaľ A je kvadratický zbytok modulo P a P nedelí A
(A/P) = -1, pokiaľ A je kvadratický nezbytok modulo P
(A/P) = 0, pokiaľ P delí A

2. Výpočet Jacobiho symbolu - v podstate ide o celkové zobecnenie Legendrovho symbolu,
ktoré nám dovoľuje počítať bez obmedzení Legendrovho symbolu

3. Solovay-Strassenov prvočíselný test - jedná sa praktické využitie Jacobiho symbolu na
základe teórie Eulerovej vety z teórie čísiel. Aj keď už teraz ide o zastaralý algoritmus,
je historicky významný, pretože to bol jeden z prvých probabilistických prvočíselných algoritmov.


Dokumentácia

Kedže môj program dispunuje plne funkčním GUI, môžeme si program, aj z jeho .py formátu spustiť - 
v programe sa nachádzajú tri okná, každý na výpočet jednej z funkcií. Celý interface je veľmi
jednoduchý, ale odpovedá aj jednoduchosti vstupu. Na prvé dve funkcie postačia čísla A a P, kde
stlačením tlačidla vypočítať Vám na textový box dole dá výsledok. Okrem toho máme k dispozícii pri 
každej funkcii tlačidlo Zmazať, ktoré nám zmaže zadaný input. Pri Solovay-Strassenovom teste 
zadávame číslo na test prvočíselnosti, a druhé číslo bude počet iterácií s náhodnými číslami.
Solovay-Strassenov test, ako aj ostatné probabilistické testy, spočívajú v tom, že podľa niekoľko 
náhodne vybraných operácií vedia s netriviálnou presnosťou odhadnúť, či je číslo prvočíslo. Preto
je ich najlepšie využiť pre naozaj veľké čísla, kde prvčíselnosť nie je triviálna. 


Testy a validácie

Na každej z funkcií som extenzívne testoval obecné aj krajné prípady, v porovnaní s výsledkami s 
dostupnými online kalkulačkami. Každá z funkcií v poslednom štádiu prešla všetky testy. Tu je dôležité 
pripomenúť, že pre Solovay-Strassenov test to, že nám povie, že N je prvočíslo ešte nemusí znamenať, 
že na 100% je. Čím vyšší je ale počet iterácií, tým vyššia je pravdepodobnosť, že to prvočíslo je.


Poznámky o kóde

Rýchlosť kódu - Kedže výpočet Legendrova/Jacobiho symbolu sa dá pomocou ich axiomov jednoducho moduliť a
zjednodušiť, väčšina našich výpočtov, ako aj tých na internete, je instantná.
Testovanie Solovay-Strassenovho testu prebehlo výhradne pomocou prvočíselných tabuliek, pretože na internete
podobná kalkulačka Solovay-Strassenova testu na porovnanie neexistuje.

