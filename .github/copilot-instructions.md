# Copilot Instructions

## Build, test, and automation commands

This repository is a course site with content-generation scripts, not a single deployable application.

### Repository-level automation

- `npm run release:ci` - Regenerates chapter header images via `.github/scripts/generate-chapter-headers.py`.
- `npm run release` - Full demo asset pipeline: creates `.tape` files, renders demo GIFs, then verifies them.
- `npm run create:tapes` - Rebuilds chapter `images/*.tape` files from `.github/scripts/demos.json`.
- `npm run generate:vhs -- --chapter 03` - Regenerates demo GIFs for one chapter.
- `npm run generate:vhs -- --file 03-development-workflows\\images\\some-demo.tape` - Regenerates one demo.
- `npm run verify:gifs` - OCR-checks generated demo GIFs for incomplete runs.

### Primary sample app (`samples\\book-app-project`)

- `cd samples\\book-app-project && python book_app.py help` - Show the CLI commands used throughout the course.
- `cd samples\\book-app-project && python -m pytest tests` - Run the full Python sample test suite.
- `cd samples\\book-app-project && python -m pytest tests\\test_books.py` - Run one test file.
- `cd samples\\book-app-project && python -m pytest tests\\test_books.py -k test_add_book` - Run one named test.

There is currently no dedicated lint script in `package.json` or `samples\\book-app-project\\pyproject.toml`.

## High-level architecture

- `00-quick-start` through `07-putting-it-together` are the course chapters. Each chapter is reader-facing content, not application code.
- `samples\\book-app-project` is the canonical project for examples across the course. It is a small Python CLI split into:
  - `book_app.py` for command dispatch and console interaction
  - `books.py` for the `Book` dataclass plus JSON-backed collection logic
  - `utils.py` for validated input helpers used by the CLI
  - `tests\\` for pytest coverage of both data logic and command flows
- `samples\\book-app-project-cs` and `samples\\book-app-project-js` are alternate-language variants, but the main course examples should still point to the Python sample unless there is a strong reason not to.
- The live Copilot configuration used by this repository is under `.github\\agents`, `.github\\skills`, and `.github\\instructions`. The matching `samples\\agents`, `samples\\skills`, and `samples\\mcp-configs` directories are teaching examples that mirror those concepts for learners.
- `.github\\scripts` contains the content automation pipeline. `create-tapes.js` converts `.github\\scripts\\demos.json` into chapter tape files, `generate-demos.js` runs VHS to produce demo GIFs, and `verify-gifs.js` checks the rendered output. `generate-chapter-headers.py` separately regenerates chapter header images.

## Key conventions

- Treat this repository as educational content first. When changing examples or explanations, keep them beginner-friendly and explain AI/ML terms if they appear.
- Use `samples\\book-app-project\\...` paths in primary examples and keep the default coding context Python + pytest.
- Keep shell examples copy-paste ready. Existing docs favor concise command blocks that learners can run directly.
- Do not "fix" code in `samples\\book-app-buggy` or `samples\\buggy-code`; those bugs are intentional for exercises.
- If you add or rename chapter content, update the course table in `README.md` so the learning path stays in sync.
- When editing Python sample code or its tests, preserve the existing style: Python 3.10+ type hints, JSON file persistence in `books.py`, and pytest tests organized with fixtures, focused test functions, and `@pytest.mark.parametrize` where it helps.
