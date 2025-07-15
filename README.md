# synthetic_panel

# synthetic_panel

A Python package to estimate poverty transition shares using synthetic panel methodology with bootstrapping.

---

## Source / Reference

This package is adapted from the methodology described in:

**Dang, Hai-Anh H., and Peter F. Lanjouw.**  
*Measuring Poverty Dynamics with Synthetic Panels Based on Repeated Cross Sections.*  
Oxford Bulletin of Economics and Statistics (Wiley Online Library), 2023.  
[https://onlinelibrary.wiley.com/doi/10.1111/obes.12539](https://onlinelibrary.wiley.com/doi/10.1111/obes.12539)

## Installation

```bash
pip install --index-url https://test.pypi.org/simple/ synthetic_panel
```

## Usage

```bash
from synthetic_panel import estimate_transitions
```
```bash
bootstrap_results = estimate_transitions(
    df_round1=df1,
    df_round2=df2,
    x_cols=['x1', 'x2', 'x31', 'x32', 'age33'],    # predictors in regression
    cohort_cols=['x1', 'x2','x3'],          # used to form cohort IDs
    dep_var_round1='depvar1',                                   # dependent var in round1
    dep_var_round2='depvar2',                                    # dependent var in round2
    pline_round1_col=None,                                    # will auto-calc using df2010['pline_7']
    pline_round2_col='cutoffline',                                 # poverty line col in df2021
    cohort_col='cohort',                                      # cohort ID column name
    auto_create_cohort=True,                                  # create cohort from cohort_cols
    log_transform=False,                                       # log-transform dependent vars
    n_bootstrap=2,                                          # number of bootstrap reps
    use_multiprocessing=True,                                 # use parallel processing
    output_excel_filename="bootstrap_poverty_transitions.xlsx",  # save Excel file in current dir
    seed=42                                                   # random seed for reproducibility
)

print(bootstrap_results.head())
