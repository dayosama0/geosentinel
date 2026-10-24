# 3. Literature Review

## 3.1. Research Context

Remote sensing enables repeated territorial observation, but the appearance of unauthorized waste disposal sites differs by material, surrounding land cover, spatial resolution and sensor. The review by Fraternali, Morandini and Herrera González [1] identifies the shortage of standardized benchmarks and the dependence of published methods on particular geographical case studies. Papale et al. [2] demonstrate the range of satellite data applicable to landfill monitoring while stressing that different sensors answer different monitoring questions. These findings motivate an explicit distinction between detecting a visual candidate and proving an unauthorized disposal event.

For the present project the preferred primary task is **bounding-box object detection**: it provides a location in the image and can be connected to a geographic raster. Image classification states whether a whole tile is likely to contain waste, while semantic segmentation identifies individual pixels. Neither task should be confused with legally establishing whether a site is unauthorized. The model is therefore part of a human-reviewed monitoring workflow rather than an automatic enforcement system.

## 3.2. Deep Learning for Detection

Zhou et al. [5] describe SWDet, an anchor-based detector for solid-waste regions with scale- and context-sensitive features, accompanied by the SWAD dataset. Li and Zhang [6] present a multi-scale context fusion network for urban solid-waste detection. These approaches show why waste, as an irregular and visually heterogeneous target, benefits from multi-scale image features. However, their reported performance cannot be transferred to a different geography or sensor without validation. Sun et al. [7] study dumpsite detection from satellite imagery at broad geographical scale and show the feasibility of computer-assisted inspection. Its experimental setting and imagery still differ from any future Kazakh pilot.

The engineering decision is to begin with a comparatively small detector (a YOLO-family implementation subject to software licensing review) and an architecturally different Faster R-CNN baseline. RT-DETR remains an evaluated alternative on paper rather than a committed third training pipeline. Models will be compared under the same independent data protocol using precision, recall, F1, mAP@0.5, mAP@0.5:0.95 and inference time. The methodology does **not** predict which model will win.

## 3.3. Dataset Suitability and Spatial Resolution

**AerialWaste** [3] originally offers 10,434 scenes: 3,478 positive and 6,956 negative. It includes airplane-derived AGEA orthophotos (about 0.2 m GSD), WorldView-3 satellite images (about 0.3 m), and Google Earth scenes (about 0.5 m). Most labels concern presence/absence and site metadata rather than complete boxes for every image; 169 test images include localized masks. It supports scene-level evaluation and negative sampling, but the full set cannot directly be treated as one bounding-box detector training corpus. Its public images are not georeferenced to protect sensitive sites. Later dataset releases must not be mixed with original 2023 counts without identifying the exact version.

**CWLD** [4] comprises 3,653 prepared satellite-derived image/mask pairs centered on construction-waste landfills in two Beijing districts. Authors report 228 original scenes from Changping and 457 from Daxing, expanded by augmentation. The four semantic classes include background, land, construction infrastructure and waste disposal areas. Masks could be converted to boxes, but augmentation-related images must be grouped before train/test splitting. Construction-waste specialization limits its utility for a detector intended to capture varied waste categories.

**SWAD** [5] provides one-class `waste dump` object detection labels. The student audited a distributed SWAD v2 YOLOv8 export containing **1,996** JPEG images at 640 x 640 and **5,562** bounding boxes. The automated scan found no damaged images or invalid bounding boxes. The official train/validation/test partitions contain **1,397 / 399 / 200** images. However, the audit flagged **102** potentially similar cross-split pairs; two manually inspected pairs showed overlapping satellite scenes between train and test. The original partitions cannot be presented as an independent final benchmark. Complete scene grouping, manual box review and imagery/license checks remain unfinished; the audit was not a full legal provenance assessment. The exported JPEG files did not expose embedded GPS/CRS data, which prevents direct map placement without separate georeferencing.

**Platform resolution matters.** Drone photographs can resolve small pieces of litter that are invisible at satellite scale. We deliberately exclude close-range drone images as the primary training or test basis for claims about satellite detection. Even satellite data differ dramatically: commercial high-resolution imagery around 0.3–1 m GSD supports different object scales than freely available Sentinel-2 bands at 10 m. Source, resolution, resampling, acquisition time, label type and class definition must be recorded for each input source.

### 3.3.1. Dataset Comparison

