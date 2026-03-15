A Python + Playwright script to download past exam papers and marking schemes from the State Examinations Commission (SEC) archive. Because life's too short to click through that website.

> **Note:** Currently configured for **Leaving Cert English (Higher Level)**. See [Customisation](#customisation) below to change subject or level.

---

## Why?

The [SEC examinations archive](https://www.examinations.ie/exammaterialarchive/) makes it unnecessarily tedious to find and download past papers. This script automates the entire process — just tell it what you want and it opens the file directly in your browser.

---

## Requirements

- Python 3.8+
- [Playwright for Python](https://playwright.dev/python/)

### Install dependencies

```bash
pip install playwright
playwright install chromium
```

---

## Usage

Run the script and enter a string when prompted in the format:

```
eYYYY1  →  Exam paper, year, paper number
mYYYY2  →  Marking scheme, year, paper number
```

### Format breakdown

| Position | Value | Meaning |
|---|---|---|
| 1st character | `e` | Exam paper |
| 1st character | `m` | Marking scheme |
| Characters 2–5 | `YYYY` | Year (e.g. `2023`) |
| Last character | `1` or `2` | Paper 1 or Paper 2 |

### Examples

```bash
python Download_exam.py
```

Then enter one of the following when prompted:

```
e20231    →  2023 Exam Paper 1
e20232    →  2023 Exam Paper 2
m20231    →  2023 Marking Scheme
```

The script will launch a Chromium browser, navigate to the SEC archive, accept the terms, apply your selections, and open the requested file in a new tab. The browser stays open so you can view or save the document.

To exit, press `Ctrl+C` in the terminal.

---

## Customisation

The script is currently hardcoded for **Leaving Cert Maths (Higher Level)**. To change this, edit the following lines in `Download_exam.py`:

### Change the exam type (LC / JC / LCA)

```python
page.select_option('select[name="...ExaminationSelect"]', value="lc")
# Options: "lc" (Leaving Cert), "jc" (Junior Cert), "lca" (LCA)
```

### Change the subject

```python
page.select_option('select[name="...SubjectSelect"]', value="3")
# value="3" is Maths — inspect the SEC archive dropdowns to find your subject's value
```

### Change the level (Higher / Ordinary / Foundation)

```python
paper_name = "Paper One / Higher Level (EV)"
# Replace "Higher Level" with "Ordinary Level" or "Foundation Level" as needed
```

---

## Notes

- The browser opens visibly by default (`headless=False`). To run it in the background, change this to `headless=True` in `Download_exam.py`.
- This script is intended for personal and educational use only.
- All content belongs to the State Examinations Commission.

---
