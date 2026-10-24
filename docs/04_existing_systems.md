# 4. Existing System Comparison

## 4.1. Method and Evaluation Criteria

Four operationally relevant platforms were compared on nine consistent criteria using their public documentation: **Kazakhstan Garysh Sapary satellite waste monitoring**, **TazaQazBot / Taza Kazakhstan**, **TazaQala**, and **TrashOut**. The review uses published feature descriptions. **Yes** indicates a documented capability; **N/D** indicates that the available documents do not establish it. **Staff** refers to mobile access for environmental officials.

## 4.2. Kazakhstan Garysh Sapary

Kazakhstan Garysh Sapary describes a national space-based waste monitoring process using high-resolution KazEOSat-1 imagery, site coordinates, a GIS portal, filters and statistics, cleanup comments entered by environmental departments, and the Waste Viewer/Waste Edit mobile applications for field use [S1]. Its website describes attaching field photos, videos, audio or documents. Its geospatial monitoring, field inspection and cleanup recording functions closely match several modules in the proposed system. A government summary reports 2,637 sites detected in 2026 by September [S2].

**Assessment:** Kazakhstan Garysh Sapary already covers satellite mapping, field inspection and cleanup tracking. Public technical documentation does not specify the detector's evaluation metrics or how citizen reports, if linked, are matched to satellite observations.

## 4.3. TazaQazBot / Taza Kazakhstan

The government reporting service enables citizens to submit a photograph, address or geolocation, and description through Telegram or eGov Mobile. Submissions are routed to responsible executive bodies; officials can complete work and attach photographic evidence [S3]. Published reports also describe status visibility and complaint categories. The service provides an established channel for citizen reports and government follow-up.

**Assessment:** the documented workflow centers on receiving, assigning and resolving reports. The material reviewed does not describe satellite object detection or the technical method used to reconcile reports with other government monitoring data.

## 4.4. TazaQala

TazaQala, associated with environmental organizations and KazNU in Almaty, provides citizen reports with photos and map locations, AI-assisted **photo moderation**, a public map, statuses, before-and-after cleanup records and participation incentives [S4], [S5]. Its guide allows anonymous submission and notes duplicate reports as a possible moderation outcome. These functions closely resemble the planned citizen interface and case tracking.

**Assessment:** TazaQala already provides mobile reporting, moderation and evidence of cleanup. Its documented photo moderation differs from bounding-box detection on georeferenced satellite images. The available guide does not explain whether the platform reconciles citizen reports with satellite detections.

## 4.5. TrashOut

TrashOut is an international reporting and cleanup platform. It offers mobile submissions of illegal dumps, mapped locations, participation by municipalities/organizations, updates and coordination [S6]. It serves as a comparison for the citizen/organizational workflow. Public documentation examined for this report does not describe satellite-based bounding-box detection or a cross-source evidence-matching evaluation.

## 4.6. Comparative Matrix

| Criterion | Garysh Sapary | TazaQazBot | TazaQala | TrashOut |
|---|---|---|---|---|
| Satellite-derived waste locations | Yes | N/D | N/D | N/D |
| Geolocated citizen photo reporting | N/D | Yes | Yes | Yes |
| Mobile access | Staff | Yes | Yes | Yes |
| Site mapping / geographic visualization | Yes | N/D | Yes | Yes |
| Institutional or organizational review | Yes | Yes | Yes | Yes |
| Cleanup statuses and supporting evidence | Yes | Yes | Yes | Yes |
| AI image analysis | Method N/D | N/D | Photo AI | N/D |
| Documented satellite-to-citizen site association | N/D | N/D | N/D | N/D |
| Documented user-facing multi-date satellite comparison | N/D | N/D | N/D | N/D |

The table compares documented functions rather than accuracy or service quality. Technical performance cannot be ranked from the available public descriptions.

## 4.7. Relevance, Overlap and Proposed Contribution

Existing platforms already cover mapping, reporting, field work, moderation and cleanup history. Kazakhstan's monitoring ecosystem also combines satellite observation with digital citizen feedback at the service level.

The proposed prototype will implement and test a complete site-level workflow: satellite detection → geographic association with citizen reports → verification mission → cleanup history → reinspection alert for later evidence → reviewed satellite sample → offline model update. The evaluation will cover detection metrics, correct evidence matches, temporal alert rules and model version controls.

The relevance of revisiting previously cleared locations is supported by the Abai Region prosecutor report: some later detections shared coordinates with previously recorded sites [S7]. This justifies repeated monitoring while leaving unresolved whether a given recurrence represents incomplete cleanup or subsequent dumping.

## 4.8. Conclusion

The comparison provides design references for the reporting and inspection interfaces, while narrowing the development focus to data integration and verifiable workflow behavior. The system will be evaluated as an engineering prototype rather than compared on national operational coverage.

## Sources for Section 4

[S1] Kazakhstan Garysh Sapary official waste monitoring: https://km.gharysh.kz/courses/waste

[S2] Official 2026 monitoring figures: https://www.gov.kz/org/cerc/press/news/details/1293504?lang=ru

[S3] Taza Kazakhstan government information: https://www.gov.kz/org/cerc/press/news/details/1246692?lang=ru

[S4] TazaQala: https://tazaqala.com/ru/

[S5] TazaQala citizen guide: https://www.tazaqala.com/ru/guide

[S6] TrashOut: https://www.trashout.ngo/organizations

[S7] Abai prosecutor report: https://www.gov.kz/org/prokuratura-abay/press/news/details/1031151?lang=ru