| Property | SWAD (audited v2 export) | AerialWaste (2023 original) | CWLD |
|---|---|---|---|
| Core task | Bounding-box detection | Binary/multilabel image classification, limited masks | Semantic segmentation |
| Size | 1,996 images; 5,562 boxes | 10,434 scenes; 3,478 positive | 3,653 prepared pairs |
| Labels | One waste-dump class and boxes | Mainly image-level tags, 169 masked images | Four-class pixel masks |
| Acquisition | Satellite-compatible images; per-export provenance must be checked | Mixed airborne/WV3/Google Earth | GF-2 and Google Earth |
| Direct YOLO training | Yes, after quality and split fixes | Not for entire dataset without new boxes | Requires mask-to-box conversion |
| Main risk | Confirmed cross-split scene overlap | Mixed sensors, limited box data, rights | Construction focus and augmented relatives |
| Role in project | Primary *candidate* | Selective external checks/negative scenes if permitted | Optional supplemental comparison |

None of these sets alone provides verified georeferenced pilot imagery for Kazakhstan. Satellite data access requests to Kazakhstan Garysh Sapary and Airbus are pending; an alternate legally usable pilot or geospatial raster test must be supported if requests are unsuccessful.

## 3.4. Citizen Science as Complementary Evidence

Citizen participation supplies photographs, observation dates and geographic context not necessarily visible in orbit. Kako et al. [10] demonstrate smartphone-based litter data collection combined with computer vision; they also identify practical filtering limits in crowdsourced observations. Watkins et al. [11], comparing a citizen litter application with municipal audits, found differences in spatial sampling: participation density can reflect where users live rather than where pollution is most frequent. Thus **few reports in an area do not imply the absence of dumping**.

Wu et al. [12] describe PlastOPol, a mobile and collaborative monitoring system for marine litter. It shows the technical feasibility of structured citizen observations and data management, but its subject and observation conditions differ from land-based satellite landfill detection. For this project, crowdsourced photographs are independent supporting evidence, not substitute satellite crops or automatically verified training labels.

## 3.5. Fusion, GIS and Human Verification

Karagiannopoulou et al. [8] review the integration of Earth observation with citizen science data, noting the advantages of complementary sources and challenges of quality, interoperability and uneven sampling. Scharf et al. [9] combine satellite/other geospatial indicators with citizen input to map **susceptibility** to illegal dumping in Dakar; a susceptibility map estimates where waste may be likely, not where an individual detected site is verified to exist. These works support the use of GIS relationships, not an unvalidated environmental risk score.

A transparent engineering strategy is to retain three related but separate concepts: **MonitoredLocation** (site identity under review), **Observation** (satellite prediction or citizen report with provenance and time), and **EvidenceMatch** (a proposed or reviewer-confirmed association). This guards against treating nearby objects as necessarily identical. A verification mission records who examined a candidate, what evidence was available and which decision was made. Thus the intended fusion contribution is reproducible systems integration with traceability, not the discovery of a new academic data-fusion algorithm.

## 3.6. Feedback and Longitudinal Monitoring

The literature highlights data quality and transfer limitations, and the project responds with an integrated **human-in-the-loop** feedback process. Only a reviewed satellite image region with a valid box and permitted license can become a training candidate for the *satellite* detector. A citizen's ground photograph can support a verification decision but is not automatically an eligible satellite training image. A model change requires a versioned dataset, reproducible offline training, independent comparative evaluation and explicit approval; improvement is an empirical result to establish, not an automatic outcome of adding data.

Re-dumping monitoring depends on preserving observations from multiple dates and keeping confirmed cleanup events in the same site's history. A new observation *acquired after* a confirmed cleanup may open an inspection alert, while an old satellite image uploaded later must not. Without temporal reliability, the record should remain uncertain. Automated dense pixelwise change detection is outside the mandatory MVP.

## 3.7. Comparative Scientific Literature Matrix

| Ref. | Study and contribution | Key limitation / implication |
|---|---|---|
| [1] | Fraternali et al. (2024): review of waste detection and monitoring | Fragmented benchmarks; motivates independent evaluation |
| [2] | Papale et al. (2023): satellite landfill monitoring review | Different sensors and tasks; do not equate all spatial resolutions |
| [3] | Torres & Fraternali (2023): AerialWaste diverse mixed-source data | Mostly image-level labels; mixed GSD and sensitive coordinates |
| [4] | Lin et al. (2024): CWLD segmentation dataset | Construction waste only; augmented samples need grouping |
| [5] | Zhou et al. (2023): SWDet and SWAD object detection | Requires audit of distribution and independent splits |
| [6] | Li & Zhang (2024): multi-scale context fusion | Added complexity; comparative gain is unverified in our conditions |
| [7] | Sun et al. (2023): cross-city satellite dumpsite detection | Generalization still relies on sensor/region-specific tests |
| [8] | Karagiannopoulou et al. (2022): EO + citizen data-fusion review | Heterogeneous evidence creates validation challenges |
| [9] | Scharf et al. (2025): GIS, EO and citizen susceptibility mapping | Risk mapping does not verify specific site presence |
| [10] | Kako et al. (2024): mobile litter monitoring and deep learning | Ground-level data can be sparse and noisy |
| [11] | Watkins et al. (2024): municipal audits vs citizen app | Participation geography may bias observed distribution |
| [12] | Wu et al. (2023): PlastOPol citizen marine litter system | Different waste context and no satellite-to-citizen match proof |

