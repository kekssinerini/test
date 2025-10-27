# MemoryLeakDetected

---

## CRITICAL

## Description
A service is consuming excessive memory over time, indicating a potential memory leak.

## Actions

## A. Check for Related alerts

- Review APM metrics (e.g., Datadog, New Relic) for memory usage over time.
- Identify correlated error logs (e.g., OutOfMemoryError, OOMKilled events in Kubernetes).

## B. Verify process memory consumption

### B.1. SSH into the affected host

```
ssh user@affected-host
```

### B.2. List top memory consumers

```
top -o %MEM
```

Expected result:
```
PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
2456 appuser   20   0  234568  14232   2304 S   0.3  70.2   5:13.56 my-service
```

## C. Mitigation Steps

- Restart the affected service to free memory.
- If running in Kubernetes:
  ```
  kubectl rollout restart deployment my-service
  ```
- Schedule follow-up with developers to analyze heap dumps or memory profiles.
