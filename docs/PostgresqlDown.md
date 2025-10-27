# PostgresqlDown

---

## CRITICAL

## Description
PostgreSQL instance is down.

## Actions

## A. Check for Related alerts

## B. Check server's availability (VPN required)

### B.1. Ping the server

No VPN result:
```
-> ping pg-server-name.db.test cloud
ping: pg-server-name.db.test.cloud: Name or service not known
```

Expected result:
```
-> ping pg-server-name.db.test cloud
64 bytes from 127.0.0.1 (127.0.0.1): icmp_seq=1 ttl=63 time=44.4ms
64 bytes from 127.0.0.1 (127.0.0.1): icmp_seq=2 ttl=63 time=43.2ms
```
