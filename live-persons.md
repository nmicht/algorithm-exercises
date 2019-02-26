Person {
  birth:
  death:
}

**What is the year with most people alive?**

Ideas:
- Go year by year and count number of people that live and not death on that year
- Save that in an hash

Improvements:
- do it by people instead of year
- Get the max on the way to avoid the dict


```python
for person in people: // P
  for year in from person.birth to person.death: // N
    year_count[year] += 1
    if max_count < year_count[year]:
      max_count = year_count[year]
      max_year = year
```
P = number of persons
N = years <1900 ... 2000>
This gives a P x N
