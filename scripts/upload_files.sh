#!/bin/bash

PORT="/dev/ttyUSB0"

log() {
  echo "$(date +'%Y-%m-%d %H:%M:%S') - $1"
}

upload_file() {
  local file_path=$1
  log "Uploading $file_path..."
  if ampy --port $PORT put $file_path; then
    log "$file_path uploaded successfully."
  else
    log "Failed to upload $file_path."
  fi
}

upload_file "../esp/websocket_client.py"
upload_file "../esp/config.py"
upload_file "../esp/wifi.py"
upload_file "../esp/boot.py"

log "All files uploaded."