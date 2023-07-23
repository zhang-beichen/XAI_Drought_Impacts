# Explainable Machine Learning for the Prediction and Assessment of Complex Drought Impacts

**Beichen Zhang**, Fatima K. Abu Salem, Michael J. Hayes, Kelly Helm Smith, Tsegaye Tadesse, Brian D. Wardlow

***The script and demo of the research published in [Science of the Total Environment (STOTEN)](https://www.sciencedirect.com/journal/science-of-the-total-environment)  July 2023.***

## Abstract

> Drought is a common and costly natural disaster with broad social, economic, and environmental impacts. Machine learning (ML) has been widely applied in scientific research because of its outstanding performance on predictive tasks. However, for practical applications like disaster monitoring and assessment, the cost of the model’s failure, especially false negative predictions, might significantly affect society. Stakeholders are not satisfied with or do not “trust” the predictions from a so-called *black box*. The explainability of ML models becomes progressively crucial in studying drought and its impacts. In this work, we propose an explainable ML pipeline using the XGBoost model and SHAP model based on a comprehensive database of drought impacts in the U.S. **The XGBoost models significantly outperformed the baseline models in predicting the occurrence of multi-dimensional drought impacts derived from the text-based Drought Impact Reporter**, attaining an average F2 score of 0.883 at the national level and 0.942 at the state level. The interpretation of the models at the state scale indicates that the Standardized Precipitation Index (SPI) and Standardized Temperature Index (STI) contribute significantly to predicting multi-dimensional drought impacts. **The time scalar, importance, and relationships of the SPI and STI vary depending on the types of drought impacts and locations. The patterns between the SPI variables and drought impacts indicated by the SHAP values reveal an expected relationship in which negative SPI values positively contribute to complex drought impacts. The explainability based on the SPI variables improves the trustworthiness of the XGBoost models.** Overall, **this study reveals promising results in accurately predicting complex drought impacts and rendering the relationships between the impacts and indicators more interpretable. This study also reveals the potential of utilizing explainable ML for the general social good to help stakeholders better understand the multi-dimensional drought impacts at the regional level and motivate appropriate responses.**

## Graphic Abstract

<p align="center">
<img src="src/Graphic_Abstract.png" alt="Graphic Abstract" style="zoom:70%;" />

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

$F_2$ score on the test dataset at the national level:

|         | Agriculture | Economy   | Fire      | Plant & Wildlife | Relief, Response & Restriction | Society \& Public Health | Water Supply \& Quality |
| ------- | ----------- | --------- | --------- | ---------------- | ------------------------------ | ------------------------ | ----------------------- |
| XGBoost | **0.914**   | **0.881** | **0.876** | **0.899**        | **0.889**                      | **0.868**                | **0.856**               |
| RF      | 0.797       | 0.723     | 0.724     | 0.759            | 0.771                          | 0.765                    | 0.733                   |
| LR      | 0.678       | 0.716     | 0.599     | 0.621            | 0.640                          | 0.566                    | 0.592                   |
| SVM     | 0.351       | 0.024     | 0.127     | 0.265            | 0.249                          | 0.117                    | 0.062                   |
| OneR    | 0.248       | 0.123     | 0.094     | 0.083            | 0.164                          | 0.133                    | 0.083                   |

## Interpretation of the XGBoost model of drought impacts related to fire in California

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
@article{zhang2023explainable,
  title={Explainable machine learning for the prediction and assessment of complex drought impacts},
  author={Zhang, Beichen and Salem, Fatima K Abu and Hayes, Michael J and Smith, Kelly Helm and Tadesse, Tsegaye and Wardlow, Brian D},
  journal={Science of The Total Environment},
  pages={165509},
  year={2023},
  publisher={Elsevier}
}
@inproceedings{xgboost_drought_impacts,
	title = {Quantitative Assessment of Drought Impacts Using XGBoost based on the Drought Impact Reporter},
	url = {https://arxiv.org/abs/2211.02768},
	booktitle = {Tackling {Climate} {Change} with {Machine} {Learning} {Workshop}, 34th {Conference} on {Neural} {Information} {Processing} {Systems} ({NeurIPS} 2020)},
	author = {Zhang, Beichen and Salem, Fatima K. Abu and Hayes, Michael J. and Tadesse, Tsegaye},
	year = {2022},
	doi = {10.48550/ARXIV.2211.02768}
}
```

