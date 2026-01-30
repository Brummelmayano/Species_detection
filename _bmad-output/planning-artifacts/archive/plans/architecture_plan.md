# Species Detection Application Architecture

## Overview
A web-based application for processing camera trap images using SpeciesNet AI model to detect wildlife species. Designed for researchers conducting biodiversity monitoring in tropical environments.

## System Architecture

### High-Level Components
- **Frontend**: Web interface for user interaction
- **Backend**: API server handling business logic and AI processing
- **Database**: Data storage for images and detections
- **AI Model**: SpeciesNet integration for species detection
- **Storage**: File storage for images and processed results

### Technology Stack
- **Frontend**: React.js or Vue.js with HTML5 Canvas for image visualization
- **Backend**: Python FastAPI for high-performance API
- **Database**: PostgreSQL for structured data, file system for images
- **AI**: SpeciesNet Python package
- **Deployment**: Docker containers for portability

### Architecture Diagram
```
[User Browser]
    |
    v
[Frontend Web App] <--- HTTP --->
    |
    v
[Backend API Server]
    |   ^
    |   | (AI Processing)
    v   |
[Database]     [SpeciesNet Model]
    |
    v
[File Storage]
```

## Component Details

### Frontend

#### Pages
- **Dashboard**: Overview statistics, recent batches, processing queue
- **Upload**: Drag-drop file upload, batch naming, progress tracking
- **Gallery**: Grid view of processed images with detection previews
- **Image Viewer**: Full-size image with interactive bounding boxes, detection details
- **Reports**: Data visualization, filtering, export options
- **Settings**: Configuration for thresholds, model parameters

#### Key Components
- **Upload Zone**: Accepts folders/images, validates file types, shows upload progress
- **Image Gallery**: Thumbnail grid with detection counts, status indicators
- **Annotation Viewer**: Canvas-based image display with clickable bounding boxes
- **Detection Table**: Sortable table of all detections with species, confidence, location
- **Charts**: Species abundance charts, temporal distribution graphs
- **Export Tools**: CSV/JSON download, report generation

#### User Experience
- Responsive design for desktop/mobile
- Real-time progress updates via WebSockets
- Offline capability for viewing cached results
- Keyboard shortcuts for navigation
- Accessibility features (ARIA labels, keyboard navigation)

### Backend
- RESTful API endpoints:
  - POST /upload - Upload image batch
  - GET /images - List processed images
  - GET /images/{id} - Get image details and detections
  - POST /reports - Generate reports
- Asynchronous processing with background tasks
- SpeciesNet model loading and inference
- Data validation and error handling

### Database Schema

#### Tables

**batches**
- id (PK)
- name (string)
- upload_date (datetime)
- status (enum: uploading, processing, completed, failed)
- total_images (int)
- processed_images (int)

**images**
- id (PK)
- batch_id (FK to batches)
- filename (string)
- path (string)
- width (int)
- height (int)
- upload_date (datetime)
- process_date (datetime, nullable)
- status (enum: uploaded, processing, processed, failed)
- latitude (float, nullable)
- longitude (float, nullable)

**detections**
- id (PK)
- image_id (FK to images)
- species_id (string, from model)
- confidence (float)
- bbox_x (float) - normalized x coordinate
- bbox_y (float) - normalized y coordinate
- bbox_w (float) - normalized width
- bbox_h (float) - normalized height
- detection_date (datetime)

**species**
- species_id (PK, from model)
- scientific_name (string)
- common_name (string)
- kingdom (string)
- phylum (string)
- class (string)
- order (string)
- family (string)
- genus (string)
- species (string)

#### Indexes
- images.batch_id
- detections.image_id
- detections.species_id

### AI Integration
- Model loading on startup
- Batch processing of images
- Confidence thresholding
- Bounding box extraction
- Species classification with taxonomy

## Data Flow

### Image Processing Pipeline
1. **Upload Phase**
   - User selects images/folders in frontend
   - Frontend validates file types (jpg, png) and sizes
   - Multipart upload to backend API

2. **Ingestion Phase**
   - Backend validates uploaded files
   - Saves images to persistent storage with unique IDs
   - Creates database records (status: 'uploaded')
   - Returns batch ID for tracking

