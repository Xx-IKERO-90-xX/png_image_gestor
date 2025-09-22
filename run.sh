#!/bin/bash

NETWORK_NAME="mc-block-net"
SUBNET="172.20.0.0/16"

if ! docker network inspect $NETWORK_NAME >/dev/null 2>&1; then
    echo "La red $NETWORK_NAME no existe. Creándola..."
    docker network create --driver=bridge --subnet=$SUBNET $NETWORK_NAME
else
    echo "La red $NETWORK_NAME ya existe. Continuando..."
fi

# Construir las imágenes definidas en docker-compose
echo "Construyendo imágenes..."
sudo docker build -t png_image_gestor .

# Levantar los contenedores
echo "Levantando contenedores..."
sudo docker-compose up -d

echo "Todo listo 🚀"
