# Constructing Synthetic Panels

A Python package to estimate poverty transition shares using synthetic panel methodology.

This package is designed to help researchers and academicians estimate transition dynamics—such as movements into and out of poverty—using repeated cross-sectional household survey data. While panel data is often unavailable in many developing country contexts, this tool leverages the synthetic panel approach to construct pseudo-panels from repeated cross sections.

The package simplifies the entire workflow: it automatically constructs synthetic cohorts based on user-specified characteristics, estimates transition shares across states (e.g., from poor to non-poor), and applies bootstrapping to generate confidence intervals for robust inference. It also supports the inclusion of regression-based methods, fixed effects, and survey weights.

By eliminating the need for manual coding and data restructuring, the package makes it easier to analyze poverty dynamics and other socioeconomic transitions using widely available data sources. It is well-suited for empirical research, policy analysis, and academic work focused on poverty, inequality, labor market mobility, and more.

All errors are my own.

---

## Sources / References

This package is adapted from the methodology described in:

**Dang, Hai-Anh H., and Peter F. Lanjouw.**  
*Measuring Poverty Dynamics with Synthetic Panels Based on Repeated Cross Sections.*  
Oxford Bulletin of Economics and Statistics (Wiley Online Library), 2023.  
[https://onlinelibrary.wiley.com/doi/10.1111/obes.12539](https://onlinelibrary.wiley.com/doi/10.1111/obes.12539)

## Installation

```bash
pip install synthetic_panel
```

## Usage

```bash
from synthetic_panel import estimate_transitions
```
[Working example](https://gist.github.com/rohanbjkr/887bd6a44b6e6e20aad5abcef813b84a)

## Recommended Citations

If you use this package in your research or publication, please cite:

The original methodology paper:
```
Dang, Hai-Anh H., and Peter F. Lanjouw. (2023). Measuring Poverty Dynamics with Synthetic Panels Based on Repeated Cross Sections. Oxford Bulletin of Economics and Statistics.
https://doi.org/10.1111/obes.12539
```

This software package:
```
Byanjankar, Rohan. (2025). synthetic_panel: A Python package to estimate poverty transition shares using synthetic panel methodology with bootstrapping (Version 0.1.3). Available at: https://pypi.org/project/synthetic-panel/
```

