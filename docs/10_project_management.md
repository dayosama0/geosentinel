# 10. Project Management & Risks

## 10.1. Project Management Approach and Responsibilities

The project, **“Development of a system for detecting and monitoring the locations of unauthorized landfills based on the analysis of satellite images and crowdsourcing,”** is an **individual diploma project** undertaken by **Ali Turaliyev**, Astana IT University, group SE-2430. **Aldiyar Salkenov** is the scientific supervisor. The student is responsible for requirements analysis, design, implementation, dataset preparation, model experiments, verification, documentation, version control, and presentation. The supervisor provides academic review and feedback at agreed checkpoints. All delivery tasks are assigned to the student.

A milestone-driven process with short implementation and review cycles will be used. Each iteration will produce a verifiable output (document, diagram, test, software feature, or experiment), with task acceptance criteria and evidence recorded in the repository. Planned dates beyond the first pre-defense are provisional and subject to supervisor and university confirmation.

## 10.2. Project Tracking and Source Control

**Source control:** Git and GitHub (or GitLab if the chosen repository is hosted there). A single continuous repository will hold documentation, versioned diagrams, prototype assets, source code, experiment scripts, and tests. The repository URL will be added to the README after publication.

**Task tracking:** YouTrack. The proposed project name is `Satellite Landfill Monitoring` and its issue key will be assigned by YouTrack during project creation. The planning identifiers `PL-01`, etc., used in the annexed backlog are temporary local identifiers, not actual YouTrack issue numbers.

Each task will contain a concise outcome, owner (Ali Turaliyev), priority, deadline, acceptance criteria, relevant requirements, dependencies, and a link to the supporting Git commit/pull request or other artifact. Proposed board states: `Backlog`, `In Progress`, `In Review`, `Blocked`, and `Done`. The student will move a task to `Done` only after its acceptance criteria and evidence have been checked. Major academic review items can remain in `In Review` until actual supervisor feedback is obtained.

**Individual contribution model:** All student development and documentation commits are authored under the student's own Git identity. Selected significant deliverables are offered to the supervisor for review; review decisions will be documented when received. Branch names and commit/PR descriptions will include the real YouTrack issue ID once available. Example after actual task creation: `DIP-23-geospatial-schema` and `DIP-23: add monitored-location schema` (illustrative only; actual prefix and key depend on the project).

The `main` branch represents the submitted/reviewed baseline. Feature tasks are developed on separate branches and integrated through documented pull requests. Each meaningful commit corresponds to a real change. The initial import will record the existing design materials on the actual commit date. Later work will be tracked through separate changes. The required first pre-defense submission will be identified by the Git tag **`pre-defense-1`**, created only after the final repository revision is checked and uploaded. Future official submission tags will be `pre-defense-2` and `final-pre-defense` where required.

## 10.3. Repository Organization and Reproducibility

The repository is organized as follows:

```text
satellite-landfill-monitoring/
├── README.md
├── docs/                  # eleven report sections (Markdown)
├── diagrams/              # source generator and SVG/PNG exports
├── prototype/             # interactive HTML and screen images
├── data_audit/            # SWAD audit and manifest
├── planning/              # task backlog, milestones, risk register
└── tests/                 # browser smoke tests
```

The README will specify the approved project title, problem, intended users, scope, current status, author/supervisor, proposed technologies, documentation entry points, YouTrack link, and later runnable setup/test commands. It will clearly distinguish a UX prototype from an implemented backend and distinguish the preliminary SWAD dataset audit from actual model-training results. Satellite imagery, private user reports, credentials, API keys, and restricted datasets will not be committed without appropriate permissions.

## 10.4. Milestones and Provisional Timeline

