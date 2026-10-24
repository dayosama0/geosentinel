# 1. Project Proposal

## 1.1. Identification

**Approved title:** Development of a system for detecting and monitoring the locations of unauthorized landfills based on the analysis of satellite images and crowdsourcing.

**Student:** Ali Turaliyev, Software Engineering, SE-2430, Astana IT University.

**Scientific supervisor:** Aldiyar Salkenov.

**Project type:** Individual software engineering diploma project. The first pre-defense is scheduled for 24 October 2026; the final defense date remains subject to the university schedule.

## 1.2. Problem and Motivation

Unauthorized waste dumping is a persistent environmental-management problem in Kazakhstan. Satellite monitoring enables potential dumping locations to be identified across territories that would otherwise require extensive field inspection. According to Kazakhstan's official communication, satellite monitoring detected **2,637** unauthorized dumping locations by September 2026, of which **2,213** were reported as eliminated [P1]. These figures describe official monitoring outcomes; they are not model accuracy measurements. A separate official prosecution report from Abai Region described **80 locations** whose coordinates matched places recorded in 2023 among newly detected sites in late 2024 [P2]. Identical coordinates alone do not prove a site was never cleaned, but they justify monitoring the same location over time.

Existing services already offer meaningful capabilities: Kazakhstan Garysh Sapary operates satellite waste monitoring with GIS tools and field applications [P3], while TazaQazBot and TazaQala accept citizen reports and maintain processing statuses [P4], [P5]. This project focuses on the link between satellite detections, citizen reports, verification tasks and the subsequent history of each monitored location. Its performance can then be evaluated at both the detection and workflow levels.

## 1.3. Target Users

**Primary intended users:** environmental inspectors, environmental protection and supervisory authorities, and similarly authorized analysts who need to triage suspected dumping locations and review evidence. The proposed roles reflect publicly documented environmental inspection workflows.

**Secondary users:** citizens and volunteers contributing geolocated photographs and the observation date through a mobile-first reporting interface. **Technical role:** an administrator/ML operator managing approved satellite training examples and reproducible model evaluation.

## 1.4. Aim

To design, implement, and evaluate a geospatial prototype that detects potential unauthorized waste dumping locations in suitable high-resolution satellite imagery and connects these detections with crowdsourced reports, inspector verification, controlled model improvement, and repeated site monitoring.

## 1.5. Objectives

1. Examine the relevant research, publicly documented monitoring systems, imagery sources, and their constraints.
2. Audit and prepare suitable satellite-compatible annotated data; establish independent training and test partitions.
3. Implement and evaluate a bounding-box **Object Detection** component against a defined baseline.
4. Build a geospatial data model and map that preserve the source, location, acquisition/observation time, and model version for each observation.
5. Provide a mobile-first citizen report form and an inspector-oriented dashboard.
6. Implement candidate **Evidence Fusion** and **Smart Verification Missions**, with authorized review rather than irreversible automatic merging.
7. Add **Re-Dumping Alerts** using newly observed evidence after a recorded confirmed cleanup, with a repeat-inspection decision.
8. Implement **Continuous Model Improvement** as verified satellite-example review, versioned export, offline retraining and explicit selection of an evaluated model.
9. Verify the implementation with detection metrics, geospatial control tests, evidence-matching tests, functional/security cases and an integrated demonstration.

## 1.6. Expected Outcomes

The intended outputs are: (i) documented requirements, architecture, UX and risk plan; (ii) a reproducible detection baseline and candidate model comparison; (iii) a licensed georeferenced-pilot imagery workflow when appropriate imagery is available; (iv) a mobile-first PWA and inspector dashboard; (v) persistent monitored locations with linked but independent observations; (vi) verification missions and historically traceable decisions; (vii) reinspection alerts triggered by eligible post-cleanup evidence; (viii) a gated satellite training-data/model-update workflow; and (ix) recorded evaluation results and limitations.

The first pre-defense covers the analysis and design stage, including a dataset audit, diagrams, UX prototype and evaluation plan. Implementation and integrated testing follow in subsequent stages.

## 1.7. Balanced MVP v2.0 Scope

**Included:** one-class or appropriately harmonized waste-dump bounding-box detection; ingestion of valid georeferenced GeoTIFF imagery; image-to-world coordinate transformation; location/observation records in PostGIS; a responsive citizen report interface; site map and inspector dashboard; geographic candidate matching with human decision; mission states and evidence attachment; cleanup events and temporally guarded re-dumping alerts; reviewed satellite annotations, dataset manifest, repeatable offline retraining/evaluation and explicit model-version choice.

**Conditional:** comparison of two co-registered satellite dates for the same location when suitably licensed and compatible acquisitions are actually available. The selected pilot region is determined **after** confirming imagery, geographic metadata, resolution, quality and rights. A pilot in Kazakhstan is preferred, subject to imagery availability and permission to use the data.

**Excluded:** nationwide operational coverage, native Android/iOS applications, integration with government systems, automated legal conclusions, universal detection of all waste categories/sizes, pixel-perfect segmentation, automated pixel-level change detection, fully automatic retraining/model promotion, vehicle route optimization, validated ecological hazard scores, and full offline report synchronization.

## 1.8. Engineering Complexity, Feasibility and Dependencies

The engineering work centers on satellite object detection, geospatial coordinate correctness, provenance-preserving evidence association, a multi-role verification workflow and data-safe model feedback. The architecture uses a modular FastAPI application, PostgreSQL/PostGIS, React/TypeScript PWA, Leaflet, Rasterio and an independent PyTorch workflow. The detailed architecture is presented in Section 7.

The main limitations are restricted access to high-resolution pilot imagery, geographic transfer of a detector trained on other regions, and uncertainty in the public dataset splits. Requests for academic imagery have been sent to Kazakhstan Garysh Sapary and Airbus. Until a suitable pilot scene is obtained, object detection can be assessed on research imagery and the geospatial conversion pipeline on a separately authorized GeoTIFF. Their results will be reported separately.

## Sources for Section 1

[P1] Committee for Environmental Regulation and Control, 2026 satellite monitoring results: https://www.gov.kz/org/cerc/press/news/details/1293504?lang=ru

[P2] Prosecutor's Office of Abai Region, repeated locations: https://www.gov.kz/org/prokuratura-abay/press/news/details/1031151?lang=ru

[P3] Kazakhstan Garysh Sapary, Space monitoring of waste: https://km.gharysh.kz/courses/waste

[P4] Government citizen reporting description: https://www.gov.kz/org/cerc/press/news/details/1246692?lang=ru

[P5] TazaQala official platform: https://tazaqala.com/ru/
