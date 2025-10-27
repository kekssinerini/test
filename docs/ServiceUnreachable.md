# ServiceUnreachable

---

## CRITICAL

## Description
A service endpoint is not reachable from the monitoring system or dependent services.

## Actions

## A. Check for Related alerts

- Look for upstream or network alerts (DNS issues, routing, load balancer failures).
- Confirm if multiple services are affected.

## B. Verify network connectivity

### B.1. Ping the service host

```
ping service-host.domain.com
```

Expected result:
```
64 bytes from service-host.domain.com: icmp_seq=1 ttl=63 time=42.1ms
```

### B.2. Test TCP connectivity

```
nc -vz service-host.domain.com 443
```

Expected result:
```
Connection to service-host.domain.com 443 port [tcp/https] succeeded!
```

## C. Validate DNS resolution

```
dig service-host.domain.com
```

If DNS fails, escalate to network operations or check DNS provider status.
