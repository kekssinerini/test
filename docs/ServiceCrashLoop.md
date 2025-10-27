# ServiceCrashLoop

---

## CRITICAL

## Description
A service or container is repeatedly restarting (CrashLoopBackOff).

## Actions

## A. Check pod status

```
kubectl get pods -n my-namespace
```

Expected result:
```
NAME                          READY   STATUS             RESTARTS   AGE
api-service-7b8c9f8cc5-xyz    0/1     CrashLoopBackOff   10         20m
```

## B. Inspect logs

```
kubectl logs api-service-7b8c9f8cc5-xyz -n my-namespace --previous
```

## C. Check deployment configuration

```
kubectl describe deployment api-service -n my-namespace
```

- Look for environment variable or secret errors.

## D. Mitigation

- Roll back recent deployment:
  ```
  kubectl rollout undo deployment api-service
  ```
- If issue persists, increase restart backoff and involve developers.
