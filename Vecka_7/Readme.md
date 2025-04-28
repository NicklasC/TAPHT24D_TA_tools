CI/CD
=====

CI/CD är ett viktigt inslag i agil systemutveckling, som bejakar snabb feedback.

Vad händer när utvecklaren pushar kod?
--------------------------------------
När utvecklaren pushar kod innebär det att merparten av de automatiserade testerna ska köras. Byggpipelines aktiveras. Eventuellt undantag kan 
vara omfattande regressionstester som kan köras nattligen eller per release, beroende på exekveringstid osv.



Vilka tester ska köras?
-----------------------
Det absoluta flertalet eller samtliga automattester. Man börjar med tester som kan exekvera snabbt, för att sedan köra 
tester som tar mer tid. En typisk ordning kan vara
* Kodlint, stylekontroller
* Unittester
* Sasttester, exv Sonarcube
* Smoketester
* Dasttester, exv OWASP ZAP
* Integrationstester
* Regressionstester


När och hur byggs applikationen?
--------------------------------
Den byggs innan DAST tester, smoketester

Rita flödet som en enkel bild eller lista.
------------------------------------------


Vad skulle kunna gå fel i flödet?
---------------------------------
Vad kan inte gå fel? =). 
* Kodlint, stylekontroller
Koden kan vara felformatterad enligt projeketets guidelines.

* Unittester
Metoder kan ha refakturerats och sluta fungera korrekt. 

* Sasttester, exv Sonarcube (Whitebox)
Koden använda sig av dåliga kodmönster, som tex kan möjliggöra sql injections, os injections osv.
Dessa upptäcks av Sonarcube.


(Här byggs systemet ihop i en testmiljö)

* Smoketester
Dessa testar att absolut grundfunktionalitet fungerar. Applikationen startar samt några kritiska funktioner.

* Dasttester, exv OWASP ZAP (Blackbox)
Dessa tester testar det körande systemet och söker efter vanliga säkerhetsfel.

* Integrationstester
Testar integrationen mellan moduler. Frontend anrop pratar med backenden osv.

* Regressionstester
Här testar vi tidigare framtagen funktionalitet så att inga nya buggar introducerats.







Vilka tester är viktigast i just ditt flöde?
--------------------------------------------


Hur kan testning förbättra kvaliteten?
--------------------------------------