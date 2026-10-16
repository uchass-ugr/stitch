# STITCH

**Scientific Teams and InequaliTies: Collaboration and Heterogeneity in Science**
Project PID2024-155412OB-I00, funded by MICIU/AEI/10.13039/501100011033 · [U^CHASS](https://uchass.ugr.es), University of Granada

🌐 Website: <https://uchass-ugr.github.io/stitch/> (also <https://uchass.ugr.es/stitch>)

This is the project repository: the website, shared code and project documentation.
Each paper has **its own repository** (`stitch-<paper>`), created from the U^CHASS template, private until publication and archived on Zenodo with its own DOI.

## What lives where

```
stitch/
├── site/            Quarto website (published automatically to GitHub Pages)
├── code/            Code shared across papers (R/, sql/)
├── data/
│   ├── restricted/  NEVER committed. README explains where the licensed data are and who grants access
│   ├── processed/   Local derived files, ignored by git
│   └── open/        Aggregated data that can be published (CC BY 4.0)
├── docs/            Project documents (data management plan, internal notes)
├── CITATION.cff     How to cite this repository
├── .zenodo.json     Metadata for Zenodo DOIs (funder, grant)
├── LICENSE          MIT, for code
└── LICENSE-data     CC BY 4.0, for data and text
```

> ⚠️ **Elsevier data must never be pushed to GitHub**, not even to a private repo. Point to it with a path in your `.Renviron` (see `.Renviron.example`).
> Any use of the project data must acknowledge STITCH (PID2024-155412OB-I00).

## Editing the website

Everything is plain text. Edit, commit, push: the site rebuilds itself in ~2 minutes.
To preview locally: open `site/` in RStudio or a terminal and run `quarto preview`.

| I want to… | Edit this |
|---|---|
| Add a news item | Copy any file in `site/news/`, rename it `YYYY-MM-DD-short-title.qmd`, edit the header (`title`, `date`, `categories`, `description`) and the text |
| Add a publication | `site/data/publications.bib` (full list, APA) **and** `site/data/outputs.yml` (what shows on the Home page) |
| Add a talk, media piece, podcast | `site/data/outreach.yml` |
| Update a milestone | `site/data/milestones.yml` (`status: done / ongoing / next`, optional `link`) |
| Change a team member | `site/data/team.yml` (photo in `site/assets/img/team/`) |
| Change page texts | `site/project.qmd`, `site/team.qmd`, `site/outputs.qmd`, `site/index.qmd` |
| Change footer or menu | `site/_quarto.yml` |
| Change colours, fonts, layout | `site/styles.scss` (colours at the top) |
| Turn on the soundtrack | `site/index.qmd`: remove the `<!--` and `-->` around the Side B box |
| Edit the genealogy diagram | `site/tools/make_genealogy.py`, then run `python3 tools/make_genealogy.py` from `site/` |

Images in news posts: put the file in `site/assets/img/news/` and write
`![Caption](../assets/img/news/file.png){fig-alt="Description for screen readers"}`.

## Licences

Code: [MIT](LICENSE) · Data and text: [CC BY 4.0](LICENSE-data)
