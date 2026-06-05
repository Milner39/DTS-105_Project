# Requirements

- Have UV installed

---

# How To Use

If you are not using UV (not recomended) replace `uv run` with `python`.

Run with:
```sh
uv run -m src`
```

## Seeding Test Data

Overwrite the **previous calendar month** with a variety of generated mood logs
(varied scores, notes and unlogged gap days) for testing the calendar, stats
and graph:

```sh
uv run -m src.database.seed
```

This only touches the previous month's logs (other months are left untouched)
and is safe to re-run.

A constant `seed` is used so that logs are random, but produce the same result
every run, unless the seed is changed.

## For Accenture Only

Your devices are sometimes cloud managed, so you need to prefix UV command with
`$env:UV_LINK_MODE="copy"`

So to run the project you would use
```sh
$env:UV_LINK_MODE="copy"
uv run -m src
```
