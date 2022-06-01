Bij dit project is een webapplicatie ontwikkeld die automatisch een github project test als er een push gemaakt wordt. Hiervoor wordt Pytest gebruikt. Om het op te zetten voor een project is het nodig om een webhook op te zetten naar www.testr.devops.quinner.nl/webhook en je repository op 'public' te zetten. Daarbij moeten ook de test bestanden geupload worden op de webpagina. Daarna wordt het vanzelf getest en wordt het resultaat naar de webhook teruggestuurd.
Hieronder is de layout van de webpagina te zien:

!["Webpage"](/doc/webpage.jpeg)

Door de naam van je project in te vullen kan je vervolgens voor dat project de test bestanden managen. Als je op 'Upload/show files' klikt upload het gekozen bestand, als er geen bestand gekozen is wordt kan je wel zien welke bestanden er voor dat project op de server staan. Vervolgens kan je daaronder de bestanden downloaden of verwijderen, hiervoor moet je onder 'Filename:' de bestandsnaam invullen. Dan kan je met de knoppen eronder het bestand verwijderen of downloaden.

Om de flaskapplicatie te maken heb ik de volgende tutorial gebruik. De HTML layout van deze tutorial heb ik gebruikt en de __init__.py code heb ik vrijwel identiek gehouden.
https://flask.palletsprojects.com/en/2.1.x/tutorial/

Om de dockerfile in te stellen heb ik de volgende tutorial gebruikt. Hier heb ik nog wel verscheidene aanpassingen aan gemaakt.
https://blog.logrocket.com/build-deploy-flask-app-using-docker/

Om de webhook op te stellen heb ik de volgende tutorial gebruikt. Deze code moest ik nog wel aanpassen voor mijn eigen doeleinden.
https://maximorlov.com/automated-deployments-from-github-with-webhook/

Voor het uploaden en downloaden van bestanden heb ik de volgende tutorial gebruikt:
https://flask.palletsprojects.com/en/2.1.x/patterns/fileuploads/
