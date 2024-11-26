# Esteganografia

La esteganografia es la práctica por la cual, emisor y receptor, son capaces de comunicarse sin que otro interlocturo sea capaz de interceptarlos. Para conseguirlo, se requiere esconder el mensaje dentro de comunicaciones fiables.

Así pues, la capacidad principal de la esteganografia no es mantener un secreto com podria ser la encriptación, sino que el objetivo es la indetectibilidad por un tercero, se trata que ningún tercero sea capaz de saber ni si quiera que está habiendo una comunicación entre dos pares. Por otro lado, el estegoanalisis es la parte que se encarga de detectar si hay comunicaciones ocultes en nuestra red.

A la hora de poder crear un comunicación esteganográfica es imprescindible tener presente, el canal (chanel) por el que se transmitirá la información, el contenedor (cover) donde insertaremos (embed) las comunicaciones ocultas, y las funciones de incrustación y extracción del mensaje.

<picture>
 <img alt="Esquema básico de esteganografia." src="scheme_stego.png">
</picture>

### Vocabulario básico

Channel: canal, medio.

Warden: Vigilante, forma parte del channel. Es quien intentará capturar nuestros mensajes ocultos, puede ser de carácter pasivo, si no modifica el mensaje, activo, intenta destruir cualquier mensajes incrustado, y malicioso, intenta modificar los mensajes enviados para hacerlos prisioneros.

Cover Work: contenedor inicial

Stego Work: contenedor con mensaje oculto.

## El cover

Actualmente, el concepto de esteganografía está bastante desenvolupado y la mayoría de la gente ya imagina esas imágenes que de forma imperceptible al ojo humano son capaces de adjuntar mensajes ocultos. Pero la esteganografía ha estado siempre presente entre el mundo de la ocultación. Podemos distinguir tres grandes forma de jugar con nuestros *cover* para inserir nuestro mensaje:

**Stego by cover lookup**: Imaginaros por un momento que queremos enviar 10 bits a nuestro receptor sin que el *warden* pueda percibir que hay algún tipo de comunicación oculta. Una primera opció sería la de tener un banco importante de canciones, las cuales nosotros aplicaríamos algorítmos de hashes hasta encontrar con alguna canción donde sus primeros 10 bits coincidieran con los bits que queremos enviar. En este tipo de técnica, los bits que queremos enviar son evidentes, y de forma clara, son los que enviamos. La ocultación viene, puesta que el *warden* no sabe que esa canción forma parte de canal por donde enviamos información oculta. Las opciones son múltiples, lo único importante es que receptor y emisor se deben poner de acuerdo en el momento y el sitio para hacer el envío.

**Stego by cover synthesis**: Otra forma que tenemos para hacer llegar la información oculta es crear *covers* expresos para poder enviar la infomración oculta. Ya no se trata de buscar que hash es igual al mensaje que quiero hacer llegar, sino que aquí crearemos un patrón que emisor y receptor serán capaces de cifrar y descifrar. Un ejemplo ya hecho lo podéis encontrar en la web [SpamMimic](https://www.spammimic.com/), donde podemos crear correos electrónicos con los mensajes ya ocultos. 

**Stego by cover modifications**: En este caso se trata de usar un *cover* ya existente en una comunicación y ser capaz de hacer las modificaciones necesarias para ocultar un mensjae. La dificultad de este sistema reside en que cuanta más información añadamos más fácil será su detección, pero a la vez, cuanta menos información añadamos más ruido necesitaremos hacer. Las modificaciones pueden ser de tres tipos:
- Sequential rule - Se trata de incrutar los bits que queramos de forma secuancial, no requiere que emisor 
y receptor compartan el *pattern*
- Pseudo-random rule, craemos un *pattern* como si fuera una regla pseudoaleatòria (PRNG) y vamos incrustando siguiendo el patrón establecido.
- Adaptative selection rule: Es una buena opción, ya que adapta la inserción según el origen del cover. No se trata de saber donde está el bit en cuestión, sino de analizar el origen y decidir donde ponerlo según las características del cover. Por ejemplo, en una imagen no incrustaremos bits en fotos completamente negras, sino que buscaremos fotos con muchos contrastes, y dentro de estos contrastes, nos será más fàcil modificar el bit sin que se pueda percibir. 







12.1 - Issues

12.2 - terminologia bàsica

12.3 - evaluació secure LSB - teòric

12.4 - Practical stego schemes

12.5 - embedding proces







1. Escollir l'embolcall

2. Crear els algoritmes d'inserció i extracció, que han de tenir:

   1. Simbol assignment function

   2. The embedding modification

   3. The selection rule

3. Stego key management





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
