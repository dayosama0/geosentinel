# 6. Requirements Specification

## 6.1. Scope, Users and Priorities

These requirements specify the **Balanced MVP v2.0**. The three user roles are **Citizen** (mobile report and permitted status), **Inspector** (verified case and mission management), and **Administrator / ML Operator** (account management, imagery/data review, model experiments). Inspector and administrator accounts have restricted permissions.

**M = Must Have** within the agreed engineering scope; **S = Should Have** if time and data permit. Image import requires a valid georeferenced file with appropriate usage rights. Human decisions distinguish potential visual waste from legally established unauthorized dumping.

## 6.2. Functional Requirements and Acceptance Criteria

### Satellite image import and detection

| ID | Priority | Requirement | Acceptance criterion |
|---|---|---|---|
| FR-01 | M | Import a supported georeferenced satellite raster, initially GeoTIFF. | Valid CRS/transform saved; malformed or unsupported input rejected without partial record. |
| FR-02 | M | Tile/process satellite image while retaining geographic pixel offsets. | Test bounding boxes map back through the original tile window and spatial transform. |
| FR-03 | M | Predict candidate waste-dump bounding boxes, labels and confidence. | Detector returns a structured, valid set of zero or more detections. |
| FR-04 | M | Display geolocated detections when source spatial information is valid. | Bounding box center/footprint is correctly positioned on map; no invented coordinates when CRS absent. |
| FR-05 | M | Preserve detection provenance and the source model version. | Linked image, model version, processing time and known acquisition date are recoverable. |

### Citizen reports, map and status

| ID | Priority | Requirement | Acceptance criterion |
|---|---|---|---|
| FR-06 | M | Submit citizen report with photo, location and optional details. | Valid report saved with unique ID; missing required information rejected. |
| FR-07 | M | Support browser geolocation and manual map-point correction. | Denied location permission still allows manual point selection. |
| FR-08 | M | Show report submission reference and permitted public status. | Citizen receives reference without access to restricted inspector notes. |
| FR-09 | M | Display monitored sites and observations on interactive map. | Inspector selects a site and opens its related observations. |
| FR-10 | S | Filter map/cases by source, status, dates and location. | Filtering and reset return correct record sets. |

### Evidence fusion and preservation

| ID | Priority | Requirement | Acceptance criterion |
|---|---|---|---|
| FR-11 | M | Distinguish MonitoredLocation from its source observations. | Multiple satellite and citizen observations may link to one site without deletion. |
| FR-12 | M | Suggest geographic candidate matches using distance and available time. | Configured nearby match is proposed; remote pairs are not matched by basic proximity rule. |
| FR-13 | M | Permit inspector to accept/reject/defer proposed match. | Decision recorded; geographic proximity cannot permanently merge records on its own. |
| FR-14 | M | Retain immutable observation provenance and event history. | Source, observation date, coordinates and decisions available to authorized reviewer. |

### Smart Verification Missions

| ID | Priority | Requirement | Acceptance criterion |
|---|---|---|---|
| FR-15 | M | Create mission related to an observation/site. | Unique mission ID, site relation and initial status stored. |
| FR-16 | M | Display explicit rule-based reasons for follow-up. | Queue shows missing confirmation, conflict or post-cleanup observation reason. |
| FR-17 | M | Update mission states and verification outcomes. | Open, In Progress, Completed, Cancelled supported; outcome includes Waste Present, False Positive, Inconclusive. |
| FR-18 | M | Attach comments and evidence to mission. | Attachment linked to mission, user and timestamp. |

### Cleanup and Re-Dumping Alerts

| ID | Priority | Requirement | Acceptance criterion |
|---|---|---|---|
| FR-19 | M | Record authorized confirmed cleanup and its effective date. | Cleanup event stores timestamp, reviewer and supporting reason/evidence. |
| FR-20 | M | Identify post-cleanup observations near the cleared location. | Observations dated after cleanup may trigger alert; old acquisitions imported later do not. |
| FR-21 | M | Link possible recurrence alert to evidence and reinspection. | Inspector can inspect prior clearance/new evidence and record review outcome. |
| FR-22 | M | Avoid duplicate unresolved recurrence alerts on reprocessing. | Repeated same observation generates only one active alert per relevant event. |

### Continuous Model Improvement

| ID | Priority | Requirement | Acceptance criterion |
|---|---|---|---|
| FR-23 | M | Select verified *satellite* observations as training candidates. | Candidate references valid satellite crop and verification record. |
| FR-24 | M | Require annotation and quality/licensing review before approval. | Ground-level citizen photo alone is not eligible as satellite detector training image; invalid annotation rejected. |
| FR-25 | M | Export approved and versioned dataset manifests. | Manifest identifies input imagery, labels, reviewer, dataset version and source split. |
| FR-26 | M | Support explicit offline retraining and evaluation. | Candidate model compared against baseline using protected independent split and saved config; if data inadequate, no improvement claim. |
| FR-27 | M | Version models and require explicit activation. | Candidate cannot replace current model before authorized release decision and saved evaluation results. |

### Security and management

| ID | Priority | Requirement | Acceptance criterion |
|---|---|---|---|
| FR-28 | M | Enforce Citizen, Inspector, Administrator/ML Operator roles. | Restricted APIs reject unauthorized attempts including direct requests. |
| FR-29 | M | Keep audit trail of verification, status and model changes. | Each change identifies actor, timestamp and affected record. |
| FR-30 | M | Manage and disable inspector/admin accounts. | Administrator can change roles and disable accounts without exposing passwords. |

