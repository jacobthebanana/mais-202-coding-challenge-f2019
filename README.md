# Jacob's response to the 2019 MAIS 202 Coding Challenge :)
## Dependencies
- Python 3.5 or higher.
- Mathplotlib 3.0 or higher.

## Getting Started (Linux)
Install Mathplotlib using pip3.
```
pip3 install mathplotlib
```

Checkout this repo using git.
```
git clone https://github.com/jacobthebanana/mais-202-coding-challenge-f2019.git
cd mais-202-coding-challenge-f2019
```

Make sure that the current user has write permission to the current directory. Start the script:
```
python3 plot.py
```

Statistics data will be written to the terminal. The script will create a subfolder `output` if it does not exist. The bar chart will be saved as a PNG file named  `output.png` in that folder.

---

## Note
This script will read `home_ownership_data.csv` and `loan_data.csv` from the current directory. It will look for
- `member_id` and `home_ownership` in the first row of `home_ownership_data.csv`, and
- `member_id` and `loan_amnt` in the first row of `loan_data.csv`. 

If any of these columns cannot be found, the script will exit with `ValueError`. As long as the header row is present, changing the order of the columns will not influence the output of this script.

This script is designed to handle an indefinite number of `home_ownership` values. Entries of `loan_data.csv` whose `member_id` could not be found in `home_ownership_data.csv` will be skipped automatically.

---
Jacob

Sep. 7, 2019.
