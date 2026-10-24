# SWAD v2 audit — provenance and limitations

Files in this folder record a student-run automated scan of a public YOLOv8-formatted distribution dated 21 October 2026. All 1,996 images and paired labels were processed, with 5,562 structurally valid boxes. The 102 perceptually similar cross-split pairs are **candidates** rather than confirmed duplicates; two manually inspected pairs were reported as confirmed same-scene overlaps. The original train/test splits are therefore not suitable for independent performance claims.

The complete manual bounding-box inspection, source-scene independence validation and license verification are not complete. Raw imagery is excluded from this repository. The full audit JSON records the limitations and an export-specific dataset fingerprint. The image manifest contains relative filenames and hashes, not a redistribution of imagery.
