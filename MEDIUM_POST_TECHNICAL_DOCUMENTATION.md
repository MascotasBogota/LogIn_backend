# Building PatitasBog: A Comprehensive Pet Management System Using Modern Web Technologies

_An Academic Software Engineering Project - Universidad Nacional de Colombia_

**Authors:**
[Martin Moreno Jara](https://www.linkedin.com/in/martin-moreno-jara-250977242/),
[Juan Esteban Cardenas Huertas](https://www.linkedin.com/in/juan-huertaszz/),
[Juan David Ardila Diaz](https://www.linkedin.com/in/luis-felipe-tolosa-sierra-4441a2267/),[Luis Felipe Tolosa Sierra](https://www.linkedin.com/in/luis-felipe-tolosa-sierra-4441a2267/),
[David Alejandro Cifuentes Gonzalez](https://www.linkedin.com/in/dcifuentesg/),
[Keynes Stephens Watson](https://www.linkedin.com/in/keynes-stephens-watson-844550288/)

---

## Abstract

This technical post documents the complete development journey of PatitasBog, a
comprehensive pet management system developed as part of our Software
Engineering 2 course. Through three iterative prototypes, we built a full-stack
web application that addresses real-world challenges in pet care, lost pet
recovery, and community engagement. This academic project demonstrates our
technical capabilities in modern web development, project management, and
iterative software development methodologies.

**Disclaimer:** This is an academic project and we acknowledge that it still has
areas for improvement and optimization.

---

## 1. Introduction and Project Vision

### 1.1 Problem Statement

Pet ownership brings immense joy but also significant responsibilities and
challenges. Our research identified three critical pain points in the pet care
ecosystem:

1. **Lost Pet Recovery:** Inefficient processes for reporting and finding lost
   pets
2. **Information Fragmentation:** Scattered resources for pet care education
3. **Community Disconnection:** Lack of centralized platforms for pet owner
   collaboration

### 1.2 Solution Overview

PatitasBog emerged as a comprehensive digital solution designed to address these
challenges through:

- **Centralized Pet Management:** Digital profiles and health records
- **Community-Driven Lost Pet System:** Real-time reporting and search
  capabilities
- **Educational Resources:** Curated content for responsible pet ownership
- **Notification System:** Automated alerts for community engagement

### 1.3 Academic Context

This project was developed following iterative and incremental methodologies,
with three distinct prototypes spanning 4 months of development. Each iteration
focused on expanding functionality while maintaining code quality and
architectural integrity.

### 1.4 Project Goals achieved

1. **User Authentication and Authorization:** Implemented secure user login and
   registration, as well as useful feature such as password recovery and profile
   management.
2. **Lost Pet Reporting System:** Developed a comprehensive system for reporting
   lost pets, including location and images.
3. **Community Engagement:** Fostered a sense of community through user profiles
   and interaction, and through the user reputation system, which rewards
   helpful contributions and penalizes unhelpful ones.
4. **Scalable Architecture:** Designed a flexible decoupled architecture to
   accommodate future features, integrating microservices for modularity.

---

## 2. Planning structure and methodology

### 2.1 Project Planning

A careful process of thought was put into the planning of this project. First,
identifying the functional requirements and then grouping them into the modules
that would be developed in each increment. In the planning phase, we organized
these increments in epics and user stories, which were then prioritized based on
their importance to the project. The epics we defined, alongside some of their
functional requirements, are as follows:

#### 2.1.1 Epics and Functional Requirements

- **User Management:** Authentication, profile management, password recovery.
- **Lost Pet Reporting:** Create, filter, and manage lost pet reports, upload
  pet images, select last known location of the pet and marking the report as
  solved.
- **Responses to reports:** Create and manage different types of responses to
  lost pet reports, including sightings and findings.
- **Notification System:** Implement a notification system for users to receive
  updates on lost pet reports.
- **User Reputation System:** Develop a user reputation system to encourage
  community engagement and reward helpful contributions.
- **Educational Content:** Create and manage educational content related to pet
  care, including articles, tips, and resources.

#### 2.1.2 Roadmap

Once we defined the epics and functional requirements, we created a roadmap to
guide the development process. The roadmap was divided into three main
increments, each with its own set of features and objectives. Each increment was
planned to be developed in a 4-week sprint. The roadmap is as follows:

1. **Increment 1: MVP. User Management, Reporting and responses** The main goal
   of this increment was to establish the foundation of the application,
   delivering the core functionalities of the application in order to accomplish
   the MVP. The main features of this increment were:
   - User registration and login system
   - Basic profile management
   - Report creation and management
   - Response system for reports
1. **Increment 2: Notification and Reputation System** The main goal of this
   increment was to enhance user engagement and trust within the platform. The
   main features of this increment were:
   - Notification system for report updates
   - User reputation system implementation
1. **Increment 3: Educational Content and Final Enhancements** The main goal of
   this increment was to provide users with valuable information and resources
   related to pet care, as well as improving already developed features of the
   application. The main features of this increment were:
   - Educational content management
   - Performance optimization
   - Final enhancements and bug fixes
   - Observability and monitoring implementation

However, due to time constraints, we had to adapt the development process to
only two iterations, as the planning phase took up the first one. Thus, the
first and second increments were merged into one, and the third increment was
developed as the final version of the application.

#### 2.1.3 Team management

The project was developed by a team of 6 members, each with specific roles and
responsibilities. While we did not implement a formal agile methodology such as
Scrum, due to the difficulty of coordinating all necessary meetings, we did
follow some agile principles such as iterative development and continuous
feedback, as well as assertive communication. We divided the team into smaller
2-men groups, each responsible for specific tasks and features. This allowed us
to work in parallel and deliver the project in a timely manner.

---

## 3. Design and Architecture

### 3.1 Architecture Overview

The architecture of the application is based on SOFEA (Service-Oriented Frontend
Architecture), by which each backend service is developed in a separate
repository, and the frontend is developed as a separate application that
consumes the backend services through REST APIs. Though this architectural style
is not so widely used in real life applications, due to the academic nature of
the project, we decided to use it in order to learn and practice good software
engineering practices, such as modularity, separation of concerns, and
scalability.

### 3.2 Modular Design and components

![Application architecture](final%20components.png)

The diagram shows the components of the application architecture in their
entirety, as well as the relationships between them. As indicated previously, a
SOFEA approach was implemented, under which the different proposed modules were
developed as REST APIs and integrated through the Front End to deliver the
application. However, communication between services could not be limited to
integration with the Front End, as some services depend on others to function
and make requests to each other to perform their tasks (this is denoted in the
diagram by the dotted arrows). Subsequently, to properly develop some
functionalities, it was necessary to use third-party services, which were
implemented through their APIs and development tools in Flask.

#### 3.2.1 Module segmentation and components

The final version of the application includes the following modules:

##### Front End (React):

- Main frontend component
- Educational module

###### Backend services (APIs developed in Flask):

- User management module
- Reports and responses module
- Notifications module
- User reputation module

###### Database (MongoDB hosted on Atlas):

- User database
- Reports and responses database

###### Third-party services:

- Observability: Open Telemetry, Prometheus, Grafana
- Image storage: Supabase storage
- Mail service: Email sender

Additionally, the integration testing module groups all the previous modules to
verify the application's correct operation.

#### 3.2.2 Component explanation

The backbone of the application is the user management and reports and responses
modules. Each module has its own database, which can only be accessed (written
or queried) through these modules and not through external modules, in order to
implement best practices. The user management module uses the Email Sender
service to send emails to Gmail domains for the password reset functionality.
Meanwhile, the reports and responses module uses supabase storage, a cloud
storage service, to store pet images that users can upload in reports and
responses. Initially, this functionality was managed by saving the images
locally, but it was decided to change this due to its infeasibility. Thus, when
images are uploaded, a public URL is generated to load them on the front end.

Both the notifications service and the user reputation service depend on the two
aforementioned services, as they must use their functionalities or access their
databases. All backend service modules were then configured to display metrics
that show the performance and error of each service. Open Telemetry was used in
conjunction with Prometheus to obtain observability information, which is then
displayed in Grafana.

All services connect to the Front End, which handles user requests and
interactions with the system, following the aforementioned SOFEA architectural
style. Finally, the integration testing module integrates the entire application
to ensure stable operation and consistent communication between all modules.

### 3.3 Technology Stack Justification

#### Frontend Technologies

- **React 18.2:** Chosen for its component-based architecture and robust
  ecosystem
- **Vite:** Selected over Create React App for faster development builds and
  better performance
- **CSS Modules:** Provides scoped styling to prevent conflicts in our modular
  component structure
- **React Router:** Enables SPA navigation with clean URL structures

#### Backend Technologies

- **Flask 2.3:** Lightweight Python framework suitable for our microservices
  approach
- **Flask-RESTX:** Provides automatic Swagger documentation and API
  standardization
- **Flask-JWT-Extended:** Implements secure authentication with token-based
  sessions
- **MongoDB:** Document-based storage aligns with our flexible data schemas

#### Development Tools

- **Git/GitHub:** Version control with feature branch workflow
- **Docker:** Containerization for consistent deployment environments
- **Pytest:** Comprehensive testing framework for backend services

### 2.3 Database Design

Our MongoDB schema leverages document flexibility while maintaining data
integrity:

```json
{
  "users": {
    "_id": "ObjectId",
    "email": "string",
    "password": "hashed_string",
    "profile": {
      "firstName": "string",
      "lastName": "string",
      "phone": "string",
      "address": "string"
    },
    "pets": ["ObjectId references"]
  },

  "reports": {
    "_id": "ObjectId",
    "type": "lost|found",
    "petInfo": {
      "name": "string",
      "species": "string",
      "breed": "string",
      "description": "string"
    },
    "location": {
      "coordinates": [longitude, latitude],
      "description": "string"
    },
    "images": ["string paths"],
    "status": "active|resolved|expired",
    "timestamp": "ISO Date"
  }

}
```

---

## 4. Functional increments and system evolution

### 4.1 Iterative Development Approach

For this class' deliverables, we adopted an iterative development approach,
dividing the project into three main prototypes, each building upon the previous
one. These prototypes include both the planning phase and the development,
allowing us to gradually implement features and improve the system based on
feedback and testing.

Due to time constraints, though we had planned to develop the project in three
development cycles, we had to adapt the development process to fit the academic
schedule. As a result, the development takes up two out of the three prototypes,
with the first prototype being the planning phase.

#### Prototype 1: Planning (Weeks 1-2)

**Objectives:** Define project scope, user stories, and technical

- Identify core features and user needs
- Establish technical stack and architecture
- Create initial wireframes and UI designs
- Set up development environment and version control
- Define project milestones and deliverables

**Key Achievements:**

- Completed requirement analysis
- Defined user stories and acceptance criteria
- Established project architecture and technology stack
- Set up GitHub organization and repository

**Justification:** Before starting the development, we needed to define the
scope of the project, the features to be implemented, and the technical
requirements.

#### Prototype 2: MVP (Weeks 3-8)

**Objectives:** User management and lost pet reporting system

- Implement user authentication and profile management
- Develop lost pet reporting system
- Create response system for lost pet reports
- Image upload and storage

**Key Achievements:**

- User registration and login system with JWT authentication
- Basic profile management with image upload
- Lost pet report creation and management
- Search and filtering of reports
- Response system for reports with image upload and

**Justification:** The main goal of this prototype was to deliver a functional,
yet unfinished, version of the application that could be used to test the core
functionalities of the system, following the MVP (Minimum Viable Product)
approach.

#### Prototype 3: Final Version (Weeks 9-12)

**Objectives:** Notification system, user reputation, and educational content

- Implement notification system for report updates
- Develop user reputation system based on report interactions
- Create educational content
- Improving the services developed in the previous prototypes
- Observability and monitoring implementation
- Integration testing module

**Key Achievements:**

- Notification system for real-time updates on reports
- User reputation system to encourage community engagement
- Educational content management with categorized articles
- Performance optimization and bug fixes
- Integration testing for all components
- Observability and monitoring with Open Telemetry, Prometheus, and

**Justification:** The main goal of this prototype was to deliver a complete
version of the application, with all the features implemented and tested, as
well as to improve the already developed features. This prototype also included
the implementation of observability and monitoring tools to ensure the system's
stability and performance.

### 4.2 Changes and insights

Even though we did a careful and detailed planning of the project, we had to do
some changes mid way through the development process because there were things
we did not foresee or that we did not take into account in the planning phase.
Some of these changes were:

- **Image storage:** Initially, we planned to store images locally, but we
  realized that this was not feasible due to the size of the images and the need
  for scalability. Thus, we decided to use Supabase storage, a cloud storage
  service, to store the images and generate public URLs for them.
- **Notification or Filters:** Initially, we had planned to implement a filter
  service for the reports, but we realized that this was not necessary as the
  search and filtering functionalities were already implemented in the reports
  and responses module. Thus, we decided to focus on the notification system
  instead, which was a more valuable feature to be implemented in a different
  repository.
- **Adjustment of the development timeline:** As previously mentioned, we had to
  adapt the development process to fit the academic schedule, which meant
  merging the first and second increments into one, and also adjusting the time
  we had planned for each one of them. Thus, the two 4-week increments were
  merged into one big 6-week increment. This required us to prioritize important
  features and be as efficient as possible.

### 3.2 Project Management Strategies

#### Version Control Workflow

We implemented a Git flow strategy with distinct branches:

- `main`: Production-ready code
- `develop`: Integration branch for features
- `feature/*`: Individual feature development
- `fix/*`: Bug fixes and hotfixes

---

## 5. Technical Implementation Details

Each module was developed as an independent service, and in a different
repository inside the team's GitHub organization. The modules we developed are
the following:

### 5.1 User management module

A detailed explanation of the user management module can be found in
[the module's repository](https://github.com/MascotasBogota/LogIn_backend.git).
This module is responsible for user authentication, profile management, and
password recovery. It uses Flask-JWT-Extended for secure token management and
bcrypt for password hashing, ensuring secure user authentication. The module
also includes password reset functionality and profile management, allowing
users to update their personal information and upload profile pictures.

#### Authentication and Security with JWT implementation

Our authentication system uses Flask-JWT-Extended for secure token management.
These tokens are then used throughout the application to authenticate user
requests. The following code snippet demonstrates the login endpoint, which
generates a JWT token upon successful authentication:

```python
from flask_jwt_extended import create_access_token, jwt_required

@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    user = User.find_by_email(email)
    if user and bcrypt.check_password_hash(user['password'], password):
        access_token = create_access_token(
            identity=str(user['_id']),
            expires_delta=timedelta(days=1)
        )
        return jsonify({
            'access_token': access_token,
            'user': serialize_user(user)
        }), 200

    return jsonify({'message': 'Invalid credentials'}), 401
```

#### Security Measures

- Password hashing using bcrypt
- CORS configuration for cross-origin requests
- Input validation and sanitization
- SQL injection prevention through parameterized queries

### 5.2 Reports and Responses Module

A detailed explanation of the reports and responses module can be found in
[the module's repository](https://github.com/MascotasBogota/2-Reportes-Respuestas.git).
This module is responsible for managing lost and found pet reports, including
creating, updating, and deleting reports, as well as filtering them by pet type
and location. It also includes a response system for users to interact with
reports, such as marking a report as solved or providing additional information.
The module uses MongoDB for data storage and Flask-RESTX for API development,
ensuring a robust and scalable solution.

The code snippets below illustrate the implementation of the report creation and
response:

**report creation**

```python
def create_report(data, user_id):
    try:
        return Report(
            user_id=user_id,
            pet_name=data['pet_name'],
            type=data['type'],
            description=data['description'],
            location=data['location'],
            images=data.get('images', [])
        ).save()
    except (ValidationError, KeyError, TypeError) as e:
        raise ValueError("Validation Error: " + str(e))
```

**Filter reports**

```python
def get_filtered_reports(report_type=None, location=None, radius=None):
    query = Q()

    if report_type:
        query &= Q(type=report_type)

    if location and radius:
        # MongoDB expects GeoJSON [long, lat]
        query &= Q(location__geo_within_center=[location, radius / 111000])  # metros a grados

    return Report.objects(query, status="open")
```

**Create Report**

```python
def create_response_service(report_id: str, data: dict, user_id: str) -> dict:

    try:
        report = Report.objects.get(id=report_id)
    except DoesNotExist:
        raise ServiceError('Report not found')
    if report.status != 'open':
        raise ServiceError('Cannot add responses to a closed report')

    # Forzar imagen para hallazgos
    if data['type'] == 'hallazgo' and not data.get('images'):
        raise ServiceError('Findings must include at least one image')
    resp = Response(
        report_id=report_id,
        resp_user_id=user_id,
        type=data['type'],
        comment=data['comment'],
        images=data.get('images', []),  # Lista de URLs de imágenes opcional
        location=data.get('location')
    )
    resp.save()

    return resp
```

**Image uploading**

```python
def handle_image_upload(file, user_id):
    is_valid, error = validate_file(file)
    if not is_valid:
        return False, error

    success, result = process_and_save_image(file, user_id)
    return success, result
```

The image uploading functionality goes much more in depth than this, as it
includes the connection to the Supabase storage service, the image processing
and resizing, and the generation of public URLs for the images. For more
information on this functionality, please refer to the module's repository.

### 5.3 Notifications Module

A detailed explanation of the notifications module can be found in
[the module's repository](https://github.com/MascotasBogota/Notification.git).
This module generates real-time notifications for report owners when their
reports are updated, such as when a response is added. It integrates with the
report and responses module to listen for changes in the reports and send
notifications to the users involved.

The following code snippet illustrates the notification creation process:

```python
def create_notification(self, report_id: str, response_id: str, response_data: Dict) -> Notification:
        try:

            report_owner_id = self._get_report_owner(report_id)

            notification_type = response_data.get('type', 'avistamiento')
            title = f"Nuevo {notification_type}"
            message = f"Se ha registrado un nuevo {notification_type} para tu reporte de mascota perdida"

            notification = Notification(
                user_id=report_owner_id,
                report_id=report_id,
                response_id=response_id,
                notification_type=notification_type,
                title=title,
                message=message,
                sighting_description=response_data.get('comment'),
                sighting_location=response_data.get('location'),
                sighting_images=response_data.get('images', []),
                sighting_time=response_data.get('created_at', datetime.utcnow())
            )

            notification.save()
            return notification

        except Exception as e:
            raise NotificationServiceError(f"Error al crear notificación: {str(e)}")
```

This code snippet shows how the notification is created when a new response is
added to a report. It retrieves the report owner's ID, constructs the
notification message, and saves it to the database.

### 5.4 User Reputation Module

A detailed explanation of the user reputation module can be found in
[the module's repository](https://github.com/MascotasBogota/4-UserReputation.git).
This module implements a user reputation system that rewards users for helpful
contributions and penalizes unhelpful ones. It tracks user interactions with
reports and responses, updating their reputation score based on their actions.
Namely, if a user responds to a report in a helpful way, a counter in their
profile is incremented, while if they respond in an unhelpful way, the counter
is decremented. This system encourages positive community engagement and helps
identify reliable users.

It is integrated with both the user management and reports and responses modules
to track user interactions and update reputation scores accordingly. The
following code snippet illustrates how the reputation score is updated based on
user actions:

```python
def rate_response(self,report_id:str,response_id: str, rating: str, user_id: str,token:str):
        # 1. Get response details to validate owner
        response_details = report_service_client.get_response_details(report_id,response_id)
        if not response_details:
            raise ConnectionError("❌ Could not connect to Report Service.")

        report_details = report_service_client.get_report_details(report_id)
        if not report_details:
            raise ConnectionError("❌ Could not connect to Report Service for report details.")

        if report_details.get("user_id") != user_id:
            raise PermissionError("❌ User is not the owner of the report.")

        response_type = response_details.get("type")
        author_id = response_details.get("resp_user_id")
        current_response_reviewed = response_details.get("reviewed")
        current_status = response_details.get("is_useful")  #

        # 2. Calculate reputation change
        delta = 0
        is_useful = False
        response_reviewed = False

        if response_type == "avistamiento":
            if rating == "useful":
                if current_response_reviewed is True and current_status is True:
                    raise ValueError("❌ This sighting has already been marked as useful.")
                delta = SIGHTING_USEFUL
                is_useful = True
            elif rating == "not_useful":
                if current_status is False:
                    raise ValueError("❌ A sighting that has not been previously marked as useful cannot be marked as not useful.")
                delta = SIGHTING_REMOVE
                is_useful = False
            else:
                raise ValueError("❌ Invalid rating for sighting. Only 'useful' or 'not_useful' are allowed.")

        elif response_type == "hallazgo":
            if rating == "useful":
                if current_response_reviewed is True and current_status is True:
                    raise ValueError("❌ this finding has already been marked as useful.")
                delta = FINDING_USEFUL
                is_useful = True
            elif rating == "false_finding":
                if current_response_reviewed is True and current_status is False:
                    raise ValueError("❌ this finding has already been marked as false.")
                delta = FINDING_FALSE
                is_useful = False
            else:
                raise ValueError("❌ Invalid rating for finding. Only 'useful' or 'false_finding' are allowed.")
        else:
            raise ValueError("❌ Invalid response type.")

        response_reviewed = True
        # 3. Update user reputation
        update_result = user_service_client.update_user_reputation(author_id, delta,token)
        if not update_result:
            raise ConnectionError("❌ Could not update user reputation.")

        # 4. Mark response as rated
        status_result = report_service_client.update_response_status(report_id,response_id,response_reviewed, is_useful,token)
        if not status_result:
            # Note: This could lead to an inconsistent state. A rollback or retry mechanism might be needed here.
            raise ConnectionError("❌ Could not update response status.")
        resObject = {"status": "success","resp_auth":author_id ,"new_reputation": update_result.get("reputation"), "response":status_result}

        return resObject
```

### 5.5 Frontend Architecture

#### Component Structure

Our React application follows a hierarchical component structure:

```javascript
src/
├── components/
│   ├── Common/          // Reusable UI components
│   ├── Auth/            // Authentication forms
│   ├── Profile/         // User profile management
│   ├── Reports/         // Pet reporting system
│   └── Education/       // Educational content
├── views/               // Page-level components
├── services/            // API communication
├── styles/              // CSS modules
└── utils/               // Helper functions
```

#### State Management

We implemented a custom context-based state management system:

```javascript
const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) {
      validateToken(token)
        .then((userData) => setUser(userData))
        .catch(() => localStorage.removeItem("token"))
        .finally(() => setLoading(false));
    } else {
      setLoading(false);
    }
  }, []);

  return (
    <AuthContext.Provider value={{ user, setUser, loading }}>
      {children}
    </AuthContext.Provider>
  );
};
```

### 5.6 Observability and Monitoring integration

A global monitoring solution was integrated to track application performance. To
achieve this, we used OpenTelemetry to instrument our services, allowing us to
collect metrics and traces. These metrics are then sent to Prometheus for
storage and analysis, and visualized in Grafana dashboards. But in order to
accomplish this we had to make a few changes in each module. Namely, we had to
install the necessary dependencies and add a piece of code to initialize
telemetry and expose a `metrics/` endpoint. The following code snippet
illustrates how we initialized the telemetry in each of the modules:

```python
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from prometheus_client import Counter, Histogram, generate_latest, REGISTRY
from flask import request
import time

REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total number of HTTP requests',
    ['method', 'endpoint']
)

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency in seconds',
    ['method', 'endpoint'],
    buckets=[0.1, 0.5, 1.0, 2.0, 5.0]
)

ERROR_COUNT = Counter(
    'http_errors_total',
    'Total number of HTTP errors',
    ['method', 'endpoint', 'status_code']
)

def init_telemetry(app):
    FlaskInstrumentor().instrument_app(app)

    @app.before_request
    def before_request():
        request._start_time = time.time()
        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=str(request.endpoint or 'none')
        ).inc()

    @app.after_request
    def after_request(response):
        latency = time.time() - request._start_time
        REQUEST_LATENCY.labels(
            method=request.method,
            endpoint=str(request.endpoint or 'none')
        ).observe(latency)

        if response.status_code >= 400:
            ERROR_COUNT.labels(
                method=request.method,
                endpoint=str(request.endpoint or 'none'),
                status_code=str(response.status_code)
            ).inc()

        return response

    @app.route("/metrics")
    def metrics():
        return generate_latest(REGISTRY), 200, {'Content-Type': 'text/plain; version=0.0.4'}
```

Later, the prometheus service had to be configured to scrape the metrics from
each module's `/metrics` endpoint. This was done by cofiguring the
`prometheus.yml` file, and then establishing both prometheus and grafana
services in the docker-compose file. The following code snippet illustrates how
we configured the `prometheus.yml` file:

```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: "user-reputation-service"
    static_configs:
      - targets: ["user-reputation-service:5100"] # Asumiendo que el servicio corre en el puerto 5100
    metrics_path: "/metrics"

  - job_name: "reports-responses-service"
    static_configs:
      - targets: ["report-service:5050"] # Asumiendo que el servicio corre en el puerto 5100
    metrics_path: "/metrics"

  - job_name: "user-service"
    static_configs:
      - targets: ["login-service:5000"] # Asumiendo que el servicio corre en el puerto 5100
    metrics_path: "/metrics"

  - job_name: "notification-service"
    static_configs:
      - targets: ["notification-service:5010"] # Asumiendo que el servicio corre en el puerto 5100
    metrics_path: "/metrics"
```

With this configuration, the prometheus service runs in port 9090 and is
consumed by the grafana service at port 3000. Then, the metrics can be
visualized in Grafana dashboards, allowing us to monitor the performance and
health of our application in real-time.

### 5.7 Testing

Our comprehensive testing approach included:

#### 5.7.1 Unit Testing

- Backend: 85% code coverage using Pytest
- Isolated testing of service functions

```python
def test_create_report_success():
    # Arrange
    user_id = str(ObjectId())
    report_data = {
        'type': 'lost',
        'pet_info': {
            'name': 'Max',
            'species': 'dog',
            'breed': 'Golden Retriever'
        },
        'location': {
            'coordinates': [-74.0721, 4.7110],
            'description': 'Near Central Park'
        }
    }

    # Act
    report_id, errors = ReportService.create_report(user_id, report_data)

    # Assert
    assert report_id is not None
    assert errors is None
    assert mongo.db.reports.find_one({'_id': ObjectId(report_id)})
```

#### 5.7.2 Integration Testing

As part of our integration testing, we created a dedicated module that
integrates all the services and verifies their correct operation. This module
tests the complete request/response cycles between the frontend and backend
services, ensuring that all components work together as expected. The
integration tests , both for backend and frontend, cover:

- API endpoint testing with complete request/response cycles
- Database integration testing
- Authentication flow testing

The testing module is accessible in the
[integration testing repository](https://github.com/MascotasBogota/Test-Integracion.git)

We used Pytest for backend integration tests, ensuring all services communicate
correctly, while for frontend integration tests, we user playwright to simulate
user interactions and verify UI behavior.

## 6. Challenges and Solutions

### 6.1 Technical Challenges

#### Challenge 1: Real-time Notifications

**Problem:** Implementing efficient real-time notifications without websockets
**Solution:** Implemented polling with intelligent intervals and email fallbacks

#### Challenge 2: Image Upload and Storage

**Problem:** Handling locally uploaded images with size and format constraints
**Solution:** Used Supabase storage for scalable image hosting and URL
generation

#### Challenge 3: Geolocation Accuracy

**Problem:** Ensuring accurate location-based pet matching **Solution:**
Implemented radius-based search with user-configurable distance parameters

### 6.2 Project Management Challenges

#### Challenge 1: Feature Scope Management

**Problem:** Balancing feature completeness with development timeline
**Solution:** Implemented priority-based feature development with MVP focus

#### Challenge 2: Code Quality Consistency

**Problem:** Maintaining consistent code quality across team members
**Solution:** Established coding standards, mandatory code reviews, and
automated testing

### 6.3 Learning Outcomes

This project provided valuable experience in:

- Modern full-stack web development
- Database design and optimization
- API design and documentation
- Version control and collaboration
- Testing methodologies
- Project management and agile methodologies

---

## 7. Results and Impact

### 7.1 Technical Achievements

- **Complete Full-Stack Application:** Successfully developed and deployed a
  functioning web application
- **Scalable Architecture:** Implemented modular design supporting future
  enhancements
- **Comprehensive Testing:** Achieved high test coverage ensuring reliability

### 7.2 Functional Completeness

Our final system successfully delivers:

- User authentication and profile management
- Complete pet management lifecycle
- Efficient lost pet reporting and recovery system
- Educational content with engaging user interface
- Notification system

---

## 9. Future Enhancements and Lessons Learned

### 9.1 Identified Improvements

As an academic project, we recognize several areas for future enhancement:

1. **Real-time Features:** Implement WebSocket connections for instant
   notifications
2. **Mobile Application:** Develop native mobile apps for iOS and Android
3. **AI Integration:** Add machine learning for pet matching and breed
   identification
4. **Social Features:** Expand community features with forums and pet playdates
5. **Analytics Dashboard:** Implement comprehensive reporting and analytics

### 9.2 Lessons Learned

#### Technical Lessons

- Importance of early architectural decisions
- Value of comprehensive testing from project start
- Benefits of modular code organization
- Significance of database design for scalability

#### Project Management Lessons

- Critical importance of clear communication
- Value of iterative development and regular reviews
- Benefits of establishing coding standards early
- Importance of realistic timeline estimation

#### Team Collaboration

- Effective use of version control workflows
- Benefits of pair programming for knowledge sharing
- Importance of documentation for team coordination
- Value of regular team meetings and progress reviews

---

## 10. Conclusion

The development of PatitasBog represents a successful academic journey in modern
software engineering. Through three iterative prototypes, we created a
comprehensive pet management system that addresses real-world problems while
demonstrating proficiency in full-stack web development.

This project showcased our ability to:

- Design and implement scalable software architecture
- Apply modern development methodologies
- Collaborate effectively as a development team
- Deliver a functional, tested, and documented software system
- Manage project timelines and scope effectively

The experience gained through this academic project is yet another step that has
prepared us for professional software development challenges and highlighted the
importance of systematic approaches to complex software problems.

We acknowledge that this academic project, while functional and comprehensive,
represents a learning exercise and would benefit from additional refinement and
optimization for production deployment. The iterative approach allowed us to
deliver working software while continuously improving our technical skills and
project management capabilities.

---

**Project Timeline:** 12 weeks, 3 prototypes, 6 team members

---

_This technical post was collaboratively written by Patitas Bogota Team as part
of our Software Engineering 2 course at Universidad Nacional de Colombia. The
complete source code and documentation are available in our GitHub
repositories._

**LinkedIn:**
[Martin Moreno Jara](https://www.linkedin.com/in/martin-moreno-jara-250977242/),
[Juan Esteban Cardenas Huertas](https://www.linkedin.com/in/juan-huertaszz/),
[Juan David Ardila Diaz](https://www.linkedin.com/in/luis-felipe-tolosa-sierra-4441a2267/),[Luis Felipe Tolosa Sierra](https://www.linkedin.com/in/luis-felipe-tolosa-sierra-4441a2267/),
[David Alejandro Cifuentes Gonzalez](https://www.linkedin.com/in/dcifuentesg/),
[Keynes Stephens Watson](https://www.linkedin.com/in/keynes-stephens-watson-844550288/)

**GitHub Organization:** [MascotasBogotaOrg](https://github.com/MascotasBogota)

**Medium Publication Date:** [July 25th, 2025 ]

---
