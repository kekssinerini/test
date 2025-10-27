# SSLExpirationImminent

---

## WARNING

## Description
An SSL certificate is expiring soon, which could disrupt secure connections.

## Actions

## A. Verify certificate expiry date

```
echo | openssl s_client -servername api.domain.com -connect api.domain.com:443 2>/dev/null | openssl x509 -noout -enddate
```

Expected result:
```
notAfter=Jan 10 12:00:00 2026 GMT
```

## B. Check certificate renewal automation

- Validate that certbot, AWS ACM, or internal cert rotation is functioning.

## C. Manual renewal (example: certbot)

```
sudo certbot renew
```

## D. Verify after renewal

\```
openssl s_client -connect api.domain.com:443 | openssl x509 -noout -dates
\```
