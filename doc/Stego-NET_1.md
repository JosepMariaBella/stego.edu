# Actividad: Hello World!

En esta primera actividad nos vamos a centrar básicamente en la configuración de nuestras máquinas el envío de paquetes a través de la librería *scapy*. 

Para ello, vamos a seguir el siguiente esquema:

$$Ubuntu Server StegoA \longleftrightarrow Ubuntu Server Router IDS/IPS \longleftrightarrow Ubuntu Desktop StegoB$$

El objetivo es modificar enviar paquetes ICMP modificando el Payload.

Para ello, empezamos configurando nuestra Ubuntu Server inicial:

```bash
sudo nano /etc/netplan/50-cloud-init.yaml
sudo nano /etc/cloud/cloud.cfg.d/99-disable-network-config.cfg
sudo nano /etc/netplan/50-cloud-init.yaml
sudo netplan apply

sudo apt install python3-venv
sudo apt install python3-pip
root <<<<----- Tot amb root!!!!
python3 -m venv stego
source stego/bin/activate    --- deactivate

$> pip install -r requirements.txt
$> pip freeze > requeriments.txt
pip list

pip3 install scapy netfilterqueue    // --break-system-packages
```
Añadimos una ruta a StegoA para poder enviar corréctamente los paquetes:
```bash
sudo ip route add 172.20.121.0/24 via 172.20.120.254
```
Para poder enviar usaremos el código [helloWorldICMP.py](../src/helloWorldICMP.py)

En la màquina receptora, fem el mateix que stegoA, però ara posem aquest codi.

```python
from scapy.all import sniff, ICMP

# Define a callback function that processes each packet
def icmp_packet_callback(packet):
    if packet.haslayer(ICMP):
        # Get the payload of the ICMP packet
        icmp_payload = packet[ICMP].payload.load if packet[ICMP].payload else b''

        if icmp_payload:
            print(f"ICMP packet payload: {icmp_payload.decode(errors='ignore')}")  # Decode payload as string

# Capture ICMP packets (use appropriate interface or adjust filter)
sniff(filter="icmp", prn=icmp_packet_callback, store=0)
```

Per crear la màquina router:

# UFW

