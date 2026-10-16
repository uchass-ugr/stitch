# Shared code

Code reused across STITCH papers: data access, cleaning, common functions.
Paper-specific analyses live in each paper's own repository (`stitch-<paper>`).

- `R/` — R functions and scripts. Number scripts in the order they run: `01_load.R`, `02_clean.R`…
- `sql/` — queries (e.g. BigQuery / OpenAlex): `01_extract_works.sql`…

Never hard-code paths to restricted data: use `Sys.getenv("STITCH_DATA")`.
