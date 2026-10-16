# Restricted data — not in this repository

The STITCH dataset (CRediT contribution statements) is licensed from **Elsevier** to the University of Granada for the project of N. Robinson-Garcia and the direct members of his team (Elsevier Data Agreement, 30 Sept 2024, and amendment).

- **Never commit these files**, in this or any other repository, public or private.
- **Where they are:** on University of Granada storage managed by the PI.
- **Access:** ask Nicolás Robinson-García. Access is limited to STITCH team members.
- **In your code:** read the path from an environment variable, e.g. in R:

  ```r
  path <- Sys.getenv("STITCH_DATA")   # set in your .Renviron (see .Renviron.example)
  ```

- **Acknowledgement:** any use of these data must acknowledge the STITCH project (PID2024-155412OB-I00).
- What can be shared openly: aggregated, derived data that do not allow reconstructing the original records → `data/open/`.
