run thingsboard on a more powerful server not pi.

i installed on nuc

https://thingsboard.io/docs/user-guide/install/docker/


Login with tenant: tenant@thingsboard.org and password tenant

Logs
docker compose logs -f mytb


curl -v -X POST -d "{\"temperature\": 25}" 192.168.4.44:8080/api/v1/4rhIw7XcVme5uOqYOhbv/telemetry --header "Content-Type:application/json"

docker ps
364a1eb91e7a   thingsboard/tb-postgres   "start-tb.sh"   2 weeks ago   Up 2 weeks   0.0.0.0:1883->1883/tcp, :::1883->1883/tcp, 0.0.0.0:7070->7070/tcp, :::7070->7070/tcp, 0.0.0.0:5683-5688->5683-5688/udp, :::5683-5688->5683-5688/udp, 0.0.0.0:8080->9090/tcp, :::8080->9090/tcp   thingsboard-mytb-1

