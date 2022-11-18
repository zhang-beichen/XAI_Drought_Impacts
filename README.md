# Explainable Machine Learning for the Prediction and Assessment of Complex Drought Impacts

*\<Author List\>*

> **Abstract:** Drought is a common and costly natural disaster with broad economic, environmental, and social impacts. To better monitor the intensity, severity, and onset of drought events, artificial intelligence (AI) and machine learning (ML) have been widely and increasingly applied in relative studies because of their outstanding performance on predictive tasks. However, for practical applications like disaster monitoring and assessment, the cost of the model’s failure, especially false negative predictions, might have a significant impact on society. Stakeholders are not satisfied with or do not “trust” the predictions from the models considered as “black boxes”. The explainability of ML models becomes progressively crucial in studying drought and its impacts. Additionally, given the characteristics of drought, it is challenging to quantitatively identify and evaluate complex impacts caused by drought events. Hence, we proposed an explainable ML framework using XGBoost and SHAP based on a comprehensive drought impacts database, the National Drought Mitigation Center’s Drought Impact Reporter, as well as the hydro-meteorological indices in the U.S. 
> The explainability and interpretability of the XGBoost model revealed promising and actionable insight. The precipitation and temperature anomalies were significantly better associated with the impact occurrence than the types of land cover and social vulnerabilities based on the XGBoost models. The information learned from XGBoost and explained by the SHAP tree interpreters revealed consistent patterns of abnormal dryness and different types of impact occurrence at the state level. The patterns of temperature anomalies are more complex and not monotonic. The SHAP interpretations of the effect of both precipitation and temperature anomalies on drought impacts predictions differed markedly across all the states observed in this study. The SHAP interpretations of the effect of both precipitation and temperature anomalies on drought impacts predictions differed markedly across all the states observed in this study. 
> We also experimented with transfer learning by fine tuning models that are well trained at the scale of climate regions to improve prediction in smaller spatial extent such as states within the same climate region. Overall, this study indicates the preliminary success of applying explainable ML to studying drought impacts in the U.S. Our framework would enable stakeholders to better understand the complex drought impacts at the regional level through the explainable ML framework and outputs, and to manipulate the fundamental hydro-meteorological variables for drought impact assessment more efficiently.

<a href="https://arxiv.org/abs/2211.02768"> Preliminary study submit to the NeurIPS workshop</a>

<a href="https://www.climatechange.ai/papers/neurips2020/18"> Video from the Tackling Climate Change with Machine Learning</a>

<a href="https://colab.research.google.com/drive/1EVZ3lJBwahy6STyTpQKA1Hsr-wMLKXLd?usp=sharing">Quick Colab Example <img src="https://colab.research.google.com/assets/colab-badge.svg" height=16px></a>

------

**The explanation of using this repository can be found at [Notes](docs/Notes.md)**.



If you find this study might help your research, please consider citing the following paper

`@inproceedings{xgboost_drought_impacts,`

​	`title = {Quantitative Assessment of Drought Impacts Using XGBoost based on the Drought Impact Reporter},`

​	`doi = {10.48550/ARXIV.2211.02768},`

​	`url = {https://arxiv.org/abs/2211.02768},`

​	`booktitle = {Tackling {Climate} {Change} with {Machine} {Learning} {Workshop}, 34th {Conference} on {Neural} {Information} {Processing} {Systems} ({NeurIPS} 2020)},`

​	`author = {Zhang, Beichen and Salem, Fatima K. Abu and Hayes, Michael J. and Tadesse, Tsegaye},`

​	`publisher = {arXiv},`

​	`year = {2022},`

​	`copyright = {arXiv.org perpetual, non-exclusive license}`
`}`

