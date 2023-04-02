# tsonder
Ohjelman tarkoitus on etsiä opiskeluseuraa. Ohjelmaan kirjaudutaan ja tehdään julkinen profiili, mihin kuuluu mm. Nimi, kuva, kuvaus ja ala mitä opiskelee. Sovellus toimii klassisella hot or not periaatteella, eli päänäkymään tulee muiden tekemiä profiileja, joista mieluisista voi tykätä ja ei-mieluisat voi hylätä. Jos kaksi tykkää toisistaan, tulee siitä ilmoitus ja aukeaa heidän välilleen keskustelualue.
Sovelluksen ominaisuuksia:
- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen ja luoda profiilin itselleen
- Käyttäjä näkee etusivulla muiden käyttäjiä yksi kerrallaan sekä keskustelujen määrän sekä napin omaan profiiliin.
- Käyttäjä voi kirjoittaa keskusteluihin
- Käyttäjä voi poistaa keskustelun, jolloin se poistuu molemmilta
- Käyttäjä voi muokata viestiään
- Käyttäjä voi etsiä kaikki viestit, joiden osana on annettu sana
- Ylläpitäjä voi poistaa Käyttäjiä sovelluksesta
- Ylläpitäjä voi aloittaa keskustelun kenen tahansa kanssa
- Ylläpitäjä voi refreshaa sovelluksen eli silloin voi tulla samoja ihmisiä etusivulla vastaan uudelleen

# KÄYNNISTYSOHJEET
Kloonaa repositori koneellesi ja mene sen juurikansioon. Tee sinne .env tiedosto, jonne laitat seuraavat tiedot 

- DATABASE_URL=(tietokannan-paikallinen-osoite)
- SECRET_KEY=(salainen-avain)

Sen jälkeen asenna sovelluksen riippuvuudet virtuaaliympäristöösi
- $ python3 -m venv venv
- $ source venv/bin/activate
- $ pip install -r ./requirements.txt
  
Käynnistä sovellus komennolla 
- Flask run

Sovellus on vielä erittäin keskeneräinen, joten siinä on vain sisäänkirjautumisnäkymä, joka ei toimi kunnolla.
