# Explainable Machine Learning for the Prediction and Assessment of Complex Drought Impacts

*\<Author List\>*

> **Abstract:** Drought is a common and costly natural disaster with broad economic, environmental, and social impacts. To better monitor the intensity, severity, and onset of drought events, artificial intelligence (AI) and machine learning (ML) have been widely and increasingly applied in relative studies because of their outstanding performance on predictive tasks. However, for practical applications like disaster monitoring and assessment, the cost of the model’s failure, especially false negative predictions, might have a significant impact on society. Stakeholders are not satisfied with or do not “trust” the predictions from the models considered as “black boxes”. The explainability of ML models becomes progressively crucial in studying drought and its impacts. Additionally, given the characteristics of drought, it is challenging to quantitatively identify and evaluate complex impacts caused by drought events. Hence, we proposed **an explainable ML framework using XGBoost and SHAP based on a comprehensive drought impacts database**, the National Drought Mitigation Center’s Drought Impact Reporter, as well as the hydro-meteorological indices in the U.S.
>
> The explainability and interpretability of the XGBoost model revealed promising and actionable insight. The precipitation and temperature anomalies were significantly better associated with the impact occurrence than the types of land cover and social vulnerabilities based on the XGBoost models. **The information learned from XGBoost and explained by the SHAP tree interpreters revealed consistent patterns of abnormal dryness and different types of impact occurrence at the state level. The patterns of temperature anomalies are more complex and not monotonic. The SHAP interpretations of the effect of both precipitation and temperature anomalies on drought impacts predictions differed markedly across all the states observed in this study. ** 
> 
> We also experimented with **transfer learning by fine tuning models that are well trained at the scale of climate regions** to improve prediction in smaller spatial extent such as states within the same climate region. **Overall, this study indicates the preliminary success of applying explainable ML to studying drought impacts in the U.S. Our framework would enable stakeholders to better understand the complex drought impacts at the regional level through the explainable ML framework and outputs, and to manipulate the fundamental hydro-meteorological variables for drought impact assessment more efficiently.

<a href="https://arxiv.org/abs/2211.02768"> Preliminary study submitted to the NeurIPS 2020 workshop</a>

<a href="https://www.climatechange.ai/papers/neurips2020/18"> Video from the Tackling Climate Change with Machine Learning</a>

<a href="https://colab.research.google.com/drive/1EVZ3lJBwahy6STyTpQKA1Hsr-wMLKXLd?usp=sharing">Quick Colab Example <img src="https://colab.research.google.com/assets/colab-badge.svg" height=16px></a>

------

**The explanation of using this repository can be found at [Notes](docs/Notes.md)**.

## Seven types of drought impacts


| Category                           | Defination                                                   |
| ---------------------------------- | ------------------------------------------------------------ |
| **Agriculture**                    | Drought effects associated with agriculture, farming,  aquaculture, horticulture, forestry, and ranching |
| **Economy**                        | - **Energy**: Drought effects associated with power production, electricity rates, energy revenue, and  purchase of alternate sources of energy.<br />- **Business \& Industry**: Drought effects associated with non-ag businesses. <br />- **Tourism \& Recreation**: Drought effects associated with recreational activities and tourism. |
| **Fire**                           | Drought effects associated with forest, range, and urban fires during drought events. |
| **Plant & Wildlife**               | Drought effects associated with wildlife, fisheries, forests, and other fauna. |
| **Relief, Response & Restriction** | Drought effects associated with disaster declarations, aid programs, requests for disaster declaration or aid, water restrictions, and fire restrictions. |
| **Society \& Public Health**       | Drought effects associated with changes in public behavior and human health effects. |
| **Water Supply \& Quality**        | Drought effects associated with surface or subsurface water supplies. |

## Performance of XGBoost on predicting drought impacts

F2 score on the test dataset at national level:

|         | Agriculture | Economy   | Fire      | Plant & Wildlife | Relief, Response & Restriction | Society \& Public Health | Water Supply \& Quality |
| ------- | ----------- | --------- | --------- | ---------------- | ------------------------------ | ------------------------ | ----------------------- |
| XGBoost | **0.914**   | **0.868** | **0.876** | **0.899**        | **0.889**                      | **0.868**                | **0.856**               |
| RF      | 0.797       | 0.723     | 0.724     | 0.759            | 0.771                          | 0.765                    | 0.733                   |
| LR      | 0.678       | 0.716     | 0.599     | 0.621            | 0.640                          | 0.566                    | 0.592                   |
| SVM     | 0.351       | 0.024     | 0.127     | 0.265            | 0.249                          | 0.117                    | 0.062                   |
| OneR    | 0.248       | 0.123     | 0.094     | 0.083            | 0.164                          | 0.133                    | 0.083                   |

## Interpretation of the XGBoost model of drought impacts on fire in California

<p align="center">
<img src="src/CA_FIRE_SHAP_SPI.png" alt="Interpretation of the SPI from the model" style="zoom:12%;" />

<img src="src/CA_FIRE_SHAP_STI.png" alt="Interpretation of the STI from the model"
style="zoom:12%;" />

<img src="src/CA_FIRE_SHAP_LC.png" alt="Interpretation of the land cover from the model" 
style="zoom:12%;" />

<img src="src/CA_FIRE_SHAP_SVI.png" alt="Interpretation of the SVI from the model" 
style="zoom:12%;" />

*Illustration of the interpretations from the SHAP values is thoroughly discussed in the article.*

## Citation


If you find this study might help your research, please consider citing the following paper:

```tex
@inproceedings{xgboost_drought_impacts,
	title = {Quantitative Assessment of Drought Impacts Using XGBoost based on the Drought Impact Reporter},
	url = {https://arxiv.org/abs/2211.02768},
	booktitle = {Tackling {Climate} {Change} with {Machine} {Learning} {Workshop}, 34th {Conference} on {Neural} {Information} {Processing} {Systems} ({NeurIPS} 2020)},
	author = {Zhang, Beichen and Salem, Fatima K. Abu and Hayes, Michael J. and Tadesse, Tsegaye},
	year = {2022},
	doi = {10.48550/ARXIV.2211.02768}
}
```

