## Summary

### Two Strata Layers
1. Audiomoth device (given it contains enough clips)
2. Time of day (0-23)

---

#### Reasoning behind Strata Layer 1

As the repo states, looks like `[AM-21, AM-19, AM-28]`are not found in the CSV.
- However, the GitHub repo notes that `AM-8`has problems but just by looking at the CSV alone, it looks functional (i.e. contains meaningful data). AM-8 is inlcuded in the strata layer.

`[AM-12,AM-13,AM-18]` were not included as groups in the first strata layer becuase they contained less than a couple hundred clips collectively. Only those with more than 2000 clips were added to the first layer. 

**First Layer:** `['AM-1', 'AM-10', 'AM-11', 'AM-14', 'AM-15', 'AM-16', 'AM-17','AM-2', 'AM-20', 'AM-22', 'AM-23', 'AM-24', 'AM-25', 'AM-26','AM-27', 'AM-29', 'AM-3', 'AM-30', 'AM-4', 'AM-5', 'AM-6', 'AM-7','AM-8', 'AM-9', 'WWF-1', 'WWF-2', 'WWF-3', 'WWF-4', 'WWF-5']`

**Total of 29 Groups**

---

#### Reasoning behind Strata Layer 2

I noticed the `Comments` column contains the time of day that the audio was recorded. I used .split() method to extract the hour mark, resulting in 24 groups.

---

#### Stratified groups

29 successful audiomoths * 24 hours = 696 combos

In total the stratified sampling should return **696 groups**. 
