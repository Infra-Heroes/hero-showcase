import json, os, http.server
def check():
    out = {}
    try:
        import psycopg2
        c = psycopg2.connect(os.environ["DATABASE_URL"], connect_timeout=5); cur = c.cursor()
        cur.execute("create table if not exists hits(n int)"); cur.execute("insert into hits values (1)")
        c.commit(); cur.execute("select count(*) from hits"); out["postgres"] = {"ok": True, "rows": cur.fetchone()[0]}
    except Exception as e: out["postgres"] = {"ok": False, "err": str(e)[:200]}
    try:
        import pymysql, urllib.parse as u
        p = u.urlparse(os.environ["MYSQL_URL"])
        c = pymysql.connect(host=p.hostname, user=p.username, password=p.password, database=p.path[1:], connect_timeout=5)
        cur = c.cursor(); cur.execute("create table if not exists hits(n int)"); cur.execute("insert into hits values (1)"); c.commit()
        cur.execute("select count(*) from hits"); out["mysql"] = {"ok": True, "rows": cur.fetchone()[0]}
    except Exception as e: out["mysql"] = {"ok": False, "err": str(e)[:200]}
    try:
        import redis
        r = redis.Redis.from_url(os.environ["REDIS_URL"], socket_connect_timeout=5)
        out["redis"] = {"ok": True, "count": r.incr("hits")}
    except Exception as e: out["redis"] = {"ok": False, "err": str(e)[:200]}
    return out
class H(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps(check() if self.path.startswith("/check") else {"up": True}).encode()
        self.send_response(200); self.send_header("content-type","application/json"); self.end_headers(); self.wfile.write(body)
http.server.HTTPServer(("0.0.0.0", 8080), H).serve_forever()
