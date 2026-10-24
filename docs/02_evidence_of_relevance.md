# 2. Evidence of Relevance

## 2.1. Evidence Collection Method

This stage draws on official environmental monitoring reports from Kazakhstan, published documentation of existing services, relevant scientific work and a direct audit of the SWAD dataset. The purpose is to identify recurring operational problems and translate them into system requirements. Interviews with environmental inspectors have not yet been conducted; the current findings are based on documents and data.

## 2.2. Publicly Verifiable Evidence

| Evidence | Documented finding | Requirement or design consequence | Limitation |
|---|---|---|---|
| National satellite monitoring [E1] | 2,637 suspected unauthorized dumping locations detected by September 2026, 2,213 reported eliminated | Geospatial monitoring and statuses are operationally relevant | Figures are administrative summaries, not ML ground-truth evaluation |
| Abai Region prosecutor report [E2] | 80 newly detected locations matched coordinates of previously recorded sites | Preserve cleanup history, post-cleanup observations and reinspection alerts | Coordinate recurrence does not establish whether cleaning failed or dumping reoccurred |
| Kazakhstan Garysh Sapary [E3] | Satellite-derived locations, institutional GIS, review and mobile field tools already exist | Retain observation provenance and inspection records | Internal model metrics and fusion internals are not public |
| TazaQazBot [E4] | Citizen reports with photos and geographic locations are routed to authorities, with cleanup evidence | Mobile reporting and status tracking are established workflows | No documented access to backend processing or actual users |
| TazaQala [E5] | Public map, mobile reporting, AI photo moderation and cleanup status | Reuse proven UX patterns, focus on cross-source evidence association | Its internal data integrations are not established by website content |
| SWAD v2 dataset audit [E6] | 1,996 readable JPEGs; 5,562 structurally valid boxes; 102 cross-split perceptual-match candidates; two overlapping train/test scenes visually confirmed | Rebuild independent evaluation split and verify imagery provenance | Manual review of all candidates and rights audit are not finished |

Taken together, the sources support two design priorities: independent evaluation of the detector and a site history that connects observations, inspection decisions and cleanup events.

## 2.3. Project-Specific Dataset Readiness Evidence

An automated scan completed on 21 October 2026 examined the downloaded SWAD v2 YOLOv8 export. It found 1,397 training, 399 validation and 200 test images; all 1,996 images were readable at 640 x 640 pixels, and the 5,562 boxes passed structural validation. It did not detect exact duplicate image files between splits. However, 102 perceptually similar cross-split pairs were flagged, and two inspected pairs showed overlapping scenes. The existing partitions are unsuitable for independent performance evaluation until scene overlap has been resolved. The export also lacks georeferencing within the inspected JPEG files, so a separate GIS pilot source is needed. Geographic coordinates would need to be supplied by a separate verified source.

The audit establishes file integrity and identifies evaluation risks. Model accuracy, data reuse rights and performance on Kazakhstan imagery still require separate checks. Source: `data_audit/audit_report.json` and the associated image manifest (not all raw imagery is included in the repository).

## 2.4. Stakeholder and Acquisition Status

Academic access requests have been sent to Kazakhstan Garysh Sapary for KazEOSat archive images and to Airbus for high-resolution satellite imagery. The pilot area will be selected once image availability, georeferencing and usage rights are known.

The proposed inspector workflow is based on published institutional procedures. Its usability and priorities should be checked with prospective users during a later review stage.

## 2.5. Requirements Supported by Evidence

The main requirements arising from this analysis are: (a) satellite detections remain *candidates*, subject to human review; (b) observations have distinct source/time/geometry; (c) links between reports and sites must be reversible or explicitly reviewable; (d) cleanup history cannot be replaced by a single current status; (e) reinspection alerts must use the **observation or acquisition date**, not merely the upload date; (f) citizen and satellite photos cannot be treated as interchangeable model training examples; (g) imagery and dataset licenses and geographic resolution must be checked; and (h) evaluation requires scene-independent testing.

## 2.6. Conclusion and Open Validation

The sources justify an integrated detection-and-verification workflow. The main gaps in the available evidence concern the applicability of detection models to Kazakhstan imagery, access to licensed pilot scenes and validation of the proposed inspector workflow with users.

## Sources for Section 2

[E1] https://www.gov.kz/org/cerc/press/news/details/1293504?lang=ru

[E2] https://www.gov.kz/org/prokuratura-abay/press/news/details/1031151?lang=ru

[E3] https://km.gharysh.kz/courses/waste

[E4] https://www.gov.kz/org/cerc/press/news/details/1246692?lang=ru

[E5] https://www.tazaqala.com/ru/guide

[E6] `data_audit/audit_report.json` (student-run dataset audit output, 21 October 2026).
