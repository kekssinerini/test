# NodeNotReady

---

## CRITICAL

## Description
A Kubernetes node is reporting as `NotReady`, potentially causing pod scheduling failures.

## Actions

## A. Check node status

```
kubectl get nodes
```

Expected result:
```
NAME           STATUS     ROLES    AGE   VERSION
node-1         Ready      worker   23d   v1.28.3
node-2         NotReady   worker   21d   v1.28.3
```

## B. Describe the affected node

```
kubectl describe node node-2
```

Look for taints or network issues in the output.

## C. Check kubelet logs

```
journalctl -u kubelet -f
```

## D. Mitigation

- Restart the kubelet service:
  ```
  systemctl restart kubelet
  ```
- If the node remains unresponsive, cordon and drain it:
  ```
  kubectl cordon node-2
  kubectl drain node-2 --ignore-daemonsets
  ```
