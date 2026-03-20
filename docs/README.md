# Requirements

- Have UV installed

---

# How To Use

- Run with `uv run -m src`.

## For Accenture Only

Your devices are sometimes cloud managed, so you need to prefix UV command with
`$env:UV_LINK_MODE="copy"`

So to run the project you would use
```sh
$env:UV_LINK_MODE="copy"
uv run -m src
```
