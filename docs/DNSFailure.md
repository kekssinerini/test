# DNSFailure

---

## CRITICAL

## Description
DNS resolution for one or more service domains is failing.

## Actions

## A. Check DNS lookup

```
dig api.domain.com
```

Expected result:
```
;; ANSWER SECTION:
api.domain.com.  59  IN  A  192.168.1.10
```

## B. Check system DNS configuration

```
cat /etc/resolv.conf
```

Ensure correct DNS nameserver entries.

## C. Test with alternative resolver

```
dig @8.8.8.8 api.domain.com
```

If it succeeds with public DNS but not internally, escalate to internal networking or DNS team.