## 6.3. Non-Functional Requirements

The following values are acceptance targets for subsequent implementation tests.

| ID | Priority | Requirement and verifiable target |
|---|---|---|
| NFR-01 | M | Citizen report usable at mobile width 360 px without horizontal scrolling of key controls. |
| NFR-02 | M | Under documented local test conditions (20 simulated concurrent clients, ≥1,000 records), p95 for non-ML API requests < 3 seconds. |
| NFR-03 | M | Long detection/retraining tasks do not block ordinary API responsiveness; failed job does not corrupt case data. |
| NFR-04 | M | Pixel-to-world transform checked against ≥5 known raster reference cases, including window offsets and CRS transform. |
| NFR-05 | M | Referential integrity enforced among site/observation/mission/alert/model records. |
| NFR-06 | M | Authentication on restricted routes; passwords hashed, uploads validated; HTTPS in deployed environment. |
| NFR-07 | M | Private contact data and restricted evidence not exposed via public API. |
| NFR-08 | M | Dataset split, seed, config, training setup, versions and evaluation recorded. |
| NFR-09 | M | Related satellite source scenes not knowingly split across training and protected test data; suspicious cases reviewed. |
| NFR-10 | M | Invalid input, corrupt image or failed processing returns controlled error, no partial committed record. |
| NFR-11 | S | Module boundaries documented, regression tests for matching, mission and alert rules. |
| NFR-12 | S | Labeled fields, visible keyboard focus and status indication beyond color only. |
| NFR-13 | M | Source and applicable use rights logged for every training/pilot imagery dataset; redistribute only when permitted. |

## 6.4. Core Acceptance Scenarios

| Scenario | Given and action | Expected behavior / negative test |
|---|---|---|
| AC-01: Satellite detection | Authorized user processes licensed, georeferenced GeoTIFF | Predictions stored with source and geographic positions; without spatial metadata no fictional map coordinates |
| AC-02: Citizen + fusion | A new georeferenced report near an existing monitored site | Potential match proposed; both original records retained; explicit review before link confirmation |
| AC-03: Verification | Inspector opens a mission for ambiguous detection | Reason, evidence and outcome saved; citizen cannot perform inspector decision |
| AC-04: Recurrence | A cleared site receives a later independently dated observation | Reinspection alert created/reused; upload of older image does not trigger recurrence |
| AC-05: Model update | Reviewed satellite crops with valid annotations and rights | Versioned export, reproducible training and baseline comparison; protected test excluded; no automatic promotion |
| AC-06: Site history | Site has observations, cleanup event and reinspection alerts | Ordered events with provenance shown; later state never erases history |

## 6.5. Data and Lifecycle Rules

Data entities include **SatelliteImage** (CRS, transform, acquisition date, source/license), **Detection** (box, confidence, model), **CitizenReport**, **MonitoredLocation**, **EvidenceMatch**, **VerificationMission**, **CleanupEvent**, **ReDumpingAlert**, **DatasetCandidate**, **DatasetVersion**, **ModelVersion**, **AuditEvent** and authorized **User**. Images and report photos are kept in restricted file storage, while PostGIS holds metadata and geometry. The report submission timestamp is distinct from the claimed observation date; the satellite processing timestamp is distinct from the actual image acquisition date. Missing dates are marked unknown and cannot establish recurrence by inference.

Citizen reports may be submitted without creating a registered account, with secure submission references. Only role-authorized inspectors can affirm waste presence, record cleanup, resolve recurrence alerts or accept evidence associations. The outcome *Waste present* records an inspection observation; legal classification falls outside the system's scope.

## 6.6. Dependencies, Prioritization and Exclusions

Implementation order: (1) dataset readiness, licensed imagery support and data model; (2) detection and map; (3) citizen interface; (4) matching plus inspector review; (5) missions and cleanup events; (6) date-aware alerts; (7) reviewed satellite candidates and versioned offline training; (8) evaluation and security. Training data are independent of active citizen photo submissions unless a corresponding legitimately licensed satellite crop is explicitly acquired and annotated.

Outside mandatory MVP: native mobile apps, full-country coverage, government integrations, online retraining on every report, legal classification, mandatory pixel segmentation, automatic satellite image change detection, advanced risk scoring, vehicle route optimization and full offline report sync. Basic multi-date image viewing may be explored **only** if suitable licensed co-registered imagery is available.

## 6.7. Requirements-to-Evidence Map

| Group | Requirements | Planned verification evidence |
|---|---|---|
| Detection / GIS | FR-01–05; NFR-04 | GeoTIFF tests, bounding boxes, transformed map coordinates |
| Citizen / map | FR-06–10; NFR-01 | API tests, mobile screenshots and end-to-end submissions |
| Fusion | FR-11–14 | Gold-labeled match/non-match pairs, reviewer actions, provenance |
| Missions | FR-15–18 | State transition tests, role restrictions and attachments |
| Monitoring | FR-19–22 | Time-order/duplicate regression cases |
| Model improvement | FR-23–27; NFR-08–09 | Dataset manifest, training configuration, independent evaluation, release gate |
| Security/admin | FR-28–30; NFR-05–07, 10 | Authorization, integrity, error handling and audit tests |

Detailed metrics, baselines and test conditions are specified in **Section 9**.
