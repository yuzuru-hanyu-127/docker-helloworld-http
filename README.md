# docker-helloworld-http

A Python HTTP server which responds to any GET or HEAD request with an HTTP 200.

## Usage

Start the server, listening for traffic on port 6666 of localhost:

```sh
docker run -it -p 1236:6666 -e PORT=6666 laser/helloworld-http:latest
```

```sh
15:47 $ curl -I 'http://localhost:1234/foo'
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.6.3
Date: Tue, 02 Jan 2018 23:47:36 GMT
```

```sh
15:59 $ curl -I 'http://localhost:1236/foobar'
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.6.3
Date: Wed, 03 Jan 2018 00:00:19 GMT
```
