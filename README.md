# Starlette

[![Build Status](https://github.com/encode/starlette/actions/workflows/main.yml/badge.svg)](https:***REDACTED***@app.route("/")
async def homepage(request):
    return JSONResponse({"hello": "world"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

For more information, please see the [documentation](https://www.starlette.io/).

## License

Starlette is released under the [BSD 3-Clause License](LICENSE).
