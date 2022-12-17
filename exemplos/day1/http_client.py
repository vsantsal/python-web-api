import httpx

result = httpx.get("https://example.com/index.html")

print(result.status_code)
print(result.headers)
print(result.content)