# Run log — after-scored

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `campus_life` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.6
- Runs per question: 3, caching off
- When: 2026-09-30 14:52

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| When is the deadline to add a course? | pass | pass | pass |
| For BIOL 160 Cell Biology, is the assessment curved? | pass | pass | pass |
| How often can you change your meal plan tier, and how much time do you have to do so? | pass | pass | pass |
| For ECON 101, how many tests are there and are they all multiple choice? | pass | pass | pass |
| When do study abroad applications open? | pass | pass | pass |

---

## The relevance gate on out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.6. Refused 5 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.787 | refused |
| How do I change the oil in a diesel engine? | 0.923 | refused |
| Who won the 1994 World Cup? | 0.847 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.824 | refused |
| How do I write a for loop in Rust? | 0.877 | refused |

---

## Real output

This is what the system actually produced. Paste the relevant parts
into your README underneath the table — the rubric asks for real
output as text, not a description of it.

### When is the deadline to add a course? — run 1

- Best distance: 0.3111 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_pass_fail_option.txt, advising_registration.txt, course_biol_160.txt, money_jobs.txt

```
You can add a course through the end of the second week (admin_add_drop_deadline.txt).
```

### When is the deadline to add a course? — run 2

- Best distance: 0.3111 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_pass_fail_option.txt, advising_registration.txt, course_biol_160.txt, money_jobs.txt

```
The deadline to add a course is through the end of the second week (admin_add_drop_deadline.txt).
```

### When is the deadline to add a course? — run 3

- Best distance: 0.3111 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_pass_fail_option.txt, advising_registration.txt, course_biol_160.txt, money_jobs.txt

```
You can add a course through the end of the second week (admin_add_drop_deadline.txt).
```

### For BIOL 160 Cell Biology, is the assessment curved? — run 1

- Best distance: 0.2356 (passed the gate)
- Sources retrieved: course_biol_160.txt, course_biol_160_exams.txt, course_cs_340_exams.txt, course_engl_205_exams.txt, course_phys_130_exams.txt

```
For BIOL 160 Cell Biology, the assessment is not curved. 

Source: `course_biol_160_exams.txt` (also mentioned in `course_biol_160.txt`)
```

### For BIOL 160 Cell Biology, is the assessment curved? — run 2

- Best distance: 0.2356 (passed the gate)
- Sources retrieved: course_biol_160.txt, course_biol_160_exams.txt, course_cs_340_exams.txt, course_engl_205_exams.txt, course_phys_130_exams.txt

```
For BIOL 160 Cell Biology, the assessment is not curved. 

Source: `course_biol_160.txt` (and `course_biol_160_exams.txt`)
```

### For BIOL 160 Cell Biology, is the assessment curved? — run 3

- Best distance: 0.2356 (passed the gate)
- Sources retrieved: course_biol_160.txt, course_biol_160_exams.txt, course_cs_340_exams.txt, course_engl_205_exams.txt, course_phys_130_exams.txt

```
No, the assessments for BIOL 160 Cell Biology are not curved (from `course_biol_160_exams.txt` and `course_biol_160.txt`).
```

### How often can you change your meal plan tier, and how much time do you have to do so? — run 1

- Best distance: 0.2435 (passed the gate)
- Sources retrieved: admin_meal_plan_changes.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, dining_the_atrium.txt, dining_the_ridgeway_cafe.txt

```
You can change your meal plan tier once, and you have the first ten days of the semester to do so (from admin_meal_plan_changes.txt).
```

### How often can you change your meal plan tier, and how much time do you have to do so? — run 2

- Best distance: 0.2435 (passed the gate)
- Sources retrieved: admin_meal_plan_changes.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, dining_the_atrium.txt, dining_the_ridgeway_cafe.txt

```
You can change your meal plan tier once, and you have the first ten days of the semester to do so (admin_meal_plan_changes.txt).
```

### How often can you change your meal plan tier, and how much time do you have to do so? — run 3

- Best distance: 0.2435 (passed the gate)
- Sources retrieved: admin_meal_plan_changes.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, dining_the_atrium.txt, dining_the_ridgeway_cafe.txt

```
You can change your meal plan tier once, and you have the first ten days of the semester to do so (admin_meal_plan_changes.txt).
```

### For ECON 101, how many tests are there and are they all multiple choice? — run 1

- Best distance: 0.4727 (passed the gate)
- Sources retrieved: course_cs_210.txt, course_cs_210_exams.txt, course_econ_101.txt, course_econ_101_exams.txt, course_stat_150_exams.txt

```
For ECON 101, there are three tests (two midterms and a final), and they are all multiple choice (Sources: course_econ_101.txt and course_econ_101_exams.txt).
```

### For ECON 101, how many tests are there and are they all multiple choice? — run 2

- Best distance: 0.4727 (passed the gate)
- Sources retrieved: course_cs_210.txt, course_cs_210_exams.txt, course_econ_101.txt, course_econ_101_exams.txt, course_stat_150_exams.txt

```
For ECON 101, there are three tests (two midterms and a final), and they are all multiple choice. 

Sources: `course_econ_101.txt` and `course_econ_101_exams.txt`
```

### For ECON 101, how many tests are there and are they all multiple choice? — run 3

- Best distance: 0.4727 (passed the gate)
- Sources retrieved: course_cs_210.txt, course_cs_210_exams.txt, course_econ_101.txt, course_econ_101_exams.txt, course_stat_150_exams.txt

```
For ECON 101, there are three tests (two midterms and a final), and they are all multiple choice (Sources: `course_econ_101.txt` and `course_econ_101_exams.txt`).
```

### When do study abroad applications open? — run 1

- Best distance: 0.2345 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_study_abroad.txt, advising_registration.txt, study_library_hours.txt

```
Study abroad applications open in October for the following academic year. 

Source: admin_study_abroad.txt
```

### When do study abroad applications open? — run 2

- Best distance: 0.2345 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_study_abroad.txt, advising_registration.txt, study_library_hours.txt

```
Study abroad applications open in October for the following academic year. 

Source: admin_study_abroad.txt
```

### When do study abroad applications open? — run 3

- Best distance: 0.2345 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_study_abroad.txt, advising_registration.txt, study_library_hours.txt

```
Study abroad applications open in October for the following academic year. 

Source: admin_study_abroad.txt
```
