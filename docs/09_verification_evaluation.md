# 9. Verification & Evaluation Plan

## 9.1. Evaluation Objective and Approach

The purpose of verification is to demonstrate that the proposed prototype can detect candidate waste dumping sites, maintain correctly referenced geographic observations, support citizen reporting and inspector verification, and manage controlled model updates and re-dumping alerts. The plan corresponds to the approved Balanced MVP v2.0 and the requirements in Section 6 (FR-01–FR-30 and NFR-01–NFR-13).

Evaluation will combine automated tests, controlled machine-learning experiments, geospatial consistency checks, and end-to-end workflow tests. Results will be collected during implementation using the conditions defined in this section.

The following distinctions will be preserved throughout reporting:
- A model prediction is a *candidate detection*, not legal proof of unauthorized dumping.
- An internal benchmark result is not evidence of generalization to a new satellite sensor or geographic region.
- Interface demonstrations and scripted test cases are not substitutes for real-world evaluation by environmental inspectors.
- Results from the UX prototype will be identified separately from results produced by an implemented backend.

## 9.2. Dataset Readiness and Independent Evaluation

The preliminary audit of the publicly distributed SWAD v2 (YOLOv8 format) examined all 1,996 JPEG images and corresponding labels, containing 5,562 valid bounding boxes for one class (`waste dump`). No corrupt images, invalid boxes, or exact cross-split duplicates were detected. However, the audit reported 102 perceptually similar cross-split candidate pairs, and two visually reviewed pairs were confirmed to depict overlapping satellite scenes between the train and test partitions. The complete manual review of the remaining candidates and source licensing has not been performed.

**Decision:** The supplied SWAD v2 split is unsuitable for an independent final performance claim in its current state.

Before model comparison, the following controls will be applied:

1. Review candidate duplicate pairs and inspect selected images with overlaid bounding boxes.
2. Group images originating from the same or overlapping source scene where provenance can be established; keep related tiles and their augmentations in a single partition.
3. Create and document revised train, validation, and test partitions by source-scene group, not by random image alone. Use augmentation only on training images.
4. Where independent scene provenance cannot be established with reasonable confidence, seek an additional separately annotated evaluation set and explicitly qualify benchmark limitations.
5. Keep the independent test set frozen. Select models, confidence thresholds, and hyperparameters using training and validation data only.
6. Include non-waste scenes and visually confusing backgrounds where rights and annotations permit; otherwise disclose the lack of negative coverage.
7. Preserve dataset manifests, version identifiers, class mapping, hashes and annotation-review notes. Record applicable usage and redistribution rights separately; the export's claimed license is not independent legal verification.

SWAD JPEG files lack embedded geospatial reference information in the audited export. Therefore, geographically valid pilot demonstrations require independently georeferenced imagery, such as authorized GeoTIFF files, with acquisition metadata. If such imagery is unavailable, map-based results must remain prototype demonstrations and must not be represented as operational geolocated detections.

## 9.3. Object Detection Experiment

**Baseline and candidate.** A Torchvision Faster R-CNN configuration will serve as an architectural baseline; a small YOLO detector will be the main candidate. Exact model variants, pretrained weights, training schedule, hardware, and software versions will be recorded before each run. The planned model selection remains provisional and is subject to available compute and licensing conditions.

**Controlled comparison.** Both models will use the same approved data partitions, class definition, evaluation code or harmonized metric implementation, and test images. Image transformations appropriate to each architecture will be documented. If feasible, repeat training under multiple fixed random seeds and report variation rather than choosing the best run.

| Metric | Purpose | Measurement |
|---|---|---|
| Precision and Recall | False-positive and missed-waste trade-off | Object-level matching at IoU >= 0.50, at a confidence threshold selected on validation data |
| F1-score | Balance of precision and recall | Derived from precision and recall at the frozen operating threshold |
| mAP@0.50 | Detection/localization performance at IoU 0.50 | Standard AP computation on the independent test set |
| mAP@0.50:0.95 | Stricter localization assessment | Mean AP over IoU 0.50, 0.55, ..., 0.95 |
| False positives on negative scenes | Practical false-alarm behavior | False detections per negative image, where independently checked negative scenes are available |
| Inference time | Deployment feasibility | Median and p95 per image or tile, with batch size, device, warm-up, and I/O boundaries specified |

