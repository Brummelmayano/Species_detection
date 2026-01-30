# Component Specifications

## Backend API Specifications

### Endpoints

#### Batch Management
- `POST /api/batches` - Create new batch
  - Body: `{name: string, files: multipart}`
  - Returns: `{batch_id: string, status: 'uploading'}`
- `GET /api/batches` - List batches
  - Query: `?status=processed&limit=10`
  - Returns: `[{id, name, status, upload_date, total_images, processed_images}]`
- `GET /api/batches/{id}` - Get batch details
- `DELETE /api/batches/{id}` - Delete batch

#### Image Management
- `GET /api/batches/{batch_id}/images` - List images in batch
- `GET /api/images/{id}` - Get image details with detections
- `GET /api/images/{id}/file` - Download original image
- `GET /api/images/{id}/annotated` - Download image with annotations

#### Species Management
- `GET /api/species` - List all detected species
- `GET /api/species/{id}` - Get species details

#### Reporting
- `GET /api/reports/species-inventory?batch_id=123` - Species inventory report
- `GET /api/reports/temporal?start_date=2024-01-01&end_date=2024-12-31` - Temporal analysis
- `POST /api/reports/export` - Export data
  - Body: `{format: 'csv', filters: {...}}`

### Data Models

#### Batch
```python
class Batch:
    id: str
    name: str
    upload_date: datetime
    status: Literal['uploading', 'processing', 'completed', 'failed']
    total_images: int
    processed_images: int
```

#### Image
```python
class Image:
    id: str
    batch_id: str
    filename: str
    path: str
    width: int
    height: int
    upload_date: datetime
    process_date: Optional[datetime]
    status: Literal['uploaded', 'processing', 'processed', 'failed']
    latitude: Optional[float]
    longitude: Optional[float]
```

#### Detection
```python
class Detection:
    id: str
    image_id: str
    species_id: str
    confidence: float
    bbox_x: float
    bbox_y: float
    bbox_w: float
    bbox_h: float
    detection_date: datetime
```

## Frontend Component Hierarchy

### App Structure
```
App
├── Header
├── Sidebar
│   ├── Navigation
│   └── UserMenu
├── MainContent
│   ├── Dashboard (default)
│   ├── UploadPage
│   ├── GalleryPage
│   ├── ImageViewerPage
│   ├── ReportsPage
│   └── SettingsPage
└── Footer
```

### Key Components

#### UploadZone
- Props: `onFilesSelected`, `maxFileSize`, `acceptedTypes`
- State: `isDragOver`, `uploadProgress`
- Features: Drag-drop, file validation, progress bar

#### ImageGallery
- Props: `images`, `onImageClick`, `filters`
- Features: Grid layout, lazy loading, filtering, sorting

#### AnnotationViewer
- Props: `image`, `detections`, `onDetectionClick`
- Features: Canvas rendering, zoom/pan, bbox selection

#### DataTable
- Props: `data`, `columns`, `sortable`, `filterable`
- Features: Pagination, export, search

#### ChartComponent
- Props: `data`, `type`, `options`
- Uses: Chart.js wrapper

## AI Integration Specifications

### SpeciesNet Wrapper
```python
class SpeciesNetProcessor:
    def __init__(self, model_path: str):
        self.model = SpeciesNet(model_path)
        self.confidence_threshold = 0.5

    def process_image(self, image_path: str) -> List[Detection]:
        """Process single image and return detections"""
        predictions = self.model.predict([image_path])
        return self._parse_predictions(predictions)

    def process_batch(self, image_paths: List[str]) -> Dict[str, List[Detection]]:
        """Process multiple images"""
        predictions = self.model.predict(image_paths)
        return {path: self._parse_predictions(pred) for path, pred in predictions.items()}

    def _parse_predictions(self, prediction_dict: dict) -> List[Detection]:
        """Convert SpeciesNet output to Detection objects"""
        # Implementation details...
```

### Processing Pipeline
1. Load image
2. Validate format/size
3. Run SpeciesNet inference
4. Filter detections by confidence
5. Extract bounding boxes
6. Parse species taxonomy
7. Return structured data

### Performance Optimization
- Batch processing for multiple images
- GPU acceleration if available
- Memory management for large batches
- Caching of model in memory