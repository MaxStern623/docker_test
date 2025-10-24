Screenshot: Generated QR code

This screenshot (`qrcode.png`) was created by running the dockerized QR Code Generator locally and mounting a host folder so the generated PNG appears on the host filesystem.

Commands used to produce the screenshot:

    mkdir -p host_qr_codes
    docker rm -f qr-generator || true
    docker run -d --name qr-generator -v $PWD/host_qr_codes:/app/qr_codes \
      qr-code-generator-app --url "https://www.example.com"
    docker logs -f qr-generator
    ls -l host_qr_codes

The `docker logs -f qr-generator` command prints a confirmation line when the QR file is written, and `ls -l host_qr_codes` shows the generated `qrcode.png` file. Use these two outputs as your container-logs and file-listing screenshots for submission.
