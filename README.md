# AI-Based Real-Time Helmet Detection and Violation Monitoring System

An AI-based computer vision system that detects whether individuals are wearing helmets in real time using a custom-trained YOLO11 model and OpenCV.

## Project Overview

This project uses computer vision and deep learning to automatically detect helmet compliance from a live camera feed.

The system can:

- Detect people wearing helmets
- Detect people without helmets
- Display real-time detection results
- Detect helmet violations
- Capture evidence of violations
- Detect multiple people simultaneously
- Track detected objects using YOLO tracking

## Technology Stack

- Python
- OpenCV
- Ultralytics YOLO11
- PyTorch
- Computer Vision
- Object Detection
- Object Tracking

## System Architecture

Camera
↓
OpenCV
↓
YOLO11 Detection
↓
Helmet Classification
↓
Violation Detection
↓
Evidence Capture

## Dataset

The model was trained using a helmet detection dataset containing two classes:

- With Helmet
- Without Helmet

Dataset split:

- Training: 1185 images
- Validation: 127 images
- Testing: 64 images

Total: 1376 images

## Model Evaluation

Test-set results:

| Metric | Result |
|---|---:|
| Precision | 86.6% |
| Recall | 68.3% |
| mAP@50 | 78.1% |
| mAP@50-95 | 42.5% |

### Class-wise Results

| Class | Precision | Recall | mAP@50 |
|---|---:|---:|---:|
| With Helmet | 90.3% | 82.4% | 92.0% |
| Without Helmet | 83.0% | 54.2% | 64.2% |

## Current Features

- Real-time camera detection
- Helmet / no-helmet classification
- Multiple-person detection
- Violation alerts
- Violation evidence capture
- Object tracking

## Future Development

Planned improvements include:

- Individual violation tracking
- Persistent person re-identification
- Violation database
- Cloud-based storage
- REST API
- Monitoring dashboard
- Model improvement for difficult lighting and camera angles

## Project Status

🚧 Currently under development.

The core real-time helmet detection and violation detection pipeline is functional. Cloud monitoring and persistent identity management are planned for future stages.
