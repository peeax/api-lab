# api-lab

API tests for QuickPizza (https://quickpizza.grafana.com) with pytest and requests.
ITDS362 Software Quality Assurance and Testing.

## How to install and run

    python -m venv .venv
    .venv\Scripts\activate
    pip install -r requirements.txt
    pytest -v

On macOS and Linux, use `python3` and `source .venv/bin/activate`.

## Input domain model for POST /api/ratings

| Characteristic | Blocks | Values in the tests |
|---|---|---|
| C1 Value of stars | below 1, 1 to 5 (base), above 5 | 0, 3, 6 |
| C2 Type of stars | whole number (base), decimal, text, missing | 3, 3.5, "3", no field |
| C3 Pizza | exists (base), does not exist | a new pizza, 999999999 |
| C4 Token | the user's own (base), none, wrong length | from auth, no header, token short |

### Tests that cover each block

| Block | Test |
|---|---|
| Base choice (3 stars, whole number, real pizza, own token) | test_base_choice_is_saved |
| C1 below 1 | test_stars_out_of_range[0] |
| C1 above 5 | test_stars_out_of_range[6] |
| C2 decimal | test_stars_wrong_type[decimal] |
| C2 text | test_stars_wrong_type[text] |
| C2 missing | test_stars_missing |
| C3 does not exist | test_pizza_does_not_exist |
| C4 none | test_token_not_valid[no_token] |
| C4 wrong length | test_token_not_valid[wrong_length] |