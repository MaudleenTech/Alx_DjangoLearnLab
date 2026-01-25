# HTTPS Deployment Configuration (Task 3)

## Nginx (example)
1. Obtain SSL/TLS certificates (e.g., Let's Encrypt).
2. Configure Nginx to listen on 443 with the certificate paths.
3. Redirect HTTP (port 80) to HTTPS.

### Example Nginx config
- HTTP redirect:
  - listen 80;
  - return 301 https://$host$request_uri;

- HTTPS server:
  - listen 443 ssl;
  - ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
  - ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

## Apache (example)
1. Enable SSL module: a2enmod ssl
2. Configure VirtualHost on 443 with SSLCertificateFile/KeyFile.
3. Redirect port 80 to 443 using RewriteRule or Redirect.

## Notes
- In production behind a proxy/load balancer, set SECURE_PROXY_SSL_HEADER appropriately.
- Ensure the reverse proxy forwards the correct scheme headers.