For the single-class SWAD task, mean Average Precision is calculated over the single waste-dump category; it must not be described as evidence of correct identification of distinct waste-material types. Results will include precision–recall curves, representative true/false detections, and an explicit error analysis (bare land, buildings, roads, shadows, and other confusing backgrounds, where present).

**Generalization check.** If appropriately licensed and independently annotated satellite images from a different region or sensor become available, they will be evaluated separately as an external test. Their ground sampling distance, sensor, image acquisition date, and annotation protocol will be recorded. Model performance on the external set will not be inferred from SWAD accuracy.

**Acceptance evidence.** The experiment must produce valid, reproducible predictions, a comparison table against the baseline, and a documented analysis of false positives and false negatives. A numeric target will be chosen after the dataset and pilot imagery are finalized. Deployment suitability will also depend on geographic transfer, false detections and verification workload.

## 9.4. Geospatial Processing and Evidence Fusion

### Georeferencing tests

Using at least five independently calculated control cases, pixel positions (including points near tile edges) will be transformed to raster CRS coordinates and, where required, to latitude/longitude. Expected and actual coordinates will be compared in consistent units. Tests will also cover a missing CRS, invalid transform, raster tile offset, and CRS mismatch. The conversion must not assign geographic coordinates to imagery without a reliable spatial reference.

### Evidence matching tests

A small labeled set of positive, negative, and ambiguous observation pairs will be prepared. As a planning target, at least 100 pairs will be used, including geographically close but unrelated observations and records with missing or conflicting dates. Synthetic pairs will be reported as scenario-level tests; real observations are required for field matching accuracy.

**Baseline:** proximity-only matching using a fixed geographic radius.

**Proposed approach:** configurable spatial matching complemented by temporal/source checks and an inspector confirmation or rejection step.

Metrics will include pair-level precision, recall, F1, false merges, missed matches, and unresolved decisions. Automated candidate generation and the final human-reviewed association will be evaluated separately. Every association decision must retain the underlying observations and their provenance. The matching radius will be set using development cases and frozen before independent testing.

## 9.5. Smart Verification Missions

Mission tests will cover the following sequence: create mission for an observation; assign/open; change status to In Progress; record outcome and evidence; close or cancel; verify audit history; and reject an unauthorized action. The minimum supported outcomes are Waste Present, False Positive, and Inconclusive. No decision may silently overwrite the original satellite detection or citizen report.

The planned rule-based attention queue will be compared with a **first-in, first-out (FIFO)** queue on the same controlled cases. Cases must have independently specified review priorities, rather than using the proposed rule itself as ground truth. Report top-k retrieval of cases requiring attention, duplicate/incorrect task creation, and the proportion of required workflow actions completed correctly. Productivity effects would require separate testing with inspectors.

## 9.6. Re-Dumping Alerts

The alert logic must use an observation's **actual observation/acquisition date**, not only its upload or processing timestamp. A qualifying new observation near a previously cleared location creates a *possible recurrence* alert requiring human review. Geographic proximity and date order alone do not confirm renewed illegal dumping.

The controlled test suite will include at least the following cases:

| Case | Expected behavior |
|---|---|
| Newly observed evidence after confirmed cleanup at the same site | Create or maintain one pending reinspection alert |
| Old image acquired before cleanup but uploaded afterward | No automatic re-dumping alert |
| New evidence near an unrelated adjacent site | Require match review; avoid unconditional site merge |
| Unknown or unreliable acquisition date | Mark for review; do not automatically classify as recurrence |
| Reprocessing the same new observation | No duplicate active alert |
| Cleanup not yet confirmed | Handle as an ordinary monitoring/verification event, not confirmed post-cleanup recurrence |
| Alert resolved and a later distinct qualifying observation appears | Evaluate a new recurrence event without deleting historical alerts |

Record the number of expected alerts correctly created, false alerts, missed expected alerts, duplicate alerts, and correct inspector status transitions. For labeled scenarios report alert precision and recall when denominators are meaningful. The simple baseline is proximity combined with upload-date ordering; the proposed date-aware logic is expected to avoid the baseline's known late-upload error. This expectation must be verified, not asserted as a completed result.

## 9.7. Continuous Model Improvement

The model-improvement process will be assessed primarily as a controlled data and versioning workflow:

1. A reviewed satellite observation is proposed as a new annotated training candidate.
2. The candidate is accepted only after checking the source image, bounding-box annotation, provenance, usage rights, and lack of prohibited overlap with the frozen test scenes.
3. Approved examples are exported with a dataset version and manifest. Citizen photographs alone are not exported as training imagery for the satellite detector.
4. A model candidate is trained offline and evaluated with the same held-out test set and metric settings as the baseline.
5. The active model is changed only after an explicit authorized decision supported by recorded evaluation results.

