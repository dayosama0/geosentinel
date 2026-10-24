# Satellite Landfill Monitoring

**Diploma project:** Development of a system for detecting and monitoring the locations of unauthorized landfills based on the analysis of satellite images and crowdsourcing.

**Author:** Ali Turaliyev · Software Engineering, SE-2430 · Astana IT University  
**Scientific supervisor:** Aldiyar Salkenov  
**Stage:** First pre-defense · 24 October 2026

## Project overview

The system is designed to help environmental inspectors locate and follow up on suspected waste dumping sites. It combines satellite image detections with geolocated citizen reports and preserves the evidence collected about each site over time.

The planned workflow is:

1. Detect candidate dumping sites in high-resolution satellite images.
2. Place detections on a map using the source image's georeferencing.
3. Match nearby citizen reports with existing locations without discarding the original observations.
4. Create verification missions and record inspection findings.
5. Flag new evidence at sites previously marked as cleared.
6. Collect reviewed satellite image crops for controlled retraining and model comparison.

## Scope

The proposed MVP consists of a satellite object detector, FastAPI backend, PostgreSQL/PostGIS database, React/TypeScript web application, and Leaflet map. Three supporting workflows are included:

- **Smart Verification Missions:** inspection tasks, review outcomes and supporting evidence.
- **Re-Dumping Alerts:** follow-up alerts when a later observation is associated with a cleared site.
- **Continuous Model Improvement:** reviewed satellite annotations, dataset versioning, offline training and explicit model release decisions.

Nationwide operation, government system integration, native mobile apps, automatic legal judgments and online self-training are outside the planned scope.

## Technical limitations

- **Image availability:** suitable high-resolution, georeferenced satellite scenes for a pilot area depend on licensing and provider access.
- **Model transfer:** data from one satellite, resolution or region may not generalize to another. The current SWAD labels identify a single `waste dump` class.
- **Evaluation integrity:** the SWAD v2 audit identified overlap between training and test scenes. These partitions require correction before an independent detection benchmark can be reported.
- **Geolocation:** the audited SWAD JPEG images contain no embedded geographic reference. Mapping actual detections requires a separate georeferenced raster or verified external metadata.
- **Evidence quality:** citizen reports may have inaccurate coordinates or observation dates. Spatial matches and post-cleanup alerts require review.

## Current deliverables

The current repository contains the analysis, architecture, dataset audit, UX prototype, evaluation plan and development backlog. Backend integration, detector training and geospatial inference are planned for subsequent development milestones.

## Repository structure

| Path | Contents |
|---|---|
| `docs/` | The eleven report sections in Markdown |
| `diagrams/` | System Context, Use Case and Component diagrams; SVG/PNG exports and source generator |
| `prototype/` | Clickable browser prototype and screenshots |
| `data_audit/` | SWAD audit output and manifest; raw imagery excluded |
| `planning/` | YouTrack task plan, milestones and risk register |
| `tests/` | Prototype smoke tests and test notes |

## Open the prototype

Open [`prototype/prototype.html`](prototype/prototype.html) in Edge or Chrome. The screens cover citizen reporting, monitoring overview, verification missions, re-dumping alerts, location history and model improvement. Interaction is local to the browser.

## Rebuild diagrams

```bash
python diagrams/generate_diagrams.py
```

## Testing

A Playwright smoke test is provided in `tests/test_prototype_smoke.py`. It checks navigation and selected interactions in the HTML prototype; model accuracy and production API tests are scheduled for subsequent development. Dataset audit methodology and output are documented in `data_audit/`.

## Project tracking

The project backlog is in [`planning/YouTrack_Backlog.csv`](planning/YouTrack_Backlog.csv). The YouTrack board URL and actual issue IDs will be added when the project is configured. Planning IDs in the CSV are temporary. The checked first pre-defense revision will be tagged `pre-defense-1`.

## Data use

Source imagery, citizen photos and model training data must be used under their applicable licenses and privacy rules. Do not commit credentials, non-public satellite archives or personal reports. See `data_audit/README.md` for the preliminary dataset checks.
