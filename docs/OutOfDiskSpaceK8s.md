# OutOfDiskSpaceK8s

---

## CRITICAL

## Description
Kubernetes node is running out of disk space; pods may be evicted.

## Actions

## A. Check node conditions

```
kubectl describe node node-name | grep DiskPressure
```

## B. Check disk usage

```
df -h
```

Expected result:
```
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       80G   79G  1.0G  98% /
```

## C. Clean up unused resources

```
docker system prune -af
kubectl get evictedpods --all-namespaces
```

## D. Prevent recurrence

- Implement pod log rotation.
- Add disk usage monitoring via Prometheus node exporter.