## 3.8. Conclusions for Design

The principal design consequences are: (1) use object detection for image-localized satellite candidates; (2) separate classifier, detector and segmentation annotation requirements; (3) audit datasets before model selection, especially scene leakage; (4) use suitable, legally permitted and georeferenced imagery for the pilot; (5) preserve original citizen and satellite observations, timestamps and provenance; (6) support inspector verification and possible re-dumping follow-up; and (7) gate model improvements behind reviewed examples and independent evaluation.

The research shows feasibility of relevant components, **not** proof that the integrated Balanced MVP v2.0 has been implemented or that it will outperform existing institutional systems.

## References (12 peer-reviewed publications)

[1] P. Fraternali, L. Morandini and S. L. Herrera González, “Solid waste detection, monitoring and mapping in remote sensing images: A survey,” *Waste Management*, vol. 189, pp. 88–102, 2024. https://doi.org/10.1016/j.wasman.2024.08.003

[2] L. G. Papale, G. Guerrisi, D. De Santis, G. Schiavon and F. Del Frate, “Satellite Data Potentialities in Solid Waste Landfill Monitoring: Review and Case Studies,” *Sensors*, vol. 23, no. 8, 3917, 2023. https://doi.org/10.3390/s23083917

[3] R. N. Torres and P. Fraternali, “AerialWaste dataset for landfill discovery in aerial and satellite images,” *Scientific Data*, vol. 10, 63, 2023. https://doi.org/10.1038/s41597-023-01976-9

[4] S. Lin, L. Huang, X. Liu, G. Chen and Z. Fu, “A construction waste landfill dataset of two districts in Beijing, China from high resolution satellite images,” *Scientific Data*, vol. 11, 388, 2024. https://doi.org/10.1038/s41597-024-03240-0

[5] L. Zhou et al., “SWDet: Anchor-Based Object Detector for Solid Waste Detection in Aerial Images,” *IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing*, vol. 16, pp. 306–320, 2023. https://doi.org/10.1109/JSTARS.2022.3218958

[6] Y. Li and X. Zhang, “Multi-Scale Context Fusion Network for Urban Solid Waste Detection in Remote Sensing Images,” *Remote Sensing*, vol. 16, no. 19, 3595, 2024. https://doi.org/10.3390/rs16193595

[7] X. Sun et al., “Revealing influencing factors on global waste distribution via deep-learning based dumpsite detection from satellite imagery,” *Nature Communications*, vol. 14, 1444, 2023. https://doi.org/10.1038/s41467-023-37136-1

[8] A. Karagiannopoulou, A. Tsertou, G. Tsimiklis and A. Amditis, “Data Fusion in Earth Observation and the Role of Citizen as a Sensor: A Scoping Review of Applications, Methods and Future Trends,” *Remote Sensing*, vol. 14, no. 5, 1263, 2022. https://doi.org/10.3390/rs14051263

[9] N. Scharf, B. Ducry, B. Sy, A. Djim and P. Lacroix, “Integrating Remote Sensing, GIS, and Citizen Science to Map Illegal Waste Dumping Susceptibility in Dakar, Senegal,” *Sustainability*, vol. 17, no. 24, 11137, 2025. https://doi.org/10.3390/su172411137

[10] S. Kako, R. Muroya, D. Matsuoka and A. Isobe, “Quantification of litter in cities using a smartphone application and citizen science in conjunction with deep learning-based image processing,” *Waste Management*, vol. 186, pp. 271–279, 2024. https://doi.org/10.1016/j.wasman.2024.06.026

[11] L. Watkins, D. N. Bonter, P. J. Sullivan and M. T. Walter, “Methods for monitoring urban street litter: a comparison of municipal audits and an app-based citizen science approach,” *Environmental Science: Advances*, vol. 3, pp. 885–896, 2024. https://doi.org/10.1039/D4VA00008K

[12] D. Wu et al., “The PlastOPol system for marine litter monitoring by citizen scientists,” *Environmental Modelling & Software*, vol. 169, 105784, 2023. https://doi.org/10.1016/j.envsoft.2023.105784