**Baseline:** the initially evaluated detector before incorporating newly reviewed examples.

**Candidate:** the model after a documented training update using an approved dataset version.

Compare changes in precision, recall, mAP, and false positives, and document regressions as well as improvements. An improvement in accuracy will be reported only after valid satellite training examples and a genuine, leakage-free retraining experiment are available. Where new data are unavailable, verify only the candidate review, versioning, export, and promotion safeguards.

## 9.8. Functional, Security, UX and Performance Testing

Requirements will be traced to test cases and evidence records. The table specifies core coverage; the complete test suite will be expanded during implementation.

| Test group | Requirement coverage | Test method and pass condition |
|---|---|---|
| Imagery processing and map | FR-01–FR-05; NFR-04 | Valid GeoTIFF import, detection records, geographic transform checks, and rejection of invalid/missing CRS |
| Citizen submission and public status | FR-06–FR-10; NFR-01 | Submit photo, date and selected location; reject invalid inputs; allow status lookup without restricted record exposure; verify 360 px layout |
| Observation matching and history | FR-11–FR-14; NFR-05 | Verify independent original records, matching review decisions, and chronological provenance |
| Verification workflow | FR-15–FR-18 | Mission creation, status transitions, evidence, and required outcomes |
| Cleanup and recurrence | FR-19–FR-22 | Cleanup history, valid post-cleanup alerts, old-image and duplicate-event controls |
| Dataset and model control | FR-23–FR-27; NFR-08–NFR-09, NFR-13 | Review gate, export manifest, independent test protection, logged training runs, and explicit model approval |
| Access and audit trail | FR-28–FR-30; NFR-06–NFR-07 | Authorized vs unauthorized API calls, role changes, upload validation, protected data, and actor/time/action history |
| Reliability and maintainability | NFR-03, NFR-10–NFR-12 | Failure recovery, isolated ML processing, core automated tests, keyboard and readable-status review |

**Performance measurement:** For ordinary non-ML API requests, the previously specified target is p95 response time below 3 seconds under 20 simulated concurrent clients against at least 1,000 monitoring records. Tests will record the machine specifications, OS, database version, deployment configuration, client load pattern, duration, sample size, and measured p50/p95 latency and error rate. Heavy satellite processing and offline retraining will be measured separately and must not be disguised as ordinary API requests.

**Usability:** At least the citizen report, inspector mission completion, and re-dumping review flows will be checked with scripted tasks. Screen compatibility will be inspected at mobile width 360 px and common desktop widths. If independent users take part, their number, recruitment and task completion observations will be reported; otherwise the results will be labeled developer-performed walkthroughs, not usability validation by actual government inspectors.

**Security and privacy:** Verify role-based access for each restricted operation, basic input and file-upload validation, password hashing, protection of sensitive records, and audit logs. Production HTTPS is a deployment acceptance requirement, not an assertion about the offline HTML prototype.

## 9.9. Evaluation Records and Reporting

For each executed test or experiment, preserve:
- Test case/requirement ID, date, software revision, environment and data version.
- Inputs, expected behavior, observed result, pass/fail decision, and defect reference if applicable.
- For ML, seed, hardware, library versions, model checkpoint, evaluation settings, confusion/error examples, and output metrics.
- For GIS, CRS and spatial transform used in the test.
- For user flows, screenshots or short recordings, with sample information clearly identified.

A traceability table will connect Section 6 acceptance criteria to test cases and repository artifacts. Failed cases will remain visible in the test log and be linked to corrective tasks.

The current confirmed work consists of a preliminary automated SWAD file/annotation audit and UX prototype browser interaction checks. **No object detection training, operational geospatial integration, user study, or quantitative model improvement has yet been demonstrated in this plan.** Future results will be added only after execution.

## 9.10. Conclusion

The evaluation plan tests both the correctness of the individual components and the integrated monitoring workflow. Independent satellite detection evaluation, provenance-preserving evidence matching, verification missions, data-controlled model updates, and date-aware re-dumping alerts form the principal technical evidence for the diploma project. The proposed baselines and measurement conditions make the planned results reproducible while preventing unsupported claims about generalization, environmental enforcement, or operational superiority to existing government systems.
