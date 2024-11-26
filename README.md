# Esteganografia

La esteganografia es la práctica por la cual, emisor y receptor, son capaces de comunicarse sin que otro interlocturo sea capaz de interceptarlos. Para conseguirlo, se requiere esconder el mensaje dentro de comunicaciones fiables.


Així doncs, la capacitat principal de la esteganografia no és el secret, sinó la indetectabilitat per part de tercers, es tracta que no hi puguin haver algoritmes que et descobreixin. L'estegoanàlisis és la pràctica que treballa aquests algoritmes i tracta de detectar si hi ha comunicacions secretes entre emissor i receptor.

A l'hora de preparar l'esquema de l'esteganografia, cal tenir present el canal de comunicació, l'embolcall, i les funcions d'inserció i extracció.  El nostre objectiu pricnipal és que sigui estadísticament indetectable.

LSB és un dels algoritmes més simples.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="[https://user-images.githubusercontent.com/25423296/163456776-7f95b81a-f1ed-45f7-b7ab-8fa810d529fa.png](https://raw.githubusercontent.com/JosepMariaBella/stego.edu/refs/heads/main/scheme_stego.png)">
  <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/25423296/163456779-a8556205-d0a5-45e2-ac17-42d089e3c3f8.png">
  <img alt="Shows an illustrated sun in light mode and a moon with stars in dark mode." src="https://user-images.githubusercontent.com/25423296/163456779-a8556205-d0a5-45e2-ac17-42d089e3c3f8.png">
</picture>

12.1 - Issues

12.2 - terminologia bàsica

12.3 - evaluació secure LSB - teòric

12.4 - Practical stego schemes

12.5 - embedding proces



## Vocabulari

Channel -> canal, mitjà.

Warden -> Vigilant, forma part del channel. Pot ser passiu (si no modifica la comunicació), actiu (modifica el contingut per destruir possibles missatges interns). Maliciós, modifica el contingut per convertir receptor i emissor en presoners. Impersonificació.

Cover Work -> embolcall inicial

Com a stego, hem de tenir present:



1. Escollir l'embolcall

2. Crear els algoritmes d'inserció i extracció, que han de tenir:

   1. Simbol assignment function

   2. The embedding modification

   3. The selection rule

3. Stego key management



### Channel

**Stego by cover lookup**: Volem enviar 10 bits, tenim 10000 cançons, faig hashesh fins que em trobi el hash que comenci per aquests 10 bits, i llavors, envio aquesta cançó. No hem provocat cap modificació. Només haurem de comunicar d'alguna manera quina cançó és, i tenir present, que si necessitem enviar més bits, necessitarem moltes més cançons:

`Nombre de cançons amb hashesh diferents = (bits a enviar ^ 2) mínim`

**Stego by cover synthesis**: Es tracta d'un treball amb diverses converses, el emissor seleccionar les línies que vols, i aquest és el missatge enviat. II WW - llibre "Between Silk and Cyanide" i codi "Windswept", british spies. També teim **el programa SpamMimmi* http://www.spammimic.com, codifica un missatge reendreçant missatges spam, ja que la falta de ortografia i gramàtica dels correus spam, permet més modificacions. Un altre exemple és el *data masking*, creen un missatge estadísticament similar a algú, per exemple una cançó, mentre ningú escolti la cançó, ningú es donarà compte.

**Stego by cover modifications**: És quan l'emissor altera un *cover* per obtenir incrustar un missatge codificat. Quan menys modifiquem, més difícil serà de detectar. Tenim tres tipus de regles per modificar:

- Sequential rule- incrusta els bits de forma seqüencial en una imatge, començant per la fila tal i anant per les columnes.... més fàcil d'implementar i detectar. (13.2.1)

- Pseudo-random rule, creem una regla pseudoaleatòria (PRNG) per anar incrustant en el lloc que toqui. .

- Adaptative selection rule : Va incrustant els bits, segons l'origen de la obra

### Key stego

L'objectiu de tenir una regla que fa que les adaptacions i les pseudo vagin variant.

També interessant les claus de sessió.

Però també ens pot ajudar a encriptar els missatges



## Notation and terminology

Embeded: `C x K x M -> C`

Extraction: `C -> M`

*K$s$* : És la stego key extreta d'un conjunt de possibles claus *K*.

*M* : El conjunt de missatges possibles a incrustar. *m* el missatge escollit.

*C* : El conjunt de tots els treballs originals. *c* el treball original escollit.

The work *s* = *Emb*(c, K$s$, m)

*Embedding capacity*: És la capacitat total que tenim per incrustar un missatge, es mesura en bits, és log$2$ |M|. Tinc 6 bits, puc fer 64 combinacions diferents de missatges a poder enviar. (2^6 = 64)

*Impact of embedding (or embedding distortion)*:  Es mesura com D(c,s), on D és la distàcnia definida a C. Intenta calcular la diferència entre l'original i el missatge a través de l'error quadràtic mig. Pixel a pixel, es calcula el quadrat de la seva diferència i es fa la mitjana. Quants més pixels poguem posar, més impactarà, però també millorarà la seva *embedding efficiency*.











# Estegoanalisis

L'estegoanalisis és la capacitat de dos dispositius d'enviar-se informació sense ser detectats. No només es tracta que cap intercepto pugui conèixer el missatge que s'envia, sinó que es tracta que ningú sigui conscient que s'ha arribat a enviar un missatge.

L'objectiu d'ocultar comunicacions poden ser variades, però els més comuns tenen relació amb la intel·igència, però també podem trobar altres usos, com per exemple, poder posar comunicacions segures dins de les nostres aplicacions.

-----

Posar teoria del lliber

----
