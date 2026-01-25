# Security Review (Task 3)

## Implemented Measures
- SECURE_SSL_REDIRECT=True: forces HTTPS by redirecting HTTP requests.
- HSTS enabled (SECURE_HSTS_SECONDS, INCLUDE_SUBDOMAINS, PRELOAD): tells browsers to only use HTTPS for the domain, reducing downgrade attacks.
- Secure cookies (SESSION_COOKIE_SECURE, CSRF_COOKIE_SECURE): ensures cookies are only sent over HTTPS.
- X_FRAME_OPTIONS="DENY": prevents clickjacking via framing.
- SECURE_CONTENT_TYPE_NOSNIFF=True: reduces MIME sniffing risks.
- SECURE_BROWSER_XSS_FILTER=True: enables browser-side XSS protection.

## Impact
These settings improve transport security and reduce common web vulnerabilities related to insecure transport and browser-side attacks.

## Potential Improvements
- Use secure reverse proxy configuration (SECURE_PROXY_SSL_HEADER) when deployed behind a load balancer.
- Use modern TLS settings and rotate certificates automatically.
- Consider adding CSP and other headers in production.
