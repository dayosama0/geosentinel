# 5. Technology Comparison

## 5.1. Selection Principles

The architecture must support computer vision experiments, reliable geospatial coordinates, a mobile reporting interface, controlled inspector decisions, historical observations, and explicit model-version approval. The comparison establishes the implementation stack for the prototype. Selection criteria include learning and implementation time for one student, interoperability, existing documentation, licensing constraints, and reproducibility.

## 5.2. Object Detection: YOLO, Faster R-CNN, RT-DETR

| Criterion | Ultralytics YOLO (candidate) | Faster R-CNN / Torchvision | RT-DETR |
|---|---|---|---|
| Detection family | One-stage | Two-stage | Transformer-based |
| Pretrained PyTorch tools | Strong | Native Torchvision | Available PyTorch implementations |
| Initial MVP integration | Relatively simple | Moderate | Moderate |
| Bounding-box labels | Supported | Supported | Supported |
| Practical concern | AGPL/commercial licensing; model/version choice | Speed/resource demands | Training complexity / compute |
| Role | Initial candidate | Planned baseline | Additional option if resources allow |

**Decision:** prepare a small YOLO-family prototype and compare with Faster R-CNN using the same independent image partitions and metrics. Selection will depend on validation results and runtime requirements. The use of Ultralytics code is subject to reviewing AGPL-3.0 or commercial terms [T1]. RT-DETR is retained as a meaningful alternative, not a mandatory third training experiment [T3]. The model comparison will be conducted after the dataset split review.

## 5.3. GIS Database: PostgreSQL/PostGIS, MongoDB, SQLite/SpatiaLite

| Criterion | PostgreSQL + PostGIS | MongoDB GeoJSON | SQLite + SpatiaLite |
|---|---|---|---|
| Distance/geometry search | Yes | Yes | Yes |
| Structured related tables and audit events | Strong | Design-specific | Supported |
| Concurrent multiuser backend | Suitable | Suitable | More limited |
| Prototype deployment | Moderate | Moderate | Low |
| Best fit | **Selected** | Alternative | Minimal local experiment |

**Decision:** PostgreSQL with PostGIS. Its spatial indexes and `ST_DWithin` searches are useful for candidate evidence matching, while relational references preserve separate location, observation, mission and history records [T4]. MongoDB remains a viable alternative; PostGIS fits the proposed relational event history more directly. The distance threshold creates a proposed association and cannot prove that two observations concern the same physical site.

## 5.4. Backend: FastAPI, Django REST Framework, Express

| Criterion | FastAPI | Django REST Framework | Node.js / Express |
|---|---|---|---|
| Primary language | Python | Python | JavaScript/TypeScript |
| Python model integration | Direct | Direct | Separate Python process/API |
| Generated OpenAPI endpoints | Built-in | Configuration/package | Additional packages |
| Admin scaffolding | Minimal | Django Admin | Minimal |
| Choice | **Selected** | Viable alternative | Viable alternative |

**Decision:** FastAPI for validated HTTP APIs connecting PWA, PostGIS and Python processing [T5]. Long-running training and satellite raster inference will run outside ordinary HTTP requests, initially as controlled local/offline jobs instead of a microservice fleet.

## 5.5. Frontend and Mapping

| Decision | Alternatives | Choice / reason |
|---|---|---|
| UI framework | React, Vue, Angular | **React + TypeScript:** shared components for citizen and inspector views |
| Interactive map | Leaflet, MapLibre GL JS, OpenLayers | **Leaflet:** sufficient markers/geometry with lower initial complexity |
| Mobile delivery | Responsive site, PWA, native mobile | **Mobile-first PWA:** one browser application; full offline submission out of scope |

Leaflet and the chosen mapping tiles are distinct dependencies: the library is available for local development, but the provider of production basemaps must allow the intended use [T6]. Browser-installable PWA behavior should not be confused with an implemented offline data-sync engine. React/TypeScript and Leaflet support a single application with separate role-sensitive screens.

## 5.6. Satellite Raster Handling: Rasterio, GDAL, OpenCV/Pillow

| Alternative | Suitable functions | Limitation |
|---|---|---|
| **Rasterio (selected)** | GeoTIFF, CRS, affine transforms, tile windows | Requires careful CRS/tiling validation |
| GDAL | Broad geospatial processing | More complex API for small Python MVP |
| OpenCV/Pillow | Cropping, resizing, image manipulations | Does not independently provide reliable georeferencing |

The model predicts bounding boxes in tile-relative pixel positions. Rasterio enables translating these positions through the source raster transform into mapped locations [T7]. SWAD JPEG crops cannot be assumed to contain the same georeferencing as separate licensed pilot GeoTIFFs; training labels and production geographic coordinates are separate concepts.

## 5.7. Support for the Three Extended Features

**Smart Verification Missions:** React form/dashboard + FastAPI mission endpoints + PostGIS location/observation references + file attachments; rule-based queue reasons, reviewer statuses and audit history.

**Re-Dumping Alerts:** event/history model plus date-sensitive geographic association rules. Use *observation or satellite acquisition date*, not import time. Duplicate active alerts must be prevented. Unknown dates route for review.

**Continuous Model Improvement:** reviewer-approved satellite crops/labels, license and scene checks, versioned manifest, explicit offline PyTorch experiment, recorded baseline comparison and model release selection. Ground photographs are kept as field evidence; satellite crops require their own annotation and review before training. Model releases require approval.

## 5.8. Stack Decision and Pending Validation

| Component | Proposed stack |
|---|---|
| Detector | PyTorch, small YOLO candidate, Faster R-CNN baseline |
| Geospatial image preprocessing | Rasterio; OpenCV/Pillow where appropriate |
| API | FastAPI |
| Geospatial persistence | PostgreSQL + PostGIS |
| Interface | React + TypeScript PWA |
| Map | Leaflet with appropriately licensed tiles |
| Engineering collaboration | GitHub + YouTrack |
| Feedback training | Offline reproducible experiments and gated release |

Major open dependencies are corrected independent evaluation splits, rights to research and pilot imagery, license suitability for chosen YOLO code/weights and the actual available compute. The detector configuration will be finalized after benchmark experiments.

## Technology Sources

[T1] Ultralytics licensing: https://www.ultralytics.com/license

[T2] Torchvision object detection guide: https://docs.pytorch.org/tutorials/intermediate/torchvision_tutorial

[T3] RT-DETR official repository: https://github.com/lyuwenyu/RT-DETR

[T4] PostGIS `ST_DWithin`: https://postgis.net/documentation/tips/st-dwithin/

[T5] FastAPI documentation: https://fastapi.tiangolo.com/

[T6] Leaflet: https://leafletjs.com/

[T7] Rasterio georeferencing: https://rasterio.readthedocs.io/en/latest/topics/georeferencing.html

[T8] MongoDB geospatial queries: https://www.mongodb.com/docs/manual/geospatial-queries/