| Milestone | Target date | Deliverable and completion condition | Principal dependency |
|---|---|---|---|
| M0 — First pre-defense | **24 Oct 2026, 18:00** | One report PDF containing the 11 mandatory sections, separate YouTrack screenshots PDF, accessible GitHub/YouTrack links, diagrams/prototype, and `pre-defense-1` tag | Document integration, repository and issue board setup |
| M1 — Data readiness | 15 Nov 2026 | Completed SWAD scene/annotation review, documented split strategy, licensing decision, and data manifest | Dataset audit, source rights |
| M2 — Detection baselines | 15 Dec 2026 | Reproducible baseline and candidate experiments with validation and error review; independent metrics only if test integrity is established | M1, computing access |
| M3 — Geospatial backend | 20 Jan 2027 | PostGIS schema, API, authenticated roles, georeferenced raster handling, coordinate checks | Technology choices, eligible GeoTIFFs |
| M4 — Core interfaces | 20 Feb 2027 | Citizen reporting, site map, status tracking and inspector dashboard integrated with API | M3 |
| M5 — Evidence and missions | 15 Mar 2027 | Provenance-preserving matching, human association review and verification mission lifecycle | M3–M4 |
| M6 — Recurrence monitoring | 31 Mar 2027 | Cleanup history, date-aware re-dumping alerts and regression tests | M5 |
| M7 — Controlled ML updates | 20 Apr 2027 | Reviewed satellite training candidates, versioned export, gated model selection; retraining demonstration if valid new data are available | M1–M2, M5 |
| M8 — Integration and evaluation | 10 May 2027 | End-to-end tests, baseline comparisons, security/performance checks, limitations | M3–M7 |
| M9 — Final preparation | May–Jun 2027, **to be confirmed** | Final report, supervisor review, presentation and demonstration | M8, official university schedule |

The dates after M0 are **planning targets**, not published university deadlines or commitments by external data providers. The scope and dates will be adjusted if a dependency is unavailable, especially licensed georeferenced imagery and independent test data.

## 10.5. Work Breakdown, Dependencies and Priorities

The project backlog is organized into workstreams rather than team-member assignments:

1. **Governance and documentation:** repository, task board, review package, supervisor consultations and traceability.
2. **Satellite data and evaluation:** dataset provenance, license checks, leakage correction, independent partitions, model baselines and cross-region testing when possible.
3. **GIS and backend:** georeferenced imagery ingestion, pixel-to-world coordinate transforms, location/observation schema, FastAPI, PostGIS, access controls.
4. **Citizen and inspector experience:** mobile-first reporting, geographic map, public status, evidence matching and verification missions.
5. **Monitoring and model feedback:** cleanup events, temporal re-dumping rules, approved-sample export, offline training, versioning and model promotion gates.
6. **Quality and delivery:** unit, integration, UI, security, performance and reproducibility tests; thesis writing and presentation.

Dependencies follow the approved Requirements Specification and architecture. **Model evaluation** depends on data integrity; **GIS detection mapping** depends on licensed georeferenced imagery; **evidence matching** depends on a persistent observation/location model; **verification missions** depend on user roles and observations; **re-dumping alerts** depend on cleanup dates and verified observation times; **model improvement** depends on reviewed satellite labels and an independent evaluation set. A machine-learning model must not be promoted without a completed evaluation and explicit approval.

The accompanying `YouTrack_Backlog.csv` records detailed tasks, suggested deadlines, acceptance criteria, requirement links and predecessors. Actual issue keys and status changes will be assigned in YouTrack.

## 10.6. Risk Management

Risks are scored on a simple qualitative **Likelihood × Impact** basis (Low / Medium / High). The risk owner is the student unless an external party is identified as a dependency; no external party is assigned a project task without agreement.

| ID | Risk | Likelihood / Impact | Mitigation and contingency |
|---|---|---|---|
| R-01 | No academic access to high-resolution georeferenced Kazakhstan imagery | High / High | Track the submitted KazEOSat and Airbus inquiries; audit alternatives with explicit licenses. If access is unavailable, demonstrate the ML component on research data and geospatial processing on another authorized pilot or sample; do not claim Kazakh operational deployment. |
| R-02 | SWAD scene-level leakage or annotation errors inflate performance | High / High | Complete manual candidate review; group source scenes; freeze independent test data; qualify or defer generalization claims when provenance is insufficient. |
| R-03 | Restrictions on imagery/model data licensing | High / High | Record permitted research, ML training and redistribution uses for each source; use compliant data and avoid committing licensed raw imagery. |
| R-04 | Domain shift between research imagery and pilot satellite sensor | High / High | Record GSD/sensor characteristics; assess external validation separately; constrain claims and selected pilot scale. |
| R-05 | Scope overrun in a one-person project | High / High | Stage-gate mandatory modules; restrict model improvement to reviewed export and controlled offline training, not automatic online learning; defer advanced features. |
| R-06 | Incorrect CRS or tile offsets cause false map locations | Medium / High | Rasterio/GDAL control-point tests, CRS metadata checks, fail-closed handling when reference data are missing. |
| R-07 | False evidence merges or duplicate reinspection cases | Medium / High | Candidate associations plus human confirmation; preserve original observations; idempotency tests and distance/temporal edge cases. |
| R-08 | Old satellite acquisitions trigger false re-dumping alerts | Medium / High | Use acquisition/observation dates, not upload dates; review unknown dates and prohibit silent recurrence conclusions. |
| R-09 | Training feedback contaminates protected test scenes | Medium / High | Dataset manifests, source-scene grouping, immutable test set, explicit reviewer approval and model promotion. |
| R-10 | Limited GPU, storage or processing time | Medium / Medium | Begin with small models and limited tiles; document compute, use efficient offline runs, adjust experiments to available resources. |
| R-11 | Missing Git/YouTrack evidence before first pre-defense | High / High | Prioritize real repository, issue board, accessible URLs, artifact upload, screenshots and tag before 24 Oct; keep truthful status of work. |
| R-12 | Supervisor feedback is unavailable before submission | Medium / High | Request review with concrete deliverables and preserve communication evidence; mark feedback pending rather than inventing approval or revisions. |
| R-13 | Exposed credentials, personal information, or unlicensed imagery | Medium / High | `.gitignore`, safe samples, restricted access, review the diff before each commit and remove confidential material from public artifacts. |

