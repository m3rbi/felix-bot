#!/bin/bash

CREDS_FILE="/home/$USER/.config/felix-bot/credentials"

if [[ ! -f $CREDS_FILE ]]
then
    echo "Could not find credentials file $CREDS_FILE"
    exit
fi

source $CREDS_FILE

if [[ -z $TELEGRAM_TOKEN ]]
then
    echo "Creds file does not export \$TELEGRAM_TOKEN"
    exit
fi

echo "Starting Felix bot!"
TELEGRAM_TOKEN=$TELEGRAM_TOKEN PLEX_CLAIM=$PLEX_CLAIM docker-compose up -d
