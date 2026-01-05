# NFL Quarterback Hand Size Analysis

## Introduction

Within NFL scouting and player evaluation, quarterback hand size has long been regarded as an important physical trait. The prevailing rationale is that larger hands improve grip and ball control, which may enhance throwing performance, particularly in cold-weather conditions where passing becomes more difficult. This belief is often emphasized by teams located in northern or outdoor stadium environments, especially during late-season play.

This project investigates whether quarterback hand size is meaningfully associated with on-field performance, with particular attention to performance under adverse weather conditions. The analysis leverages publicly available performance metrics—including Pro Football Focus (PFF) grades, ball security measures, and deep passing tendencies—to evaluate both overall performance and context-dependent outcomes.

## View Final Presentation

Go into the repo and select "Relationship Between Hand Sizes of Quarterbacks and Performance.pdf" to view the final presentation

---

## Data and Methodology

The analysis focuses on quarterbacks who participated in the 2023 NFL season. For each quarterback, hand size measurements were collected alongside weekly performance metrics. Separately, game-level weather data, including temperature and wind speed, were compiled for all regular-season games. A unique game identifier was used to merge quarterback performance data with corresponding weather conditions.

Quarterbacks were categorized into three hand-size groups:

- **Small:** ≤ 9.25 inches  
- **Medium:** 9.25–9.75 inches  
- **Large:** ≥ 9.75 inches  

For each category, scatter plots were constructed with game temperature (°F) on the X-axis and selected performance metrics on the Y-axis. This structure enabled a comparative analysis of performance trends across weather conditions. The initial hypothesis was that quarterbacks with larger hands would exhibit less performance variability in colder temperatures, while quarterbacks with smaller hands might show greater sensitivity to adverse weather.

Data collection, cleaning, and integration posed several challenges, particularly in aligning performance metrics with environmental conditions. Additionally, the relatively limited sample size constrained the ability to draw statistically significant causal conclusions, positioning this study as exploratory in nature.

---

## Historical Analysis

In addition to performance-based analysis, the study examined historical draft trends to assess whether NFL teams’ valuation of quarterback hand size has changed over time. By analyzing the distribution of quarterback hand sizes across draft years, the project aimed to identify shifts in scouting preferences and drafting behavior related to this physical attribute.

---

## Results

Across all hand-size groups, the analysis revealed no clear or consistent relationship between quarterback hand size and performance under varying weather conditions. None of the groups demonstrated a statistically discernible trend suggesting that hand size directly influences quarterback effectiveness in cold or adverse environments.

However, a secondary observation emerged: quarterbacks with larger hands appeared more frequently among the highest PFF grades in colder games. In contrast, quarterbacks with smaller hands were rarely represented among top-graded performances in these conditions. While this pattern does not establish causation, it suggests a modest association that may influence evaluative perceptions rather than directly determine performance outcomes.

---

## Conclusion

The findings of this study challenge the long-standing assumption that quarterback hand size is a critical determinant of performance, even in cold-weather contexts. While theoretical arguments favoring larger hands are intuitive, the empirical evidence from the 2023 season does not support a strong or consistent relationship between hand size and overall quarterback performance.

Although quarterbacks with larger hands are slightly overrepresented among elite performances in colder games, the absence of a broader trend suggests that hand size alone is insufficient as a predictive metric. Instead, quarterback success appears to be driven by a combination of technical skill, decision-making, preparation, and situational factors.

Future work incorporating larger datasets across multiple seasons and more rigorous statistical testing would be required to further evaluate these findings and determine whether the observed nuances persist over time.

---

## References

1. Pro Football Reference  
2. Mock Draft Database  
3. Wunderground  
4. Pro Football Focus  
