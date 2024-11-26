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
root <<<<----- Todo amb root!!!!
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

En la màquina receptora, podemos ver el resultado a través de Wireshark.