[](https://gist.github.com/kimus/9315140#ufw)

I use Ubuntu’s Uncomplicated firewall because it is available on Ubuntu and it's very simple.

## Install UFW

[](https://gist.github.com/kimus/9315140#install-ufw)

if ufw is not installed by default be sure to install it first.

```
$ sudo apt-get install ufw
```

## NAT

[](https://gist.github.com/kimus/9315140#nat)

If you needed ufw to NAT the connections from the external interface to the internal the solution is pretty straight forward. In the file /etc/default/ufw change the parameter DEFAULT_FORWARD_POLICY

```
DEFAULT_FORWARD_POLICY="ACCEPT"
```

Also configure /etc/ufw/sysctl.conf to allow ipv4 forwarding (the parameters is commented out by default). Uncomment for ipv6 if you want.

```
net.ipv4.ip_forward=1
#net/ipv6/conf/default/forwarding=1
#net/ipv6/conf/all/forwarding=1
```

The final step is to add NAT to ufw’s configuration. Add the following to /etc/ufw/before.rules just before the filter rules.

```
# NAT table rules
*nat
:POSTROUTING ACCEPT [0:0]

# Forward traffic through eth0 - Change to match you out-interface
-A POSTROUTING -s 192.168.1.0/24 -o eth0 -j MASQUERADE

# don't delete the 'COMMIT' line or these nat table rules won't
# be processed
COMMIT
```

Now enable the changes by restarting ufw.

```
$ sudo ufw disable && sudo ufw enable
```

## FORWARD

[](https://gist.github.com/kimus/9315140#forward)

For port forwardind just do something like this.

```
# NAT table rules
*nat
:PREROUTING ACCEPT [0:0]
:POSTROUTING ACCEPT [0:0]

# Port Forwardings
-A PREROUTING -i eth0 -p tcp --dport 22 -j DNAT --to-destination 192.168.1.10

# Forward traffic through eth0 - Change to match you out-interface
-A POSTROUTING -s 192.168.1.0/24 -o eth0 -j MASQUERADE

# don't delete the 'COMMIT' line or these nat table rules won't
# be processed
COMMIT
```

## Instal·lació Suricata

```bash
sudo add-apt-repository ppa:oisf/suricata-stable
sudo apt-get update
sudo apt-get install suricata
sudo suricata-update
```

Ara intentem detectar el payload d'aquestes dues màquines. Dins les regles que s'instal·len automàticament en Suricata, no en ve cap que ho detecti, és a dir, si permetem passar icmp, tenim via lliure per poder-nos comunicar, només amb una anàlisis posterior de tot el tràfic de xarxa podríem observar el payload.

Si volem que una regla de suricata funcioni, el problema que tenim és que per analitzar el payload ho hem de fer des del `content` i amb el `pcre`, però aquest no accepta continguits buit, és a dir, no podem posar `content:""; pcre:"/.+/"`. No ens funcionaria, perquè sempre hem de posar alguna cosa de contingut. 

Si volem, podem excloure el content, si ho fem, el problema serà que ens detecta coses com a payload que no son el que volem comprovar, obtindrem falsos positius que no ens interessen. 

Així doncs hem d'obtar per anar provant, no tenim una regla que ho pugui controlar tot, una aproximació seria:

```yaml
alert ip any any -> any any (msg:"PING PAYLOAD"; ip_proto:1; pcre:"/[aeiouAEIOU]/"; sid:1000001; rev1;)
```

Busca alguna vocal en el nostre payload, clar, si algú enviés un missatge sense vocals no seria detectale.

Els paquets ICMP

Aquí tens una taula amb les dades que has demanat per als paquets ICMP més comuns:

| **Tipus de Paquet ICMP**                                                | **Payload**                                       | **Funció i Ús Comú**                                                                                                                                        | **Com executar-ho a CLI d'Ubuntu**                                                                                                                         |
| ----------------------------------------------------------------------- | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Echo Request (Tipus 8)** i **Echo Reply (Tipus 0)**                   | Identificador i número de seqüència               | Verificar la connectivitat entre dos dispositius (ping). Permet mesurar la latència i confirmar si un dispositiu és accessible.                             | `ping <adreça_IP_destinació>`<br>o<br>`sudo hping3 -1 <adreça_IP_destinació>`                                                                              |
| **Destination Unreachable (Tipus 3)**                                   | Capçalera IP del paquet original i dades inicials | Indica que un dispositiu o xarxa és inabastable des del punt d’origen. És útil per detectar si una xarxa o host no està accessible o el port no està obert. | `sudo hping3 -1 --icmp --icmp-type 3 <adreça_IP_destinació>`                                                                                               |
| **Redirect (Tipus 5)**                                                  | Part del paquet original                          | Recomana a un dispositiu que utilitzi una ruta alternativa per enviar paquets a la destinació, ajudant a optimitzar les rutes en la xarxa.                  | `sudo hping3 -1 --icmp --icmp-type 5 <adreça_IP_destinació>`                                                                                               |
| **Time Exceeded (Tipus 11)**                                            | Capçalera IP i dades inicials del paquet original | Indica que el TTL del paquet ha arribat a zero abans d’arribar a la destinació. Útil per a `traceroute` i altres eines de rastreig de rutes.                | `ping -t 1 <adreça_IP_destinació>`<br>o<br>`sudo hping3 -1 --icmp --icmp-type 11 <adreça_IP_destinació>`                                                   |
| **Parameter Problem (Tipus 12)**                                        | Capçalera IP i dades inicials del paquet original | Indica un problema amb un paràmetre de la capçalera IP del paquet, com ara un camp no vàlid. És útil per depurar errors en paquets IP.                      | `sudo hping3 -1 --icmp --icmp-type 12 <adreça_IP_destinació>`                                                                                              |
| **Timestamp Request (Tipus 13)** i **Timestamp Reply (Tipus 14)**       | Marques de temps (enviament, recepció, resposta)  | Permeten sincronitzar el rellotge entre dispositius, ajudant a calcular el retard (latència) i millorar la sincronització horària en la xarxa.              | `sudo hping3 -1 --icmp --icmp-type 13 <adreça_IP_destinació>`<br>per Request<br>`sudo hping3 -1 --icmp --icmp-type 14 <adreça_IP_destinació>`<br>per Reply |
| **Address Mask Request (Tipus 17)** i **Address Mask Reply (Tipus 18)** | Màscara de xarxa del dispositiu                   | Sol·licita la màscara de xarxa d’un dispositiu, especialment útil en xarxes antigues per obtenir informació de subxarxa. Avui dia és poc utilitzat.         | `sudo hping3 -1 --icmp --icmp-type 17 <adreça_IP_destinació>`<br>per Request<br>`sudo hping3 -1 --icmp --icmp-type 18 <adreça_IP_destinació>`<br>per Reply |

Aquestes comandes et permetran enviar cadascun dels paquets ICMP amb `hping3` o `ping` des de la línia de comandes d’Ubuntu, facilitant així el diagnòstic i prova de xarxes!

Aquí tens una taula amb les dades que has demanat per als paquets ICMP més comuns:

| **Tipus de Paquet ICMP**                                                | **Payload**                                                                                                            |                                                                                                                                                                                                                                   |
| ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Echo Request (Tipus 8)** i **Echo Reply (Tipus 0)**                   | Identificador i número de seqüència<br/><br/>No veig seqüència, sempre igual.<br/>Només canvien els tres primers bytes | &w................. !"#$%&'()*+,-./012345<br/><br/>2677020000000000101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f3031323334353637<br/>windows: 6162636465666768696a6b6c6d6e6f7071727374757677616263646566676869 |
|                                                                         |                                                                                                                        |                                                                                                                                                                                                                                   |
| **Destination Unreachable (Tipus 3)**                                   | Capçalera IP del paquet original i dades inicials.<br/>No he vist cap payload                                          |                                                                                                                                                                                                                                   |
| **Redirect (Tipus 5)**                                                  | Part del paquet original<br/>No veig res                                                                               |                                                                                                                                                                                                                                   |
| **Time Exceeded (Tipus 11)**                                            | Capçalera IP i dades inicials del paquet original                                                                      |                                                                                                                                                                                                                                   |
| **Parameter Problem (Tipus 12)**                                        | Capçalera IP i dades inicials del paquet original                                                                      |                                                                                                                                                                                                                                   |
| **Timestamp Request (Tipus 13)** i **Timestamp Reply (Tipus 14)**       | Marques de temps (enviament, recepció, resposta)                                                                       |                                                                                                                                                                                                                                   |
| **Address Mask Request (Tipus 17)** i **Address Mask Reply (Tipus 18)** | Màscara de xarxa del dispositiu                                                                                        |                                                                                                                                                                                                                                   |

Aquestes comandes et permetran enviar cadascun dels paquets ICMP amb `hping3` o `ping` des de la línia de comandes d’Ubuntu, facilitant així el diagnòstic i prova de xarxes!

El payload comença després de quatre bytes buits 00 00 00 00
