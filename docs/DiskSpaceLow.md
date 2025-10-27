# DiskSpaceLow

---

## CRITICAL

## Description
A server or container is running low on disk space, which can lead to service interruptions.

## Actions

## A. Check for Related alerts

- Verify if multiple nodes report low disk space — might indicate a shared storage issue.

## B. Check disk usage

### B.1. SSH into the affected host

```
ssh user@affected-host
```

### B.2. Run disk usage check

```
df -h
```

Expected result:
```
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        40G   39G  1.0G  98% /
```

## C. Clean up logs and temporary files

```
sudo du -ahx / | sort -rh | head -n 20
sudo journalctl --vacuum-time=3d
sudo rm -rf /tmp/*
```

## D. Prevent recurrence

- Review log rotation policies.
- Increase disk volume size if usage is legitimate and sustained.