Full trigger, owner, status and fallback fields are provided in `Risk_Register.csv`. High risks will be revisited at each milestone and after external data provider responses or substantial design changes.

## 10.7. Traceability and Progress Evidence

Each planned change follows the sequence:

**Requirement or risk → YouTrack issue → branch/commit/PR → artifact or test → acceptance decision → milestone.**

Examples of planned traceability:

| Requirements | Planned task (local ID, not a real YouTrack key) | Evidence | Milestone |
|---|---|---|---|
| FR-01–FR-05; NFR-04 | PL-16, PL-17 | GeoTIFF import code, coordinate test cases | M3 |
| FR-11–FR-14 | PL-20 | Match rules, location records, matching tests | M5 |
| FR-15–FR-18 | PL-21 | Mission UI, API results, transition tests | M5 |
| FR-19–FR-22 | PL-22 | Date-aware alerts and regression tests | M6 |
| FR-23–FR-27; NFR-08–NFR-09 | PL-23, PL-24 | Reviewed sample manifest, training record, metrics | M7 |
| FR-28–FR-30; NFR-06–NFR-07 | PL-18, PL-25 | RBAC/API and audit log tests | M3–M8 |

At the first pre-defense the already prepared analytical materials (proposal and supporting drafts, SWAD audit, diagrams, UX prototype and verification plan) may be cited as **drafted artifacts**, but not as operationally implemented functions. Repository commits and YouTrack completion statuses must reflect their real submission and review state.

## 10.8. Immediate Pre-Defense Submission Controls

The official first pre-defense requirements include: **one main report PDF with all eleven sections**, an **independent PDF containing YouTrack board/task screenshots**, an accessible project repository, and a tagged submitted revision. The submission records the current status of supervisor review and completed technical work. Repository and YouTrack links, screenshots and the submission tag must be checked before upload.

Immediate actions, in order:

1. Set up or identify the actual GitHub repository and provide supervisor/committee access as required.
2. Create the YouTrack project and the core prioritized tasks; assign them to the student's real YouTrack account.
3. Consolidate sections 1–11, including pending truthful supervisor-feedback status, and correct inconsistencies across the Balanced MVP v2.0 drafts.
4. Upload editable architecture diagram sources/exports, the updated UX prototype and evaluation files.
5. Commit meaningful document/design changes, link the resulting real commit IDs to YouTrack tasks, and create `pre-defense-1` only after checking the submitted revision.
6. Export the main report PDF and the separate YouTrack screenshots PDF, verify both files and all URLs, then submit via the official form by 24 October 2026 at 18:00.

**A complete implemented application is not required for the first pre-defense.** The deliverables should demonstrate a credible, traceable progression of research, design, validation planning and supervised development.

## 10.9. Conclusion

The planned workflow provides a clear record of individual development and review. GitHub will retain the engineering artifacts and progress history, while YouTrack will connect tasks with requirements, responsibilities, deadlines, dependencies and concrete evidence. The milestone plan explicitly isolates data-readiness risks, ML evaluation integrity and feature dependencies. The first pre-defense package will provide a checked planning baseline for the subsequent implementation and formal evaluation stages.
