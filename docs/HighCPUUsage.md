# HighCPUUsage

---

## WARNING

## Description
CPU usage exceeds the defined threshold on one or more hosts, potentially impacting performance.

## Actions

## A. Check for Related alerts

- Verify if CPU usage spike aligns with deployments, batch jobs, or cron tasks.

## B. Identify high CPU processes

### B.1. SSH into the host

```
ssh user@affected-host
```

### B.2. Check CPU usage

```
top -o %CPU
```

Expected result:
```
PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
3212 appuser   20   0  234568  14232   2304 R  90.0   7.0   5:13.56 worker-process
```

## C. Check recent deployments or code changes

- If correlated, consider rolling back or scaling horizontally.

## D. Temporary Mitigation

```
systemctl restart my-service
```

or in Kubernetes:

```
kubectl scale deployment my-service --replicas=2
```
