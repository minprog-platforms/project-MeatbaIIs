## Probleem
Bij het ontwikkelen van een (groot) project moeten er vaak bestanden toegevoegd of veranderd worden. Hierbij kunnen gemakkelijk bugs/conflicten ontstaan. Dit kan zorgen dat essentiele bestanden in een project niet meer bruikbaar zijn en er dus hard gezocht moet worden waar de fout is ontstaan of dat er een backup gebruikt moet worden en dan gaat er dus werk verloren.

## Oplossing
Hierom wil ik een applicatie ontwikkelen die automatisch een github project test zodra er aanpassingen gemaakt worden. Dit zorgt dat fouten direct worden opgemerkt en dat het dus ook makkelijk te achterhalen is bij welke push er een fout ontstaan is.

!["Voorbeeld interface"](doc/InterfaceSchets.jpeg)
Met dit interface is een gebruiker in staat om een project te linken met bestanden die de code kunnen testen. Door een link naar het project in te stellen en de juiste testbestanden te uploaden is het mogelijk om de tests te laten draaien zodra er een bestand toegevoegd of aangepast wordt bij dit project.

## Benodigheden
De applicatie heeft weinig gegevens nodig om te kunnen werken. Hij moet toegang hebben tot het github project en hij moet de test bestanden paraat hebben. De toegang tot het project kan geregeld worden door een github-gebruiker aan de applicatie te koppelen, dan moet deze gebruiker nog wel aan het project toegevoegd worden.
Om te kunnen testen moeten testomgevingen gedownload worden zoals bijvoorbeeld pytest. Anders zou de applicatie de test-bestanden niet kunnen uitvoeren. Om te testen zal de applicatie het hele project van github pullen. Misschien dat er nog onderscheidt gemaakt kan worden tussen relevante bestanden, maar het risico is dan wel dat er toch een bestand niet gepulled wordt dat achteraf wel nodig blijkt. Denk aan een plaatje dat in de code aangeroepen wordt o.i.d.. 
