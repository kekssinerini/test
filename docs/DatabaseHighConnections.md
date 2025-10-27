# DatabaseHighConnections

---

## WARNING

## Description
Database has reached or exceeded its maximum allowed connection count.

## Actions

## A. Check for Related alerts

- Verify application connection pool metrics.
- Look for unclosed or idle connections.

## B. Check active connections

```
psql -h db-host -U postgres -c "SELECT count(*) FROM pg_stat_activity;"
```

Expected result:
```
 count
-------
   120
(1 row)
```

## C. Identify blocking or idle connections

```
SELECT pid, state, query, age(now(), query_start) FROM pg_stat_activity ORDER BY query_start;
```

Terminate long-idle or blocking connections as needed:
```
SELECT pg_terminate_backend(pid);
```

## D. Prevent recurrence

- Optimize connection pooling.
- Increase `max_connections` only if infrastructure allows.
