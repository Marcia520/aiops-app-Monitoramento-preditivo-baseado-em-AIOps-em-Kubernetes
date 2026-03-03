C:\Users\Marcia\Documents\aiops-app\k8s>kubectl get pods -n aiops-banco
NAME                                                     READY   STATUS             RESTARTS        AGE
aiops-app-65f6b9878d-p5s4q                               1/1     Running            0               61s
aiops-app-65f6b9878d-twsxq                               1/1     Running            0               77s
alertmanager-prometheus-kube-prometheus-alertmanager-0   2/2     Running            6 (11m ago)     2d18h
prometheus-grafana-644d5c5bdf-klgh4                      3/3     Running            3 (11m ago)     46h
prometheus-kube-prometheus-operator-8465b57d95-zbznf     1/1     Running            5 (9m31s ago)   2d18h
prometheus-kube-state-metrics-cc8c6b4df-grqc9            1/1     Running            4 (9m30s ago)   2d18h
prometheus-prometheus-kube-prometheus-prometheus-0       2/2     Running            6 (11m ago)     2d18h
prometheus-prometheus-node-exporter-lt6kc                0/1     CrashLoopBackOff   79 (4m1s ago)   2d18h