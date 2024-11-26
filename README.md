# Esteganografia

La esteganografia es la práctica por la cual, emisor y receptor, son capaces de comunicarse sin que otro interlocturo sea capaz de interceptarlos. Para conseguirlo, se requiere esconder el mensaje dentro de comunicaciones fiables.

Así pues, la capacidad principal de la esteganografia no es mantener un secreto com podria ser la encriptación, sino que el objetivo es la indetectibilidad por un tercero, se trata que ningún tercero sea capaz de saber ni si quiera que está habiendo una comunicación entre dos pares. Por otro lado, el estegoanalisis es la parte que se encarga de detectar si hay comunicaciones ocultes en nuestra red.

A la hora de poder crear un comunicación esteganográfica es imprescindible tener presente, el canal (chanel) por el que se transmitirá la información, el contenedor (cover) donde insertaremos (embed) las comunicaciones ocultas, y las funciones de *embeded* y extracción del mensaje.

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

## Embeded and extraction functions

La incrustación de nuestro mensaje en el *cover* y su modificación genera la siguiente notificación científica:

```math
Embeded: C \times K \times M \rightarrow S

Extraction: S \rightarrow M
```
Donde *C* es el conjunt de *covers*, *K* es la clave con la que encriptamos el mensaje, *M* es el mensaje que queremos ocultar, y *S* es el resultado de la incrustación del mensaje en el *cover*.

Teniendo en cuenta las dos últimas fórmulas, debemos siempre tener en cuenta:

*Embedding capacity*: És la capacitat total que tenemos para incrustar un mensaje, se mide en bits.

*Impact of embedding (or embedding distortion)*: Calcula la distancia entre *C* y *S*, se calcula bit a bit, cuanta mejor sea la *embedding efficiency* menor será el impacto, pero también será menor la cantidad de información total.


