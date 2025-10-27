# HighLatencyDetected

---

## WARNING

## Description
Response times for a monitored service have exceeded acceptable thresholds.

## Actions

## A. Check for Related alerts

- Review load balancer metrics and APM traces for increased latency.
- Check database or downstream service performance.

## B. Verify latency manually

```
curl -w "@curl-format.txt" -o /dev/null -s https://api.domain.com/health
```

Expected result:
```
time_total: 0.150
```

## C. Investigate backend bottlenecks

- Use profiling tools (e.g., Datadog APM, New Relic traces).
- Check for recent deployments or configuration changes.
