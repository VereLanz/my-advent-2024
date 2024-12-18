from pathlib import Path
import shutil
import sys
import webbrowser

from my_advent import YEAR


README_DAILY_TEMPLATE = (
"""### *title* - [Puzzle Page]({aoc_link})
[my code &#8614;](my_advent/day{day_nr}.py)
### Part One
-

### Part Two
-"""
)


def parse_input() -> int:
    if len(sys.argv) < 2 or not sys.argv[1].isdigit():
        raise ValueError(
            "One command line argument in the form of an integer "
            "representing the day of December for AoC has to be provided."
        )
    
    # day must be between 1 and 25
    day_nr = int(sys.argv[1])
    if not 1 <= day_nr <= 25:
        raise ValueError("The provided day number must be between 1 and 25!")
    return day_nr


def create_day_file(location: Path, day_nr: int):
    shutil.copy(
        location / "my_advent" / "day_template.py",
        location / "my_advent" / f"day{day_nr}.py",
    )


def create_day_test_file(location: Path, day_nr: int):
    # copy and adapt test_template for new day
    with open(location / "tests" / "test_template.py", "r") as template:
        test_content = template.read()
        test_content = test_content.replace(".day_template", f".day{day_nr}")
        with open(location / "tests" / f"test_day{day_nr}.py", "w") as test_day:
            test_day.write(test_content)


def rewrite_readme_for_new_day(location: Path, aoc_url: str, day_nr: int):
    # edit readme.me to add daily text template
    day_readme = README_DAILY_TEMPLATE.format(aoc_link=aoc_url, day_nr=day_nr)
    with open(location / "README.md", "r+") as readme:
        readme_content = readme.readlines()
        try:
            # should all exist for 1 to 25
            day_idx = readme_content.index(f"## Day {day_nr}\n")
            # in case it is rerun, but readme was already updated for that day
            if not readme_content[day_idx + 1].startswith("###"):
                readme_content.insert(day_idx + 1, day_readme)
        except ValueError:
            # if for some reason key was not found, rewrite readme as it was
            pass
        # new text will always be longer or same as before, so no truncate needed
        readme.seek(0)
        readme.writelines(readme_content)


if __name__ == "__main__":
    day_nr = parse_input()
    here = Path(__file__).parent
    aoc_url = f"https://adventofcode.com/{YEAR}/day/{day_nr}"

    create_day_file(here, day_nr)
    create_day_test_file(here, day_nr)
    rewrite_readme_for_new_day(here, aoc_url, day_nr)

    # open challenge of the day in webbrowser (needs BROWSER env var in WSL!)
    # also print link for re-use or in case browser did not open (e.g. WSL settings)
    print(aoc_url)
    webbrowser.open(aoc_url)
    