3. **Processing Phase** (Asynchronous)
   - Background worker loads SpeciesNet model
   - For each image:
     - Load image
     - Run detection (find animal bounding boxes)
     - Run classification (identify species with confidence)
     - Filter detections by confidence threshold (>0.5)
     - Store detections in database
   - Update image status to 'processed'
   - Send completion notification

4. **Retrieval Phase**
   - Frontend queries processed images by batch ID
   - Displays gallery with annotated images
   - Shows detection details in tables
   - Allows export of results

5. **Reporting Phase**
   - Aggregate detections by species/location/date
   - Generate CSV/JSON reports
   - Create visualizations (charts, maps)

### Error Handling
- Invalid file formats: reject with error message
- Processing failures: mark as 'failed', log errors
- Large batches: chunk processing, progress tracking
- Model loading failures: retry mechanism

## Reporting and Analytics

### Report Types
- **Species Inventory**: Complete list of detected species with counts, confidence ranges
- **Temporal Analysis**: Detection trends over time (daily/weekly/monthly)
- **Spatial Analysis**: Distribution maps if GPS data available
- **Activity Patterns**: Detections by hour of day, seasonal patterns
- **Batch Summary**: Statistics for uploaded batches (success rate, processing time)

### Analytics Features
- **Diversity Metrics**: Species richness, Shannon diversity index
- **Abundance Charts**: Bar charts, pie charts of species counts
- **Trend Analysis**: Time series plots with moving averages
- **Comparative Reports**: Compare multiple batches or time periods
- **Custom Queries**: Filter by species, confidence, date range, location

### Export Formats
- CSV: Tabular data for spreadsheet analysis
- JSON: Structured data for API integration
- PDF: Formatted reports with charts
- Shapefile: GIS data for spatial analysis

### Visualization Libraries
- Chart.js or D3.js for charts
- Leaflet.js for maps
- DataTables for interactive tables
- Canvas API for image annotations

## Security Considerations
- Input validation for uploaded files
- Rate limiting for API calls
- Secure file storage paths
- No sensitive data exposure

## Deployment Options

### Local Development
- **Docker Compose**: Containerized environment with PostgreSQL, backend, frontend
- **Conda Environment**: Python environment with all dependencies
- **Standalone**: Direct Python execution for development

### Production Deployment
- **Docker Containers**: Backend and frontend in separate containers
- **Cloud Platforms**:
  - AWS ECS/Fargate for container orchestration
  - Google Cloud Run for serverless
  - Azure Container Instances
- **Kubernetes**: For scalable, multi-region deployments

### Colab Integration
- **Demo Mode**: Simplified version running in Colab notebooks
- **API Access**: Connect Colab to external API for processing
- **Hybrid**: Use Colab for GPU processing, local for storage

### Infrastructure Requirements
- **Compute**: CPU/GPU depending on model size (SpeciesNet works on CPU)
- **Storage**: 100GB+ for images and database
- **Memory**: 8GB+ RAM for model loading
- **Network**: Fast upload/download for large image batches

## Summary and Next Steps

### Architecture Overview
This architecture provides a complete solution for automated species detection in camera trap images using SpeciesNet AI. The system supports batch processing, real-time results visualization, and comprehensive reporting for wildlife monitoring research.

### Key Features
- **Automated Processing**: End-to-end pipeline from upload to species identification
- **Scalable Design**: Supports local deployment to cloud scaling
- **Rich UI**: Intuitive interface for researchers with advanced visualization
- **Flexible Reporting**: Multiple export formats and analytical tools
- **Robust Integration**: Seamless SpeciesNet AI model integration

### Implementation Phases
1. **Phase 1**: Backend API and database setup
2. **Phase 2**: SpeciesNet integration and processing pipeline
3. **Phase 3**: Frontend development and UI components
4. **Phase 4**: Reporting and analytics features
5. **Phase 5**: Testing, deployment, and documentation

### Risk Mitigation
- Model dependency: Include fallback processing options
- Large datasets: Implement pagination and lazy loading
- Performance: Optimize for CPU processing, add GPU support later
- Data integrity: Comprehensive validation and error handling

### Success Metrics
- Processing accuracy >95% for high-confidence detections
- UI response time <2 seconds
- Support for batches of 1000+ images
- Export functionality for research workflows

## Scalability
- Horizontal scaling of backend instances
- Database connection pooling
- Caching for frequently accessed data
- Batch processing optimization