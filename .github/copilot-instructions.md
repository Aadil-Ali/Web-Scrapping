# Copilot Instructions for Web Scrapping Project

## Project Overview
This project is a collection of Python scripts for web scraping, primarily using Selenium. The workspace contains multiple scripts for scraping and automation tasks, and a CSV file for storing scraped data.

## Key Files & Structure
- `scrapping.py`: Main script for scraping workflows. Likely handles data extraction and saving to CSV.
- `selenium_practice.py`, `selenium_project.py`, `Selenium_project2.py`: Selenium-based scripts for browser automation and scraping. Each may target different sites or use cases.
- `Iphone mobile data1.csv`: Output data file for storing scraped results.
- `__pycache__/`: Python bytecode cache, ignore for code changes.

## Developer Workflows
- **Run scripts**: Execute any `.py` file directly with Python. No build step required.
- **Debugging**: Use print statements or Python debuggers (e.g., `pdb`). Selenium scripts may require browser drivers (e.g., ChromeDriver) in PATH.
- **Data output**: Scraped data is saved to CSV. Check `Iphone mobile data1.csv` for results.

## Patterns & Conventions
- Scripts are standalone; no shared modules or package structure.
- Selenium usage: Look for `webdriver`, `find_element`, and browser navigation patterns.
- Data handling: CSV writing/reading is done via Python's `csv` module or pandas.
- No test framework or build system detected; manual script execution is standard.
- Naming: Script names indicate their purpose (practice, project, etc.).

## External Dependencies
- **Selenium**: Ensure `selenium` Python package is installed. May require browser drivers (e.g., ChromeDriver).
- **pandas** (optional): If used for CSV handling, install via `pip install pandas`.

## Example Usage
```powershell
python scrapping.py
python selenium_practice.py
```

## Integration Points
- Scripts may be updated to scrape different sites or data. Update selectors and URLs as needed.
- Output CSV can be used for further analysis or reporting.

## Recommendations for AI Agents
- When adding new scraping logic, follow the pattern in existing scripts.
- Document any new dependencies or required drivers in comments.
- Keep scripts simple and focused; avoid unnecessary abstraction.
- Reference `scrapping.py` for main data flow and CSV handling.

---
For questions or unclear patterns, ask the user for clarification or examples from their workflow.
